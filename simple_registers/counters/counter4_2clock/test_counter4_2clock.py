import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer


@cocotb.test()
async def test_counter4_2clock(dut):
    # Create two independent clocks:
    # clk0: 10ns period (100 MHz)
    # clk1: 20ns period (50 MHz)
    clock0 = Clock(dut.clk0, 10, unit="ns")
    clock1 = Clock(dut.clk1, 20, unit="ns")

    cocotb.start_soon(clock0.start())
    cocotb.start_soon(clock1.start())

    dut._log.info("Starting Dual-Clock 4-bit Counter Testbench...")

    # 1. Apply synchronous/asynchronous reset on both counters
    dut.rst.value = 1
    await Timer(15, unit="ns")

    # Verify outputs are zeroed under reset
    assert int(dut.q0.value) == 0, f"Expected q0 to be 0 under reset, got {dut.q0.value}"
    assert int(dut.q1.value) == 0, f"Expected q1 to be 0 under reset, got {dut.q1.value}"
    dut._log.info("Reset state verified for both domains.")

    # 2. Release reset on a falling edge of clk0
    await FallingEdge(dut.clk0)
    dut.rst.value = 0
    dut._log.info("Reset released. Verifying dual-clock increment sequences...")

    # Track expected counts separately since frequencies differ (clk0 is 2x faster than clk1)
    expected_q0 = 0
    expected_q1 = 0

    # Step through several cycles of clk0
    for i in range(8):
        await RisingEdge(dut.clk0)
        await Timer(1, unit="ns")  # Small settle delay
        expected_q0 = (expected_q0 + 1) % 16

        assert (
            int(dut.q0.value) == expected_q0
        ), f"Cycle {i+1}: Expected q0={expected_q0}, got {dut.q0.value}"
        dut._log.info(f"clk0 edge {i+1}: q0 = {dut.q0.value}")

    # Check that q1 has incremented at its own slower pace (half the frequency)
    # After 8 cycles of clk0 (80ns), clk1 has seen 4 rising edges.
    expected_q1 = 4
    assert int(dut.q1.value) == expected_q1, f"Expected q1={expected_q1}, got {dut.q1.value}"
    dut._log.info(f"Dual-clock ratio verified: q1 = {dut.q1.value} after 4 clk1 cycles.")

    dut._log.info("Dual-clock counter test passed successfully!")
