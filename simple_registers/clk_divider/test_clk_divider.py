#####################################################################
# Test the functionality of clk_divider
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
async def clk_divider(dut):

    ################################################################
    # Clock Generation
    CLK0_PERIOD = 10  # [ns]
    # dut.clk_i.value <= 0
    cocotb.start_soon(Clock(dut.clk_i, CLK0_PERIOD, "ns").start())

    dut.rst.value = 1
    await RisingEdge(dut.clk_i)
    await RisingEdge(dut.clk_i)
    dut.rst.value = 0

    # Wait for 2 positive edges on the input clock
    for i in range(2):
        await RisingEdge(dut.clk_i)

    # Check that the output clk_o is 1
    await FallingEdge(dut.clk_i)
    assert int(dut.clk_o.value) == 1, "does not match expected value!"

    # Wait for 2 positive edges on the input clock
    for i in range(2):
        await RisingEdge(dut.clk_i)

    # Check that the output clk_o is 0
    await FallingEdge(dut.clk_i)
    assert int(dut.clk_o.value) == 0, "does not match expected value!"

    # Wait for 2 more positive edges on the input clock
    for i in range(2):
        await RisingEdge(dut.clk_i)

    # Check that the output clk_o is 1
    await FallingEdge(dut.clk_i)
    assert int(dut.clk_o.value) == 1, "does not match expected value!"
