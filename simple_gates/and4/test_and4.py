#####################################################################
# Test the functionality of AND gate
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_and4(dut):
    ################################################################
    # Test all the cases
    clock_period = 1
    test_id = 0
    num_inputs = 4
    num_tests = pow(2, num_inputs)
    for itest in range(num_tests):
        input_vector = BinaryValue(itest, n_bits=num_inputs).binstr
        a = int(input_vector[0])
        b = int(input_vector[1])
        c = int(input_vector[2])
        d = int(input_vector[3])
        dut._log.info("==== Begin Test case %d ====", itest)
        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d
        await Timer(clock_period, units="ns")
        dut._log.info("a is %s", dut.a.value)
        dut._log.info("b is %s", dut.b.value)
        dut._log.info("c is %s", dut.c.value)
        dut._log.info("d is %s", dut.d.value)
        expected_e = a & b & c & d
        dut._log.info("expected_e is %s", expected_e)
        assert dut.e.value == expected_e, "e does not match expected value!"
        dut._log.info("==== End Test case %d ====", itest)
        itest += 1
