#####################################################################
# Test the functionality of dual-clock registered AND gate
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_and2_latch_2clock(dut):
    ################################################################
    # Create clocks
    CLK0_PERIOD = 10  # [ns]
    CLK1_PERIOD = 20  # [ns]
    cocotb.start_soon(Clock(dut.clk0, CLK0_PERIOD, units="ns").start())
    cocotb.start_soon(Clock(dut.clk1, CLK1_PERIOD, units="ns").start())

    ################################################################
    # Test all the cases
    test_id = 0
    for a in range(2):
        for b in range(2):
            await FallingEdge(dut.clk0)
            dut._log.info("==== Begin Test case %d ====", test_id)
            dut.a0.value = a
            dut.b0.value = b

            await RisingEdge(dut.clk0)
            dut._log.info("a0 is %s", dut.a0.value)
            dut._log.info("b0 is %s", dut.b0.value)
            dut._log.info("c0 is %s", dut.c0.value)
            expected_c = a & b
            dut._log.info("expected_c is %s", expected_c)
            assert dut.c0.value == expected_c, "c does not match expected value!"

            await FallingEdge(dut.clk0)
            expected_d = a & b
            dut._log.info("d0 is %s", dut.d0.value)
            dut._log.info("expected_d is %s", expected_d)
            assert dut.d0.value == expected_d, "d does not match expected value!"
            dut._log.info("==== End Test case %d ====", test_id)
            test_id += 1

    for a in range(2):
        for b in range(2):
            await FallingEdge(dut.clk1)
            dut._log.info("==== Begin Test case %d ====", test_id)
            dut.a1.value = a
            dut.b1.value = b

            await RisingEdge(dut.clk1)
            dut._log.info("a1 is %s", dut.a1.value)
            dut._log.info("b1 is %s", dut.b1.value)
            dut._log.info("c1 is %s", dut.c1.value)
            expected_c = a & b
            dut._log.info("expected_c is %s", expected_c)
            assert dut.c1.value == expected_c, "c does not match expected value!"

            await FallingEdge(dut.clk1)
            expected_d = a & b
            dut._log.info("d1 is %s", dut.d1.value)
            dut._log.info("expected_d is %s", expected_d)
            assert dut.d1.value == expected_d, "d does not match expected value!"
            dut._log.info("==== End Test case %d ====", test_id)
            test_id += 1
