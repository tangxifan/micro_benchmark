import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_configuration_manager(dut):
    # Create a 50MHz clock (20ns period) on clk_in
    clock = Clock(dut.clk_in, 20, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize signals
    dut._log.info("Starting Configuration Manager Testbench...")

    # Wait for reset release and configuration sequence to complete
    # Since CONFIGURATION_CLK_DIV_SIZE is 12 (divide by 4096), 
    # full configuration takes some time. We can set a timeout or monitor signals.
    
    cycles_waited = 0
    max_cycles = 500000  # Adjust based on BITSTREAM_SIZE and divider

    while not dut.configuration_done.value:
        await RisingEdge(dut.clk_in)
        cycles_waited += 1
        if cycles_waited > max_cycles:
            raise TestFailure("Timeout waiting for configuration_done to assert!")

    dut._log.info(f"Configuration successfully completed in {cycles_waited} clk_in cycles!")

    # Observe state after completion
    assert dut.configuration_done.value == 1, "Configuration done signal should be high"
    
    # Wait a few more cycles to ensure stability
    for _ in range(10):
        await RisingEdge(dut.clk_in)

    dut._log.info("Test passed successfully!")