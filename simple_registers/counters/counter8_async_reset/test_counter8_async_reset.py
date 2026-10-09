import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


@cocotb.test()
async def test_counter8_async_reset(dut):
    """Test 8-bit counter with asynchronous reset and clean clock synchronization."""

    # Start a clock with a 10ns period
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # --- Step 1: Apply Asynchronous Reset ---
    dut._log.info("Asserting reset...")
    dut.reset.value = 1
    await Timer(25, unit="ns")  # Hold reset for a safe duration

    # Verify counter is held at 0 during reset
    res = int(dut.result.value)
    assert res == 0, f"result should be 0 during reset, got {res}"

    # De-assert reset cleanly on the falling edge of the clock to avoid race conditions
    dut._log.info("De-asserting reset on falling edge...")
    await FallingEdge(dut.clk)
    dut.reset.value = 0

    # --- Step 2: Verify Sequential Increments ---
    expected_val = 0
    for step in range(1, 11):
        await RisingEdge(dut.clk)
        expected_val = (expected_val + 1) & 0xFF
        await Timer(1, unit="ns")  # Small delay to settle output logic
        actual_val = int(dut.result.value)

        assert (
            actual_val == expected_val
        ), f"Mismatch at step {step}: expected {expected_val}, got {actual_val}"

    # --- Step 3: Mid-Run Asynchronous Reset Test ---
    dut._log.info("Testing mid-run asynchronous reset...")
    dut.reset.value = 1
    await Timer(5, unit="ns")  # Assert mid-cycle asynchronously

    res = int(dut.result.value)
    assert res == 0, f"result failed to reset asynchronously, got {res}"

    dut.reset.value = 0
    dut._log.info("All tests passed successfully!")
