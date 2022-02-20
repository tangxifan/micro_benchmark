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
async def test_and2_latch(dut):
  ################################################################
  # Create clocks
  CLK_PERIOD = 10 # [ns]
  cocotb.start_soon(Clock(dut.clk, CLK_PERIOD, units="ns").start())

  ################################################################
  # Test all the cases
  test_id = 0
  for a in range(2):
    for b in range(2):
      await FallingEdge(dut.clk)
      dut._log.info("==== Begin Test case %d ====", test_id)
      dut.a.value = a
      dut.b.value = b

      await RisingEdge(dut.clk)
      dut._log.info("a is %s", dut.a.value)
      dut._log.info("b is %s", dut.b.value)
      dut._log.info("c is %s", dut.c.value)
      expected_c = a & b
      dut._log.info("expected_c is %s", expected_c)
      assert dut.c.value == expected_c, "c does not match expected value!"
 
      await FallingEdge(dut.clk)
      expected_d = a & b
      dut._log.info("d is %s", dut.c.value)
      dut._log.info("expected_d is %s", expected_d)
      assert dut.d.value == expected_d, "d does not match expected value!"
      dut._log.info("==== End Test case %d ====", test_id)
      test_id += 1
