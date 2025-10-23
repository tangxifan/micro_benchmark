#####################################################################
# Test the functionality of 32 bot counter multi instances
#####################################################################
import random
import numpy as np
import cocotb
from cocotb.types import LogicArray
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_counterup32_1clk_async_reset_n_instances(dut):

    ################################################################
    # Clock Generation
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clock0, CLK_PERIOD, "ns").start())

    ################################################################

    # Test all the cases
    test_cases = 1
    COUNTER_SIZE = 32
    num_cycles = pow(2, COUNTER_SIZE)
    COUNTER_MAX_VAL = num_cycles - 1
    assert_rst = 1
    deassert_rst = 0
    expected_count = 0
    reset_rand = random.randint(0, int((num_cycles * test_cases) / 20000000))

    dut.reset.value = assert_rst
    await ClockCycles(dut.clock0, 2)

    dut.reset.value = deassert_rst
    dut.id.value = 10

    await FallingEdge(dut.clock0)
    dut._log.info("reset Test0:: count is %d", dut.count.value)
    dut._log.info("reset Test0:: expected_count is %d", expected_count)
    assert dut.count.value == expected_count, "count does not match expected value!"

    await ClockCycles(dut.clock0, 20)
    dut.reset.value = assert_rst
    await FallingEdge(dut.clock0)

    dut._log.info("CHECKING VALUE ON RESET = HIGH ")
    dut._log.info("reset Test1:: count is %d", dut.count.value)
    dut._log.info("reset Test1:: expected_count is %d", expected_count)
    assert dut.count.value == expected_count, "count does not match expected value!"
    await RisingEdge(dut.clock0)
    await Timer(1, "ns")
    dut.reset.value = deassert_rst
    await FallingEdge(dut.clock0)

    for cycle in range(
        int((num_cycles * test_cases) / 2000000)
    ):  # Divided by this number just to reduce runtime
        if cycle == reset_rand:
            await Timer(1, "ns")
            dut.reset.value = assert_rst  # Random Reset
            await Timer(1, "ns")

            dut._log.info("reset Test2:: Driving reset randomly!")
        else:
            await Timer(1, "ns")
            dut.reset.value = deassert_rst

        if expected_count == COUNTER_MAX_VAL or dut.reset.value == assert_rst:
            expected_count = 0
            await RisingEdge(dut.clock0)
            dut._log.info("count is %d", dut.count.value)
            dut._log.info("expected_count is %d", expected_count)

        else:
            await Timer(5, "ns")
            expected_count += 1
            await RisingEdge(dut.clock0)
            dut._log.info("count is %d", dut.count.value)
            dut._log.info("expected_count is %d", expected_count)

    dut._log.info("counter id is %d", dut.id.value)
    assert dut.count.value == expected_count, "count does not match expected value!"
