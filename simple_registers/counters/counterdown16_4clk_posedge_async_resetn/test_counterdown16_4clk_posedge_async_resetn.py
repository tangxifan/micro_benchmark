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

@cocotb.test()
async def test_counterdown16_4clk_posedge_async_resetn(dut):

  ################################################################
	# Clock Generation
	CLK0_PERIOD = 10 # [ns]
	cocotb.start_soon(Clock(dut.clock0, CLK0_PERIOD, units="ns").start())
	CLK1_PERIOD = 20 # [ns]
	cocotb.start_soon(Clock(dut.clock1, CLK1_PERIOD, units="ns").start())
	CLK2_PERIOD = 30 # [ns]
	cocotb.start_soon(Clock(dut.clock2, CLK2_PERIOD, units="ns").start())
	CLK3_PERIOD = 40 # [ns]
	cocotb.start_soon(Clock(dut.clock3, CLK3_PERIOD, units="ns").start())

	################################################################
	
	# Counter0 test
	################################################################
	
	# Test all the cases
	test_cases = 2
	COUNTER_SIZE = 16
	num_cycles = pow(2, COUNTER_SIZE)
	COUNTER_MIN_VAL = 0 
	assert_rst = 0
	deassert_rst = 1
	expected_count = 0Xffff
	rst_counter_rand = random.randint(0, num_cycles*test_cases)
	
	dut.reset.value = assert_rst
	await ClockCycles(dut.clock0, 2)
	
	await RisingEdge(dut.clock0)
	dut.reset.value = deassert_rst
	
	await FallingEdge(dut.clock0)
	dut._log.info("Reset Test0:: count0 is %d", dut.cnt0_16.value)
	dut._log.info("Reset Test0:: expected_count is %d", expected_count)
	assert dut.cnt0_16.value == expected_count, "count0 does not match expected value!"

	await ClockCycles(dut.clock0, 20)
	await RisingEdge(dut.clock0)
	dut.reset.value = assert_rst
	await FallingEdge(dut.clock0)
	dut._log.info("Reset Test1:: count0 is %d", dut.cnt0_16.value)
	dut._log.info("Reset Test1:: expected_count is %d", expected_count)
	assert dut.cnt0_16.value == expected_count, "count0 does not match expected value!"
	await RisingEdge(dut.clock0)
	dut.reset.value = deassert_rst
	await FallingEdge(dut.clock0)
	
	for cycle in range(num_cycles*test_cases):
		if cycle == rst_counter_rand:
			dut.reset.value = assert_rst
			dut._log.info("Reset Test2:: Driving reset randomly!")
		else:
			dut.reset.value = deassert_rst
			
		await RisingEdge(dut.clock0)
		if expected_count == COUNTER_MIN_VAL or dut.reset.value == assert_rst:
			expected_count = 0Xffff
		else:
			expected_count -= 1
			
		await FallingEdge(dut.clock0)
		dut._log.info("count0 is %d", dut.cnt0_16.value)
		dut._log.info("expected_count is %d", expected_count)
		assert dut.cnt0_16.value == expected_count, "count0 does not match expected value!"

  ################################################################
	
	# Counter1 test
	################################################################
	
	test_cases = 2
	COUNTER_SIZE = 16
	num_cycles = pow(2, COUNTER_SIZE)
	COUNTER_MIN_VAL = 0 
	assert_rst = 0
	deassert_rst = 1
	expected_count = 0Xffff
	rst_counter_rand = random.randint(0, num_cycles*test_cases)
	
	dut.reset.value = assert_rst
	await ClockCycles(dut.clock1, 2)
	
	await RisingEdge(dut.clock1)
	dut.reset.value = deassert_rst
	
	await FallingEdge(dut.clock1)
	dut._log.info("Reset Test0:: count1 is %d", dut.cnt1_16.value)
	dut._log.info("Reset Test0:: expected_count1 is %d", expected_count)
	assert dut.cnt1_16.value == expected_count, "count1 does not match expected value!"

	await ClockCycles(dut.clock1, 20)
	await RisingEdge(dut.clock1)
	dut.reset.value = assert_rst
	await FallingEdge(dut.clock1)
	dut._log.info("Reset Test1:: count1 is %d", dut.cnt1_16.value)
	dut._log.info("Reset Test1:: expected_count1 is %d", expected_count)
	assert dut.cnt1_16.value == expected_count, "count1 does not match expected value!"
	await RisingEdge(dut.clock1)
	dut.reset.value = deassert_rst
	await FallingEdge(dut.clock1)
	
	for cycle in range(num_cycles*test_cases):
		if cycle == rst_counter_rand:
			dut.reset.value = assert_rst
			dut._log.info("Reset Test2:: Driving reset randomly!")
		else:
			dut.reset.value = deassert_rst
			
		await RisingEdge(dut.clock1)
		if expected_count == COUNTER_MIN_VAL or dut.reset.value == assert_rst:
			expected_count = 0Xffff
		else:
			expected_count -= 1
			
		await FallingEdge(dut.clock1)
		dut._log.info("count1 is %d", dut.cnt1_16.value)
		dut._log.info("expected_count1 is %d", expected_count)
		assert dut.cnt1_16.value == expected_count, "count1 does not match expected value!"

  ################################################################
	
	# Counter2 test
	################################################################
	
	test_cases = 2
	COUNTER_SIZE = 16
	num_cycles = pow(2, COUNTER_SIZE)
	COUNTER_MIN_VAL = 0 
	assert_rst = 0
	deassert_rst = 1
	expected_count = 0Xffff
	rst_counter_rand = random.randint(0, num_cycles*test_cases)
	
	dut.reset.value = assert_rst
	await ClockCycles(dut.clock2, 2)
	
	await RisingEdge(dut.clock2)
	dut.reset.value = deassert_rst
	
	await FallingEdge(dut.clock2)
	dut._log.info("Reset Test0:: count2 is %d", dut.cnt2_16.value)
	dut._log.info("Reset Test0:: expected_count2 is %d", expected_count)
	assert dut.cnt2_16.value == expected_count, "count2 does not match expected value!"

	await ClockCycles(dut.clock2, 20)
	await RisingEdge(dut.clock2)
	dut.reset.value = assert_rst
	await FallingEdge(dut.clock2)
	dut._log.info("Reset Test1:: count2 is %d", dut.cnt2_16.value)
	dut._log.info("Reset Test1:: expected_count2 is %d", expected_count)
	assert dut.cnt2_16.value == expected_count, "count2 does not match expected value!"
	await RisingEdge(dut.clock2)
	dut.reset.value = deassert_rst
	await FallingEdge(dut.clock2)
	
	for cycle in range(num_cycles*test_cases):
		if cycle == rst_counter_rand:
			dut.reset.value = assert_rst
			dut._log.info("Reset Test2:: Driving reset randomly!")
		else:
			dut.reset.value = deassert_rst
			
		await RisingEdge(dut.clock2)
		if expected_count == COUNTER_MIN_VAL or dut.reset.value == assert_rst:
			expected_count = 0Xffff
		else:
			expected_count -= 1
			
		await FallingEdge(dut.clock2)
		dut._log.info("count2 is %d", dut.cnt2_16.value)
		dut._log.info("expected_count2 is %d", expected_count)
		assert dut.cnt2_16.value == expected_count, "count2 does not match expected value!"

  ################################################################
	
	# Counter3 test
	################################################################
	
	test_cases = 2
	COUNTER_SIZE = 16
	num_cycles = pow(2, COUNTER_SIZE)
	COUNTER_MIN_VAL = 0 
	assert_rst = 0
	deassert_rst = 1
	expected_count = 0Xffff
	rst_counter_rand = random.randint(0, num_cycles*test_cases)
	
	dut.reset.value = assert_rst
	await ClockCycles(dut.clock3, 2)
	
	await RisingEdge(dut.clock3)
	dut.reset.value = deassert_rst
	
	await FallingEdge(dut.clock3)
	dut._log.info("Reset Test0:: count3 is %d", dut.cnt3_16.value)
	dut._log.info("Reset Test0:: expected_count3 is %d", expected_count)
	assert dut.cnt3_16.value == expected_count, "count3 does not match expected value!"

	await ClockCycles(dut.clock3, 20)
	await RisingEdge(dut.clock3)
	dut.reset.value = assert_rst
	await FallingEdge(dut.clock3)
	dut._log.info("Reset Test1:: count3 is %d", dut.cnt3_16.value)
	dut._log.info("Reset Test1:: expected_count3 is %d", expected_count)
	assert dut.cnt3_16.value == expected_count, "count3 does not match expected value!"
	await RisingEdge(dut.clock3)
	dut.reset.value = deassert_rst
	await FallingEdge(dut.clock3)
	
	for cycle in range(num_cycles*test_cases):
		if cycle == rst_counter_rand:
			dut.reset.value = assert_rst
			dut._log.info("Reset Test2:: Driving reset randomly!")
		else:
			dut.reset.value = deassert_rst
			
		await RisingEdge(dut.clock3)
		if expected_count == COUNTER_MIN_VAL or dut.reset.value == assert_rst:
			expected_count = 0Xffff
		else:
			expected_count -= 1
			
		await FallingEdge(dut.clock3)
		dut._log.info("count3 is %d", dut.cnt3_16.value)
		dut._log.info("expected_count3 is %d", expected_count)
		assert dut.cnt3_16.value == expected_count, "count3 does not match expected value!"
