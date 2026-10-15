import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


@cocotb.test()
async def test_counter8_async_resetb(dut):
    """Test 8-bit counter with active-low asynchronous reset (resetb)."""

    # Start a clock with a 20ns period (matching the 10ns half-period in the Verilog TB)
    clock = Clock(dut.clk, 20, unit="ns")
    cocotb.start_soon(clock.start())

    # --- Step 1: Apply Asynchronous Reset (Active-Low) ---
    dut._log.info("Asserting active-low reset (resetb = 0)...")
    dut.resetb.value = 0
    await Timer(25, unit="ns")  # Hold reset for a safe duration

    # Verify counter is held at 0 during reset
    res = int(dut.result.value)
    assert res == 0, f"result should be 0 during reset, got {res}"

    # De-assert reset cleanly on the falling edge of the clock to avoid race conditions
    dut._log.info("De-asserting reset (resetb = 1) on falling edge...")
    await FallingEdge(dut.clk)
    dut.resetb.value = 1

    # --- Step 2: Verify Sequential Increments ---
    expected_val = 0
    for step in range(1, 11):
        await RisingEdge(dut.clk)
        expected_val = (expected_val + 1) & 0xFF
        await Timer(1, unit="ns")  # Small delay to let output logic settle
        actual_val = int(dut.result.value)

        assert (
            actual_val == expected_val
        ), f"Mismatch at step {step}: expected {expected_val}, got {actual_val}"

    # --- Step 3: Mid-Run Asynchronous Reset Test ---
    dut._log.info("Testing mid-run asynchronous reset...")
    await RisingEdge(dut.clk)
    await Timer(5, unit="ns")  # Move 5ns past the rising edge (mid-cycle)

    dut.resetb.value = 0  # Assert reset active-low immediately
    await Timer(
        1, unit="ns"
    )  # Tiny delta delay to allow simulator to propagate the internal reg update

    res = int(dut.result.value)
    assert res == 0, f"result failed to reset asynchronously, got {res}"

    # Release reset to clean up the test state
    dut.resetb.value = 1
    dut._log.info("All tests passed successfully!")
