
#####################################################################
# Test the functionality of clk_divider
#####################################################################
import random
import numpy as np
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge
from cocotb.triggers import ReadOnly
from cocotb.result import TestFailure


async def monitor_pwm(dut):
    period = 100
    duty_cycle = 80
    high_time = period * duty_cycle / 100
    low_time = period - high_time
    high_count = 0
    low_count = 0
    i=0
    #await FallingEdge(dut.reset)
    
    while(i<1000):      
        await RisingEdge(dut.clk)
        if dut.pwm.value.integer == 1:
            high_count += 1
            if high_count > high_time:
                raise TestFailure("PWM high time exceeded")
        else:
            low_count += 1
            if low_count > low_time:
                raise TestFailure("PWM low time exceeded")
        if high_count + low_count >= period:
            high_count = 0
            low_count = 0
        #print("High count low count",high_count,low_count)
        i=i+1

@cocotb.test()
async def pwm_test_generator(dut):
    # Create a clock and start it running
    CLK0_PERIOD = 10 # [ns]
    #dut.clk.value <= 0
    cocotb.start_soon(Clock(dut.clk, CLK0_PERIOD, units="ns").start())
    await RisingEdge(dut.clk)

    # Reset the design
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0
    await RisingEdge(dut.clk)

    # Monitor the PWM output
    pwm_coroutine = monitor_pwm(dut)
    monitor_thread = cocotb.start_soon(pwm_coroutine)

    # Run the test for 100 clock cycles
    for i in range(100):
        await RisingEdge(dut.clk)

    # Stop the clock
    #clk.stop()
    await monitor_thread

