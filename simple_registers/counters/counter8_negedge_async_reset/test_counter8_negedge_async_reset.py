import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer


@cocotb.test()
async def test_counter8_negedge_async_reset(dut):
    """Testbench verifying 8-bit negative-edge counter with asynchronous reset."""

    # Start a 10ns period clock on clkn
    clock = Clock(dut.clkn, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting counter8_negedge_async_reset simulation...")

    # 1. Test Asynchronous Reset
    dut.reset.value = 1
    await Timer(2, unit="ns")
    assert int(dut.result.value) == 0, f"Reset failed! Expected 0, got {int(dut.result.value)}"
    cocotb.log.info("Asynchronous reset verified successfully.")

    # Release reset
    dut.reset.value = 0
    await Timer(3, unit="ns")

    # 2. Test Counting on Negative Edges of clkn
    expected_count = 0
    for i in range(10):
        # Wait for the negative edge where the counter increments
        await FallingEdge(dut.clkn)
        await Timer(1, unit="ns")  # Small propagation delay for non-blocking assignment

        expected_count = (expected_count + 1) & 0xFF
        actual_count = int(dut.result.value)

        cocotb.log.info(f"Cycle {i+1}: Count = {actual_count} (Expected: {expected_count})")
        assert (
            actual_count == expected_count
        ), f"Count mismatch at cycle {i+1}! Expected {expected_count}, got {actual_count}"

    # 3. Test Asynchronous Reset during operation
    dut.reset.value = 1
    await Timer(2, unit="ns")
    assert (
        int(dut.result.value) == 0
    ), f"Mid-operation reset failed! Expected 0, got {int(dut.result.value)}"

    dut.reset.value = 0
    await FallingEdge(dut.clkn)
    await Timer(1, unit="ns")
    assert (
        int(dut.result.value) == 1
    ), f"Recovery after reset failed! Expected 1, got {int(dut.result.value)}"

    cocotb.log.info("counter8_negedge_async_reset simulation completed successfully!")
