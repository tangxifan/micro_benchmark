#####################################################################
# Test the functionality of AND and OR gate
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_and2_or2(dut):
    ################################################################
    # Test all the cases
    clock_period = 1
    test_id = 0
    for a in range(2):
        for b in range(2):
            dut._log.info("==== Begin Test case %d ====", test_id)
            dut.a.value = a
            dut.b.value = b
            await Timer(clock_period, units="ns")
            dut._log.info("a is %s", dut.a.value)
            dut._log.info("b is %s", dut.b.value)
            dut._log.info("c is %s", dut.c.value)
            expected_c = a & b
            expected_d = a | b
            dut._log.info("expected_c is %s", expected_c)
            dut._log.info("expected_d is %s", expected_d)
            assert dut.c.value == expected_c, "c does not match expected value!"
            assert dut.d.value == expected_d, "c does not match expected value!"
            dut._log.info("==== End Test case %d ====", test_id)
            test_id += 1
