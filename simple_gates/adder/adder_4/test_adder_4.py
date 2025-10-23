#####################################################################
# Test the functionality of adders
#####################################################################
import random
import cocotb
from cocotb.types import LogicArray
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_adder_4(dut):
    ################################################################
    # Test a number of random vectors
    num_tests = 100
    adder_size = 4
    clock_period = 1
    for cycle in range(num_tests):
        dut._log.info("======== BEGIN iteration %d ========", cycle)
        a = random.randint(0, pow(2, adder_size) - 1)
        b = random.randint(0, pow(2, adder_size) - 1)
        cin = random.randint(0, 0)
        dut.a.value = LogicArray(a, adder_size).to_unsigned()
        dut.b.value = LogicArray(b, adder_size).to_unsigned()
        dut.cin.value = cin
        await Timer(clock_period, "ns")
        dut._log.info("a is %d", dut.a.value)
        dut._log.info("b is %d", dut.b.value)
        dut._log.info("cin is %d", dut.cin.value)
        dut._log.info("cout is %d", dut.cout.value)
        dut._log.info("sum is %d", dut.sum.value)
        expected_out = dut.a.value.to_unsigned() + dut.b.value.to_unsigned() + int(dut.cin.value)
        expected_out = expected_out % (1 << adder_size)  # only keep lowest width bits
        expected_sum = LogicArray(expected_out, adder_size).to_unsigned()
        dut._log.info("expected_sum is %d", expected_sum)
        assert dut.sum.value == expected_sum, "sum does not match expected value!"
        dut._log.info("======== END iteration %d ========", cycle)
