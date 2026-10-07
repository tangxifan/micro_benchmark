import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_counter8_4clk_async_reset(dut):
    """Test 4-clock asynchronous reset counter across independent clock domains."""

    # Start 4 independent clocks with different periods (in nanoseconds)
    clock_periods = [10, 15, 20, 25]
    for i, period in enumerate(clock_periods):
        clk_handle = getattr(dut, f"clk{i}")
        cocotb.start_soon(Clock(clk_handle, period, units="ns").start())

    # --- Step 1: Apply Asynchronous Reset ---
    dut._log.info("Asserting reset...")
    dut.reset.value = 1
    await Timer(50, units="ns")

    # Verify all counters are held at 0 during reset
    for i in range(4):
        res = getattr(dut, f"result{i}").value
        assert res == 0, f"result{i} should be 0 during reset, got {res}"

    # De-assert reset asynchronously
    dut._log.info("De-asserting reset...")
    dut.reset.value = 0
    await Timer(1, units="ns")

    # --- Step 2: Verify Independent Increments ---
    # Monitor each clock domain for 10 cycles
    for i, period in enumerate(clock_periods):
        clk_handle = getattr(dut, f"clk{i}")
        result_handle = getattr(dut, f"result{i}")

        dut._log.info(f"Testing Domain {i} (Period: {period}ns)...")

        # Initial check after reset release
        expected_val = 0
        assert result_handle.value == expected_val, f"Domain {i} failed initial value"

        for step in range(1, 11):
            await RisingEdge(clk_handle)
            expected_val = (expected_val + 1) & 0xFF
            await Timer(1, units="ns")  # Small delay to settle output logic
            actual_val = int(result_handle.value)

            assert actual_val == expected_val, (
                f"Domain {i} mismatch at step {step}: " f"expected {expected_val}, got {actual_val}"
            )

    # --- Step 3: Mid-Run Asynchronous Reset Test ---
    dut._log.info("Testing mid-run asynchronous reset...")
    dut.reset.value = 1
    await Timer(5, units="ns")  # Assert mid-cycle

    for i in range(4):
        res = int(getattr(dut, f"result{i}").value)
        assert res == 0, f"result{i} failed to reset asynchronously, got {res}"

    dut.reset.value = 0
    dut._log.info("All tests passed successfully!")
