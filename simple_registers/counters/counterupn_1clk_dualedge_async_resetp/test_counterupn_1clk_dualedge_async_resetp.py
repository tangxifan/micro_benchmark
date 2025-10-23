#####################################################################
# Test the functionality of dual_edge_up_counter
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
async def counterupn_1clk_dualedge_async_resetp(dut):

    ################################################################
    # Clock Generation
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clk, CLK_PERIOD, "ns").start())

    ################################################################

    # Test all the cases
    test_cases = 1
    COUNTER_SIZE = 12
    num_cycles = pow(2, COUNTER_SIZE)
    COUNTER_MAX_VAL = num_cycles - 1
    assert_rst = 1
    deassert_rst = 0
    expected_count = 0
    rst_counter_rand = random.randint(0, int((num_cycles * test_cases) / COUNTER_SIZE))

    dut.rst_counter.value = assert_rst
    await ClockCycles(dut.clk, 2)

    await RisingEdge(dut.clk)
    await Timer(1, "ns")
    dut.rst_counter.value = deassert_rst

    await FallingEdge(dut.clk)
    dut._log.info("rst_counter Test0:: count is %d", dut.q_counter.value)
    dut._log.info("rst_counter Test0:: expected_count is %d", expected_count)
    assert dut.q_counter.value == expected_count, "count does not match expected value!"

    await ClockCycles(dut.clk, 20)
    await RisingEdge(dut.clk)
    dut.rst_counter.value = assert_rst
    await FallingEdge(dut.clk)

    dut._log.info("CHECKING VALUE ON RESET = HIGH ")
    dut._log.info("rst_counter Test1:: count is %d", dut.q_counter.value)
    dut._log.info("rst_counter Test1:: expected_count is %d", expected_count)
    assert dut.q_counter.value == expected_count, "count does not match expected value!"
    await RisingEdge(dut.clk)
    await Timer(1, "ns")
    dut.rst_counter.value = deassert_rst
    await FallingEdge(dut.clk)

    for cycle in range(
        int((num_cycles * test_cases) / COUNTER_SIZE)
    ):  # Divided by COUNTER_SIZE just to reduce runtime
        if cycle == rst_counter_rand:
            await Timer(1, "ns")
            dut.rst_counter.value = assert_rst  # Random Reset
            await RisingEdge(dut.clk)
            dut._log.info("rst_counter Test2:: Driving rst_counter randomly!")
        else:
            await Timer(1, "ns")
            dut.rst_counter.value = deassert_rst

        await Timer(1, "ns")

        if expected_count == COUNTER_MAX_VAL or dut.rst_counter.value == assert_rst:
            expected_count = 0
            dut._log.info("RESET is %d", dut.rst_counter.value)
            dut._log.info("count is %d", dut.q_counter.value)
            dut._log.info("expected_count is %d", expected_count)

        else:
            await RisingEdge(dut.clk)
            expected_count += 1
            dut._log.info("RESET is %d", dut.rst_counter.value)
            dut._log.info("count is %d", dut.q_counter.value)
            dut._log.info("expected_count is %d", expected_count)

            await FallingEdge(dut.clk)
            expected_count += 1
            dut._log.info("RESET is %d", dut.rst_counter.value)
            dut._log.info("count is %d", dut.q_counter.value)
            dut._log.info("expected_count is %d", expected_count)

        if expected_count >= COUNTER_MAX_VAL or dut.rst_counter.value == assert_rst:
            expected_count = 0

        assert dut.q_counter.value == expected_count, "count does not match expected value!"
