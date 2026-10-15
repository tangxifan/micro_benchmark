import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge


@cocotb.test()
async def test_risc_posedge_clk(dut):
    # Create a clock with a 40ns period (matching the 20ns half-period toggle in original testbench)
    clock = Clock(dut.clk, 40, unit="ns")
    cocotb.start_soon(clock.start())

    dut._log.info("Starting RISC Core Testbench...")

    # Initialize signals
    dut.clk.value = 0
    dut.rst.value = 1

    # Wait 30ns under reset
    await Timer(30, unit="ns")

    # Deassert reset
    dut.rst.value = 0
    dut._log.info("Reset deasserted. Running simulation...")

    # Run for 6000ns matching the original $stop duration
    await Timer(6000, unit="ns")

    dut._log.info("RISC simulation completed successfully!")
