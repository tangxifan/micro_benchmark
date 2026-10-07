import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_timer_n_clock(dut):
    """Universal verification for N-clock 8-bit countdown timers."""
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk.value)
    dut._log.info(f"Testing {num_clks}-clock domain timer configuration...")

    for i in range(num_clks):
        period = 10 + (i * 2)
        cocotb.start_soon(Clock(dut.clk[i], period, units="ns").start())

    # 1. Assert Reset
    dut.reset.value = 1
    dut.en.value = 0
    dut.period.value = 0
    await Timer(50, units="ns")
    assert int(dut.count.value) == 0, "Reset count check failed"
    assert int(dut.timer_done.value) == 0, "Reset done check failed"

    # 2. De-assert Reset & Configure Timers
    dut.reset.value = 0
    await Timer(1, units="ns")

    # Set load period of 5 cycles for all domains
    period_val = 0
    for i in range(num_clks):
        period_val |= 5 << (i * 8)
    dut.period.value = period_val
    dut.en.value = (1 << num_clks) - 1  # Enable all timers

    # 3. Test Countdown and Done Pulse Execution
    for i in range(num_clks):
        dut._log.info(f"Checking countdown for timer domain {i}...")
        # Clock down from 5 to 0
        for step in range(5, -1, -1):
            await RisingEdge(dut.clk[i])
            await Timer(1, units="ns")
            curr_cnt = (int(dut.count.value) >> (i * 8)) & 0xFF
            done_bit = (int(dut.timer_done.value) >> i) & 0x1

            if step == 0:
                assert done_bit == 1, f"Domain {i} expected timer_done assertion"
            else:
                assert done_bit == 0, f"Domain {i} unexpected timer_done high"

    # 4. Mid-run Async Reset Test
    dut.reset.value = 1
    await Timer(5, units="ns")
    assert int(dut.count.value) == 0, "Mid-run async reset count failed"
    assert int(dut.timer_done.value) == 0, "Mid-run async reset done failed"
    dut.reset.value = 0
