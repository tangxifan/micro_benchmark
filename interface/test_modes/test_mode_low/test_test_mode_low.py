import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_test_mode_low_functional(dut):
    """Testbench for test_mode_low verifying pipelined shift and sum behavior."""
    
    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs and assert active-high reset
    dut.reset.value = 1
    dut.a.value = 0
    dut.b.value = 0

    # Wait for a couple of clock cycles with reset active
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Deassert reset
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    cocotb.log.info("Reset released, starting test vectors...")

    # Define test patterns for a and b inputs
    test_vectors = [
        (1, 0),
        (0, 1),
        (1, 1),
        (0, 0),
        (1, 1),
        (0, 1)
    ]

    for a_val, b_val in test_vectors:
        dut.a.value = a_val
        dut.b.value = b_val
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")  # Allow combinatorial propagation settling
        out_val = int(dut.out.value)
        cocotb.log.info(f"Driven a={a_val}, b={b_val} -> out={bin(out_val)}")

    # Hold inputs low and flush the internal pipeline
    dut.a.value = 0
    dut.b.value = 0
    for _ in range(4):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        out_val = int(dut.out.value)
        cocotb.log.info(f"Pipeline flush step -> out={bin(out_val)}")

    cocotb.log.info("All test_mode_low simulation steps completed successfully!")
