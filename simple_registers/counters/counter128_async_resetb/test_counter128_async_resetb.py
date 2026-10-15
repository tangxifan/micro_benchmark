import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer


@cocotb.test()
async def test_counter128_async_resetb(dut):
    # Create a 10ns period clock (100 MHz) on clk
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    dut._log.info("Starting Counter 128 Async Active-Low Reset Testbench...")

    # 1. Test Asynchronous Active-Low Reset at startup (resetb = 0)
    dut.resetb.value = 0
    await Timer(5, unit="ns")  # Apply reset asynchronously between clock edges

    # Check that result is cleared to 0 under reset
    assert (
        int(dut.result.value) == 0
    ), f"Expected result to be 0 under active-low reset, got {dut.result.value}"
    dut._log.info("Async active-low reset verified: result is 0.")

    # 2. Release reset (resetb = 1) on a falling edge to avoid race conditions with rising edge
    await FallingEdge(dut.clk)
    dut.resetb.value = 1
    dut._log.info("Reset released. Verifying increment sequence...")

    expected_val = 0
    for i in range(5):
        await RisingEdge(dut.clk)
        # Wait a small delay for output register updates to settle
        await Timer(1, unit="ns")
        expected_val += 1
        assert (
            int(dut.result.value) == expected_val
        ), f"Expected result {expected_val}, got {dut.result.value}"
        dut._log.info(f"Cycle {i+1}: result = {dut.result.value}")

    # 3. Test asynchronous active-low reset assertion during operation (resetb = 0)
    dut._log.info("Testing mid-operation async active-low reset...")
    dut.resetb.value = 0
    await Timer(3, unit="ns")  # Assert reset asynchronously
    assert (
        int(dut.result.value) == 0
    ), f"Expected result to reset to 0 asynchronously, got {dut.result.value}"

    # Deassert reset on falling edge and check resumption
    await FallingEdge(dut.clk)
    dut.resetb.value = 1
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert (
        int(dut.result.value) == 1
    ), f"Expected result to resume counting from 1, got {dut.result.value}"

    dut._log.info("Counter 128 active-low reset test passed successfully!")
