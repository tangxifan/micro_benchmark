#####################################################################
# Test counters
#####################################################################
import random
import array
import cocotb
import numpy as np
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_counterup36_8_2clk_async_resetp(dut):
    ## Create clocks
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clock0, CLK_PERIOD, units="ns").start())
    # cocotb.start_soon(Clock(dut.clock1, CLK_PERIOD, units="ns").start())

    test_cases = 1
    COUNTER_SIZE = 8
    num_cycles = pow(2, COUNTER_SIZE)
    COUNTER_MAX_VAL1 = num_cycles - 1

    COUNTER_SIZE2 = 12
    num_cycles2 = pow(2, COUNTER_SIZE2)
    COUNTER_MAX_VAL2 = num_cycles2 - 1

    COUNTER_SIZE3 = 16
    num_cycles3 = pow(2, COUNTER_SIZE3)
    COUNTER_MAX_VAL3 = num_cycles3 - 1

    COUNTER_SIZE4 = 10
    num_cycles4 = pow(2, COUNTER_SIZE4)
    COUNTER_MAX_VAL4 = num_cycles4 - 1

    c1 = COUNTER_SIZE + COUNTER_SIZE2 + COUNTER_SIZE3
    dut.reset.value = 1

    expected_count = 0
    expected_count1 = 0
    expected_count2 = 0
    expected_count3 = 0

    divider = COUNTER_SIZE3 * COUNTER_SIZE2

    rst_counter_rand = random.randint(10, 30)  ## quick reset to reduce simulation time
    rst_counter_rand1 = random.randint(20, 40)

    await ClockCycles(dut.clock0, 50)

    assert dut.out2.value == 0, "10 bit counter in top module does not matched"
    await Timer(1, units="ns")
    dut.reset.value = 0
    await FallingEdge(dut.clock0)
    ########################################################################################
    for cycle in range(
        int((num_cycles * test_cases) / COUNTER_SIZE3 * COUNTER_SIZE4 * COUNTER_SIZE)
    ):  # testing counter 10 bit

        if cycle == rst_counter_rand1:
            await RisingEdge(dut.clock0)
            dut.reset.value = 1
            await Timer(5, units="ns")
            dut._log.info("Reset Test2:: Driving reset randomly!")
        else:
            dut.reset.value = 0
            # dut._log.info("Reset VALUE is", dut.reset.value)

        await Timer(5, units="ns")

        ## for 10 bit
        if expected_count3 == COUNTER_MAX_VAL4 or dut.reset.value == 1:
            expected_count3 = 0
        else:
            expected_count3 += 1

        await Timer(5, units="ns")
        dut._log.info("Testing counter10 %d", expected_count3)
        assert dut.out2.value == expected_count3, "counter 10 bit does not match expected value!"
    ###########################################################################################################

    for cycle in range(
        int((num_cycles3 * test_cases) / divider)
    ):  # Divided by COUNTER_SIZE just to reduce runtime

        if cycle == rst_counter_rand:
            await RisingEdge(dut.clock0)
            dut.reset.value = 1
            await Timer(5, units="ns")
            dut._log.info("Reset Test2:: Driving reset randomly!")
        else:
            dut.reset.value = 0
        await Timer(5, units="ns")

        ## for 8 bit
        if expected_count == COUNTER_MAX_VAL1 or dut.reset.value == 1:
            expected_count = 0
        else:
            expected_count += 1

        await Timer(5, units="ns")

        ###  for 12 bit
        if expected_count1 == COUNTER_MAX_VAL2 or dut.reset.value == 1:
            expected_count1 = 0
        else:
            expected_count1 += 1

        await FallingEdge(dut.clock0)

        ### for 16 bit
        if expected_count2 == COUNTER_MAX_VAL3 or dut.reset.value == 1:
            expected_count2 = 0
        else:
            expected_count2 += 1

        expected_out_str0 = BinaryValue(expected_count, n_bits=8, bigEndian=False).binstr
        expected_out_str1 = BinaryValue(expected_count1, n_bits=12, bigEndian=False).binstr
        expected_out_str2 = BinaryValue(expected_count2, n_bits=16, bigEndian=False).binstr

        dut._log.info("expected value of counter 8 in binary %s", expected_out_str0)
        dut._log.info("expected value of counter12 in binary %s", expected_out_str1)
        dut._log.info("expected value of counter16 in binary %s", expected_out_str2)

        counter16_str = BinaryValue(dut.out1.value.value, n_bits=2772, bigEndian=False).binstr

    ins = 76

    for cycle in range(ins):

        assert (
            counter16_str[(ins * 36) : ((ins * 36) + 16)] == expected_out_str2
        ), "counter 16 bit does not match expected value!"
        assert (
            counter16_str[((ins * 36) + 16) : ((ins * 36) + 28)] == expected_out_str1
        ), "counter 12 bit does not match expected value!"
        assert (
            counter16_str[((ins * 36) + 28) : ((ins * 36) + 36)] == expected_out_str0
        ), "counter 8 bit does not match expected value!"
