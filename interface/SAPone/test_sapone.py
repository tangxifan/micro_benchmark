import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_sapone_functional(dut):
    """Testbench for SAPone processor verifying reset behavior and initial execution cycles."""
    
    # Start a 10ns period clock (100 MHz, matching #5 clk = ~clk half-period)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize control signals: assert active-low clear (clr_ = 0)
    dut.clr_.value = 0
    
    # Wait for 10ns (equivalent to #10 in Verilog testbench)
    await Timer(10, units="ns")
    
    # Deassert clear (clr_ = 1) to start processor execution
    dut.clr_.value = 1
    cocotb.log.info("SAPone reset released, starting execution...")

    # Run for 990ns (matching #990 $stop simulation window)
    await Timer(990, units="ns")
    
    # Safely retrieve string values to avoid ValueError on 'X' or 'Z' bus states
    sap_out_val = str(dut.SAP_out.value)
    bus_val = str(dut.bus.value)
    con_val = str(dut.con.value)
    
    cocotb.log.info(f"Simulation completed.")
    cocotb.log.info(f"Final SAP_out: {sap_out_val}")
    cocotb.log.info(f"Final bus:     {bus_val}")
    cocotb.log.info(f"Final con:     {con_val}")
