#####################################################################
# Test DSP LUTs and FFs: Transposed Tap4 Unsigned FIR Test
#####################################################################
import random
import cocotb
from cocotb.types import LogicArray
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

SEQ_STR = "10110010"
SEQ_BITS = 8


@cocotb.test()
async def test_scalable_seq_detector(dut):
    # Initialize
    dut.x.value = 0
    dut.reset.value = 0
    dut.sequence_str.value = LogicArray(SEQ_STR, SEQ_BITS)
    # Clock Generation
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clock0, CLK_PERIOD, "ns").start())
    # apply reset
    await ClockCycles(dut.clock0, 3)
    dut.reset.value = 1
    await ClockCycles(dut.clock0, 2)
    await FallingEdge(dut.clock0)
    dut.reset.value = 0

    # Test
    for seq_item in range(8):
        dut._log.info("======== BEGIN Sequence item: %d ========", seq_item)
        # sending each sequence item
        dut.x.value = LogicArray(SEQ_STR[SEQ_BITS - 1 - seq_item]).to_unsigned()
        if seq_item == 0:
            expected_start = 1
            expected_stop = 0
            expected_mid = 0
            expected_1sth = 1
            expected_2ndh = 0
        elif seq_item == 7:
            expected_start = 0
            expected_stop = 1
            expected_mid = 0
            expected_1sth = 0
            expected_2ndh = 1
        elif seq_item == 4:
            expected_start = 0
            expected_stop = 0
            expected_mid = 1
            expected_1sth = 0
            expected_2ndh = 0
        elif seq_item < 4:
            expected_start = 0
            expected_stop = 0
            expected_mid = 0
            expected_1sth = 1
            expected_2ndh = 0
        else:
            expected_start = 0
            expected_stop = 0
            expected_mid = 0
            expected_1sth = 0
            expected_2ndh = 1

        assert dut.start.value == expected_start, "out start does not match expected value!"
        assert dut.stop.value == expected_stop, "out stop does not match expected value!"
        assert dut.mid.value == expected_mid, "out mid does not match expected value!"
        assert (
            dut.first_half.value == expected_1sth
        ), "out first_half does not match expected value!"
        assert (
            dut.second_half.value == expected_2ndh
        ), "out second_half does not match expected value!"
        await FallingEdge(dut.clock0)
        dut._log.info("======== END Sequence item: %d ========", seq_item)
