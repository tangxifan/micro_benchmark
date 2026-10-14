import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_configuration_manager(dut):
    # Create a 50MHz clock (20ns period) on clk_in
    clock = Clock(dut.clk_in, 20, unit="ns")
    cocotb.start_soon(clock.start())

    dut._log.info("Starting Configuration Manager Testbench...")

    # Wait for a couple of clock edges to let signals initialize out of 'X'
    await RisingEdge(dut.clk_in)
    await RisingEdge(dut.clk_in)

    cycles_waited = 0
    # Increased max_cycles to account for the 4096x clock division and 6140 bitstream size
    max_cycles = 35_000_000  

    # Safely poll configuration_done by handling potential 'X' or 'Z' values during startup
    while True:
        val = dut.configuration_done.value
        if val.is_resolvable and int(val) == 1:
            break
        
        await RisingEdge(dut.clk_in)
        cycles_waited += 1
        
        if cycles_waited > max_cycles:
            raise AssertionError("Timeout waiting for configuration_done to assert!")

    dut._log.info(f"Configuration successfully completed in {cycles_waited} clk_in cycles!")

    # Observe state after completion
    assert int(dut.configuration_done.value) == 1, "Configuration done signal should be high"
    
    # Wait a few more cycles to ensure stability
    for _ in range(10):
        await RisingEdge(dut.clk_in)

    dut._log.info("Test passed successfully!")
