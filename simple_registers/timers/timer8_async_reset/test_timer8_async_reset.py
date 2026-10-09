import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


@cocotb.test()
async def test_timer8_async_reset(dut):
    """Test single-clock 8-bit countdown timer with async reset, enable, and reload behavior."""

    # Start a 10ns clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # --- Step 1: Apply Asynchronous Reset ---
    dut._log.info("Asserting asynchronous reset...")
    dut.reset.value = 1
    dut.en.value = 0
    dut.period.value = 5
    await Timer(20, unit="ns")

    assert int(dut.count.value) == 0, f"Expected count=0 during reset, got {dut.count.value}"
    assert (
        int(dut.timer_done.value) == 0
    ), f"Expected timer_done=0 during reset, got {dut.timer_done.value}"

    # De-assert reset cleanly on falling edge
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await Timer(1, unit="ns")

    # --- Step 2: Test Disabled State (en = 0) ---
    dut._log.info("Testing disabled state...")
    dut.en.value = 0
    dut.period.value = 3
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")

    assert int(dut.count.value) == 0, f"Count should remain 0 when disabled, got {dut.count.value}"
    assert (
        int(dut.timer_done.value) == 0
    ), f"Timer done should be 0 when disabled, got {dut.timer_done.value}"

    # --- Step 3: Test Countdown Sequence (period = 3) ---
    dut._log.info("Testing countdown sequence with period=3...")
    dut.en.value = 1
    dut.period.value = 3

    # Cycle 1: count is 0 -> reloads period (3), sets timer_done = 1
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 3, f"Expected count=3 after reload, got {dut.count.value}"
    assert (
        int(dut.timer_done.value) == 1
    ), f"Expected timer_done=1 on reload cycle, got {dut.timer_done.value}"

    # Cycle 2: count decrements to 2, timer_done = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 2, f"Expected count=2, got {dut.count.value}"
    assert int(dut.timer_done.value) == 0, f"Expected timer_done=0, got {dut.timer_done.value}"

    # Cycle 3: count decrements to 1, timer_done = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 1, f"Expected count=1, got {dut.count.value}"
    assert int(dut.timer_done.value) == 0, f"Expected timer_done=0, got {dut.timer_done.value}"

    # Cycle 4: count decrements to 0, timer_done = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 0, f"Expected count=0, got {dut.count.value}"
    assert int(dut.timer_done.value) == 0, f"Expected timer_done=0, got {dut.timer_done.value}"

    # Cycle 5: count hits 0 -> reloads period (3) again, timer_done = 1
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 3, f"Expected count=3 after second reload, got {dut.count.value}"
    assert (
        int(dut.timer_done.value) == 1
    ), f"Expected timer_done=1 on reload cycle, got {dut.timer_done.value}"

    # --- Step 4: Test Mid-Run Asynchronous Reset ---
    dut._log.info("Testing mid-run asynchronous reset...")
    dut.reset.value = 1
    await Timer(5, unit="ns")

    assert (
        int(dut.count.value) == 0
    ), f"Expected count=0 during mid-run reset, got {dut.count.value}"
    assert (
        int(dut.timer_done.value) == 0
    ), f"Expected timer_done=0 during mid-run reset, got {dut.timer_done.value}"

    dut.reset.value = 0
    dut._log.info("All timer tests passed successfully!")
