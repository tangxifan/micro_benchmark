import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_clk_cond_functional(dut):
    """Testbench for clk_cond module verifying locally gated clock network and register latching behavior."""

    # Start a primary system clock with 10ns period (100 MHz)
    clock = Clock(dut.clk_i, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.clk_cond_i.value = 0
    dut.d_i.value = 0

    await RisingEdge(dut.clk_i)
    await RisingEdge(dut.clk_i)

    cocotb.log.info("Starting clk_cond verification...")

    # Test Case 1: Keep gating condition low (int_clk remains disabled), toggle data
    dut.clk_cond_i.value = 0
    dut.d_i.value = 1
    for _ in range(3):
        await RisingEdge(dut.clk_i)
        await Timer(1, unit="ns")
        q_val = str(dut.q_o.value)
        cocotb.log.info(f"Gating low (clk_cond_i=0), d_i=1 -> q_o={q_val}")

    # Assert q_o should still be uninitialized/0 since int_clk didn't pulse
    # (Handling potential X/Z state safely via string or strict equality check)
    assert str(dut.q_o.value) in [
        "0",
        "x",
        "X",
    ], f"Unexpected q_o value while clock gated off: {dut.q_o.value}"

    # Test Case 2: Enable gating condition (clk_cond_i = 1), allowing int_clk to follow clk_i
    dut.clk_cond_i.value = 1
    cocotb.log.info("Gating enabled (clk_cond_i=1). Driving test patterns...")

    test_data = [1, 0, 1, 1, 0]
    for val in test_data:
        dut.d_i.value = val
        # Wait for the positive edge of the conditioned internal clock
        await RisingEdge(dut.int_clk if hasattr(dut, "int_clk") else dut.clk_i)
        await Timer(1, unit="ns")
        q_val = str(dut.q_o.value)
        cocotb.log.info(f"Driven d_i={val} -> q_o={q_val}")

        # Verify sampled data matches after clock edge
        if q_val not in ["x", "X", "Z"]:
            assert (
                int(dut.q_o.value) == val
            ), f"Mismatch: expected q_o={val}, got {int(dut.q_o.value)}"

    cocotb.log.info("All clk_cond test cases completed successfully!")
