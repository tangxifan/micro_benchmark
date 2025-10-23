#####################################################################
# Test a Falling-edge D-type flip-flop with active-high async reset
#####################################################################
import random
import cocotb
from cocotb.types import LogicArray
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

# Constants
CLEAR_ENABLE = 1
CLEAR_DISABLE = 0

################################################################
# Configure the dut with a given mode bit
# See truth table in documentation as a reference
# async def config_mode(dut, mode_bits):
#  dut.mode_i.value = LogicArray(mode_bits).to_unsigned()


@cocotb.test()
async def test_dffnr(dut):
    # Initialize
    # Disable scan mode
    # dut.test_en_i.value = 0
    # dut.di_i.value = 0
    # Disable clear signal which is configured to be active-high
    dut.clr_i.value = CLEAR_ENABLE

    ################################################################
    # Configure the flip-flop as a simple d-type flip-flop
    # See truth table in documentation as a reference
    # cocotb.start_soon(config_mode(dut, "1010"))

    ################################################################
    # Create clocks
    CLK_PERIOD = 10  # [ns]
    cocotb.start_soon(Clock(dut.clk_i, CLK_PERIOD, "ns").start())

    # Just wait a very short period, apply reset
    await Timer(CLK_PERIOD / 10)
    dut.clr_i.value = CLEAR_ENABLE
    dut.d_i.value = 1
    # check output
    expected_q_o = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test async reset under d='1' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"

    # Still under reset, check if D is not impacting output
    await Timer(CLK_PERIOD / 10)
    dut.clr_i.value = CLEAR_ENABLE
    dut.d_i.value = 0
    # check output
    expected_q_o = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test async reset under d='0' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"

    # Disable clear signal now
    await Timer(CLK_PERIOD / 10)
    dut.clr_i.value = CLEAR_DISABLE
    dut.d_i.value = 0

    # Test if d can be output as 0 or 1
    dut._log.info("======== Test D-to-Q on logic '1' ========")
    await RisingEdge(dut.clk_i)
    dut.d_i.value = 1
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 1
    dut.d_i.value = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test D-to-Q on logic '0' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 0
    dut.d_i.value = 1
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test D-to-Q on logic '1' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 1
    dut.d_i.value = 1
    dut._log.info("expected_q_o is %d", expected_q_o)
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"

    # Just wait a very short period, apply reset
    await Timer(CLK_PERIOD / 10)
    dut.clr_i.value = CLEAR_ENABLE
    dut.d_i.value = 1
    await Timer(CLK_PERIOD / 10)
    # check output
    expected_q_o = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test async reset under d='1' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"

    # Still under reset, check if D is not impacting output
    await Timer(CLK_PERIOD / 10)
    dut.clr_i.value = CLEAR_ENABLE
    dut.d_i.value = 0
    # check output
    expected_q_o = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test async reset under d='0' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"

    # Check the impact of clock on q_o when reset is enabled
    # Test if d can be output as 0 or 1
    dut._log.info("======== Test D-to-Q on logic '1' ========")
    await RisingEdge(dut.clk_i)
    dut.d_i.value = 1
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 0
    dut.d_i.value = 0
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test D-to-Q on logic '0' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 0
    dut.d_i.value = 1
    dut._log.info("expected_q_o is %d", expected_q_o)
    dut._log.info("======== Test D-to-Q on logic '1' ========")
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"
    await RisingEdge(dut.clk_i)
    # Check output
    dut._log.info("q_o is %d", dut.q_o.value)
    # Calculate expected values of output
    expected_q_o = 0
    dut.d_i.value = 1
    dut._log.info("expected_q_o is %d", expected_q_o)
    assert dut.q_o.value == expected_q_o, "q_o does not match expected value!"
