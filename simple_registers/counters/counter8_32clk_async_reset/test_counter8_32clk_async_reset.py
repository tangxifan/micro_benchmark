import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, ReadOnly


@cocotb.test()
async def test_counter8_32clk_async_reset(dut):
    """Test 32-clock asynchronous reset counter across independent clock domains concurrently."""

    clock_periods = [10 + (i * 1.5) for i in range(32)]
    for i, period in enumerate(clock_periods):
        clk_handle = getattr(dut, f"clk{i}")
        cocotb.start_soon(Clock(clk_handle, period, unit="ns").start())

    # --- Step 1: Apply Asynchronous Reset ---
    dut._log.info("Asserting reset...")
    dut.reset.value = 1
    await Timer(30, unit="ns")

    for i in range(32):
        res = int(getattr(dut, f"result{i}").value)
        assert res == 0, f"result{i} should be 0 during reset, got {res}"

    # --- Step 2: Define Concurrent Verification Routine ---
    async def verify_domain(i, period):
        clk_handle = getattr(dut, f"clk{i}")
        result_handle = getattr(dut, f"result{i}")
        
        dut._log.info(f"Monitoring Domain {i} (Period: {period}ns)...")
        
        # Wait until reset is de-asserted
        while dut.reset.value == 1:
            await RisingEdge(clk_handle)

        expected_val = 0
        for step in range(1, 11):
            await RisingEdge(clk_handle)
            expected_val = (expected_val + 1) & 0xFF
            await Timer(1, unit="ns")
            actual_val = int(result_handle.value)

            assert actual_val == expected_val, (
                f"Domain {i} mismatch at step {step}: "
                f"expected {expected_val}, got {actual_val}"
            )

    # Launch verification tasks for all 32 domains BEFORE releasing reset
    tasks = [cocotb.start_soon(verify_domain(i, period)) for i, period in enumerate(clock_periods)]

    # De-assert reset cleanly
    dut._log.info("De-asserting reset...")
    dut.reset.value = 0

    # Wait for all domains to complete their 10 cycles
    for task in tasks:
        await task

    # --- Step 3: Mid-Run Asynchronous Reset Test ---
    dut._log.info("Testing mid-run asynchronous reset...")
    dut.reset.value = 1
    await Timer(5, unit="ns")

    for i in range(32):
        res = int(getattr(dut, f"result{i}").value)
        assert res == 0, f"result{i} failed to reset asynchronously, got {res}"

    dut.reset.value = 0
    dut._log.info("All tests passed successfully!")
