#####################################################################
# Test the functionality of 16 bit Counter
#####################################################################
import random
import numpy as np
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


async def reset_dut(reset, active_high, delay_ns, duration_ns):
    ASSERT_RST = 0
    DEASSERT_RST = 1
    if active_high:
        ASSERT_RST = 1
        DEASSERT_RST = 0
    # Wait sometime to start if required
    if delay_ns > 0:
        reset.value = DEASSERT_RST
        await Timer(delay_ns, units="ns")
    reset.value = ASSERT_RST
    await Timer(duration_ns, units="ns")
    reset.value = DEASSERT_RST
    reset._log.debug("Reset complete")


# Counter test
async def counter(dut, clk, cnt, msg):
    test_cases = 1
    COUNTER_SIZE = 16
    num_cycles = pow(2, COUNTER_SIZE)
    COUNTER_MAX_VAL = num_cycles - 1
    assert_rst = 0
    deassert_rst = 1
    expected_count = 0

    dut._log.info("Reset Test0:: %s is %d", msg, cnt.value)
    dut._log.info("Reset Test0:: expected_count is %d", expected_count)
    assert cnt.value == expected_count, msg + "does not match expected value!"

    for cycle in range(
        int((num_cycles * test_cases) / COUNTER_SIZE)
    ):  # Divided by COUNTER_SIZE just to reduce runtime
        await RisingEdge(clk)
        if expected_count == COUNTER_MAX_VAL or dut.reset.value == assert_rst:
            expected_count = 0
            if dut.reset.value == assert_rst:
                dut._log.info("Reset Test1:: Reset in Middle!")
        else:
            expected_count += 1

        await FallingEdge(clk)
        if dut.reset.value == assert_rst:
            dut._log.info("Reset Test1:: Reset in Middle!")
            expected_count = 0

        dut._log.info("%s is %d", msg, cnt.value)
        dut._log.info("expected_count is %d", expected_count)
        assert cnt.value == expected_count, msg + " does not match expected value!"


@cocotb.test()
async def test_counterup16_7clk_posedge_async_resetn(dut):

    ################################################################
    # Clock Generation
    CLK0_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clock0, CLK0_PERIOD, units="ns").start())
    CLK1_PERIOD = 20  # [ns]
    cocotb.start_soon(Clock(dut.clock1, CLK1_PERIOD, units="ns").start())
    CLK2_PERIOD = 30  # [ns]
    cocotb.start_soon(Clock(dut.clock2, CLK2_PERIOD, units="ns").start())
    CLK3_PERIOD = 40  # [ns]
    cocotb.start_soon(Clock(dut.clock3, CLK3_PERIOD, units="ns").start())
    CLK4_PERIOD = 50  # [ns]
    cocotb.start_soon(Clock(dut.clock4, CLK4_PERIOD, units="ns").start())
    CLK5_PERIOD = 60  # [ns]
    cocotb.start_soon(Clock(dut.clock5, CLK5_PERIOD, units="ns").start())
    CLK6_PERIOD = 70  # [ns]
    cocotb.start_soon(Clock(dut.clock6, CLK6_PERIOD, units="ns").start())

    max_clock = max(
        CLK6_PERIOD, CLK5_PERIOD, CLK4_PERIOD, CLK3_PERIOD, CLK2_PERIOD, CLK1_PERIOD, CLK0_PERIOD
    )

    await cocotb.start_soon(reset_dut(dut.reset, False, 0, 1))
    rst_in_middle_thread = cocotb.start_soon(reset_dut(dut.reset, False, 8000, max_clock))

    counter_thread0 = cocotb.start_soon(counter(dut, dut.clock0, dut.cnt0_16, "count0"))
    counter_thread1 = cocotb.start_soon(counter(dut, dut.clock1, dut.cnt1_16, "count1"))
    counter_thread2 = cocotb.start_soon(counter(dut, dut.clock2, dut.cnt2_16, "count2"))
    counter_thread3 = cocotb.start_soon(counter(dut, dut.clock3, dut.cnt3_16, "count3"))
    counter_thread4 = cocotb.start_soon(counter(dut, dut.clock4, dut.cnt4_16, "count4"))
    counter_thread5 = cocotb.start_soon(counter(dut, dut.clock5, dut.cnt5_16, "count5"))
    counter_thread6 = cocotb.start_soon(counter(dut, dut.clock6, dut.cnt6_16, "count6"))

    # Wait to finish all the threads
    await counter_thread6
    await counter_thread5
    await counter_thread4
    await counter_thread3
    await counter_thread2
    await counter_thread1
    await counter_thread0
