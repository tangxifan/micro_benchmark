#####################################################################
# Test the functionality of adders
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

@cocotb.test()
async def test_adder_6(dut):
  ################################################################
  # Test a number of random vectors
  num_tests = 100
  adder_size = 6
  clock_period = 1
  for cycle in range(num_tests):
    dut._log.info("======== BEGIN iteration %d ========", cycle)
    a = random.randint(0, pow(2, adder_size) - 1)
    b = random.randint(0, pow(2, adder_size) - 1)
    cin = random.randint(0, 1)
    dut.a.value = BinaryValue(a, n_bits=adder_size).integer
    dut.b.value = BinaryValue(b, n_bits=adder_size).integer
    dut.cin.value = cin
    await Timer(clock_period, units="ns")
    dut._log.info("a is %d", dut.a.value)
    dut._log.info("b is %d", dut.b.value)
    dut._log.info("cin is %d", dut.cin.value)
    dut._log.info("cout is %d", dut.cout.value)
    dut._log.info("sum is %d", dut.sum.value)
    expected_sum = BinaryValue(dut.a.value.integer + dut.b.value.integer + dut.cin.value.integer, n_bits=adder_size).integer
    dut._log.info("expected_sum is %d", expected_sum)
    assert dut.sum.value == expected_sum, "sum does not match expected value!"
    dut._log.info("======== END iteration %d ========", cycle)
