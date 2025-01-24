#####################################################################
# Test LUTs and FFs: test_fsm_seq_detector
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_fsm_seq_detector(dut):
    # Initialize
    dut.seq_in.value = 0
    dut.reset.value = 0
    SEQ_STR = "10011001"
    dut.expected_seq.value = BinaryValue(SEQ_STR, n_bits=8, bigEndian=False)
    # Clock Generation
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clock0, CLK_PERIOD, units="ns").start())

    # apply reset
    await ClockCycles(dut.clock0, 1)
    dut._log.info("======== reset assertion to reset FSM ========")
    dut.reset.value = 1
    await ClockCycles(dut.clock0, 2)
    await FallingEdge(dut.clock0)
    dut._log.info("======== reset de-assertion to start FSM ========")
    dut.reset.value = 0

    # Test 1
    for seq_item in range(8):
        dut._log.info("======== Sequence item# %d ========", seq_item)
        # sending each sequence item
        dut.seq_in.value = BinaryValue(SEQ_STR[7 - seq_item]).integer
        await FallingEdge(dut.clock0)
    assert dut.seq_detected.value == 1, "Sequence is not detected"
    dut._log.info("======== Sequence %s detected successfully ========", SEQ_STR)

    SEQ_STR = "10101101"
    dut.expected_seq.value = BinaryValue(SEQ_STR, n_bits=8, bigEndian=False)

    # apply reset
    await ClockCycles(dut.clock0, 1)
    dut._log.info("======== reset assertion to reset FSM ========")
    dut.reset.value = 1
    await ClockCycles(dut.clock0, 2)
    await FallingEdge(dut.clock0)
    dut._log.info("======== reset de-assertion to start FSM ========")
    dut.reset.value = 0

    # Test 2
    for seq_item in range(8):
        dut._log.info("======== Sequence item# %d ========", seq_item)
        # sending each sequence item
        dut.seq_in.value = BinaryValue(SEQ_STR[7 - seq_item]).integer
        await FallingEdge(dut.clock0)
    assert dut.seq_detected.value == 1, "Sequence is not detected"
    dut._log.info("======== Sequence %s detected successfully ========", SEQ_STR)
