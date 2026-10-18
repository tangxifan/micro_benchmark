import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_dual_mult8_mix_regin(dut):
    """Testbench verifying dual 8-bit multipliers (combinational vs input-registered)."""

    # Start a 10ns period clock (100 MHz)[cite: 7]
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting dual_mult8_mix_regin simulation...")

    # Apply synchronous reset[cite: 7, 9]
    dut.rst.value = 1
    dut.a0.value = 0
    dut.b0.value = 0
    dut.a1.value = 0
    dut.b1.value = 0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # Test cases: (a, b) pairs
    test_vectors = [
        (10, 20),
        (15, 15),
        (255, 2),
        (12, 34),
        (100, 200),
    ]

    for val_a, val_b in test_vectors:
        # Drive inputs on both channels simultaneously[cite: 7]
        dut.a0.value = val_a
        dut.b0.value = val_b
        dut.a1.value = val_a
        dut.b1.value = val_b

        # -------------------------------------------------------------
        # 1. Check combinational output (out0) after brief propagation delay[cite: 7, 8]
        # -------------------------------------------------------------
        await Timer(1, unit="ns")
        expected_out0 = val_a * val_b
        actual_out0 = int(dut.out0.value)

        cocotb.log.info(
            f"[Combinational] {val_a} * {val_b} = {actual_out0} (Expected: {expected_out0})"
        )
        assert actual_out0 == expected_out0, (
            f"out0 mismatch! Expected {expected_out0}, got {actual_out0}"
        )

        # -------------------------------------------------------------
        # 2. Check registered output (out1) after 1 clock cycle[cite: 7, 9]
        # -------------------------------------------------------------
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        expected_out1 = val_a * val_b
        actual_out1 = int(dut.out1.value)

        cocotb.log.info(
            f"[Registered]    {val_a} * {val_b} = {actual_out1} (Expected: {expected_out1})"
        )
        assert actual_out1 == expected_out1, (
            f"out1 mismatch! Expected {expected_out1}, got {actual_out1}"
        )

    cocotb.log.info("dual_mult8_mix_regin simulation completed successfully!")
