import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_counter8_sync_reset(dut):
    """Test 8-bit counter with active-high synchronous reset."""

    # Start a clock with a 20ns period (matching the 10ns half-period in the Verilog TB)
    clock = Clock(dut.clk_counter, 20, unit="ns")
    cocotb.start_soon(clock.start())

    # --- Step 1: Apply Synchronous Reset ---
    dut._log.info("Asserting synchronous reset (rst_counter = 1)...")
    dut.rst_counter.value = 1

    # Run for 2 full clock cycles to ensure reset is sampled on a rising edge
    for _ in range(2):
        await RisingEdge(dut.clk_counter)

    # Verify counter is held at 0 after the clock edges during active reset
    res = int(dut.q_counter.value)
    assert res == 0, f"q_counter should be 0 during reset, got {res}"

    # De-assert reset synchronously right on the rising edge
    dut.rst_counter.value = 0
    dut._log.info("De-asserting reset (rst_counter = 0)...")

    # --- Step 2: Verify Sequential Increments ---
    expected_val = 0
    for step in range(1, 11):
        await RisingEdge(dut.clk_counter)
        expected_val = (expected_val + 1) & 0xFF
        await Timer(1, unit="ns")  # Small delay to let non-blocking outputs settle
        actual_val = int(dut.q_counter.value)

        assert (
            actual_val == expected_val
        ), f"Mismatch at step {step}: expected {expected_val}, got {actual_val}"

    # --- Step 3: Mid-Run Synchronous Reset Test ---
    dut._log.info("Testing mid-run synchronous reset...")

    # Assert reset mid-cycle (it shouldn't affect the output immediately because it's synchronous)
    dut.rst_counter.value = 1
    await Timer(5, unit="ns")

    # Check that output has NOT reset yet (synchronous reset waits for the edge)
    actual_val_mid = int(dut.q_counter.value)
    assert (
        actual_val_mid == expected_val
    ), f"Counter reset prematurely before the clock edge, got {actual_val_mid}"

    # Wait for the next clock edge where the reset should actually be sampled
    await RisingEdge(dut.clk_counter)
    await Timer(1, unit="ns")  # Let the simulator propagate the sequential assignment

    res_after_edge = int(dut.q_counter.value)
    assert (
        res_after_edge == 0
    ), f"q_counter failed to reset synchronously on clock edge, got {res_after_edge}"

    # Release reset to leave the testbench in a clean state
    dut.rst_counter.value = 0
    dut._log.info("All synchronous test phases passed successfully!")
