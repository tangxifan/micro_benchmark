import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


@cocotb.test()
async def test_timer8_16clk_async_reset(dut):
    """Test hierarchical 16-clock 8-bit countdown timer across 16 independent clock domains concurrently."""

    # Define unique integer periods for all 16 independent clock domains to avoid float precision errors
    clock_periods = [10 + i for i in range(16)]
    for i, period in enumerate(clock_periods):
        clk_handle = getattr(dut, f"clk{i}")
        cocotb.start_soon(Clock(clk_handle, period, unit="ns").start())

    # --- Step 1: Apply Asynchronous Reset ---
    dut._log.info("Asserting asynchronous reset across all 16 domains...")
    dut.reset.value = 1
    for i in range(16):
        getattr(dut, f"en{i}").value = 0
        getattr(dut, f"period{i}").value = 3

    await Timer(30, unit="ns")

    for i in range(16):
        assert int(getattr(dut, f"count{i}").value) == 0, f"count{i} should be 0 during reset"
        assert (
            int(getattr(dut, f"timer_done{i}").value) == 0
        ), f"timer_done{i} should be 0 during reset"

    # De-assert reset cleanly on the falling edge of clk0
    dut._log.info("De-asserting reset on falling edge of clk0...")
    await FallingEdge(dut.clk0)
    dut.reset.value = 0
    await Timer(1, unit="ns")

    # --- Step 2: Define Concurrent Verification Routine ---
    async def verify_domain(i, period):
        clk_handle = getattr(dut, f"clk{i}")
        en_handle = getattr(dut, f"en{i}")
        period_handle = getattr(dut, f"period{i}")
        count_handle = getattr(dut, f"count{i}")
        done_handle = getattr(dut, f"timer_done{i}")

        en_handle.value = 1
        period_handle.value = 3

        # State tracking for individual domain countdown behavior
        current_val = 0
        for step in range(1, 10):
            await RisingEdge(clk_handle)

            # Predict next state: if zero, reload period (3) and set done=1; otherwise decrement
            if current_val == 0:
                current_val = 3
                expected_done = 1
            else:
                current_val = (current_val - 1) & 0xFF
                expected_done = 0

            await Timer(1, unit="ns")  # Small delay for logic settling
            actual_count = int(count_handle.value)
            actual_done = int(done_handle.value)

            assert actual_count == current_val, (
                f"Domain {i} count mismatch at step {step}: "
                f"expected {current_val}, got {actual_count}"
            )
            assert actual_done == expected_done, (
                f"Domain {i} timer_done mismatch at step {step}: "
                f"expected {expected_done}, got {actual_done}"
            )

    # Launch verification tasks concurrently across all 16 clock domains
    tasks = [cocotb.start_soon(verify_domain(i, p)) for i, p in enumerate(clock_periods)]
    for task in tasks:
        await task

    # --- Step 3: Mid-Run Asynchronous Reset Test ---
    dut._log.info("Testing mid-run asynchronous reset on 16-clock hierarchy...")
    dut.reset.value = 1
    await Timer(5, unit="ns")

    for i in range(16):
        assert int(getattr(dut, f"count{i}").value) == 0, f"count{i} failed mid-run reset"
        assert int(getattr(dut, f"timer_done{i}").value) == 0, f"timer_done{i} failed mid-run reset"

    dut.reset.value = 0
    dut._log.info("All 16-clock hierarchical timer tests passed successfully!")
