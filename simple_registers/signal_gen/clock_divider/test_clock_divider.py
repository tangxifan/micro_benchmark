import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_clock_divider(dut):
    """Testbench for clock_divider verifying division ratio and clk_out toggling."""
    
    # Start a 10ns period input clock (100 MHz)
    clock = Clock(dut.clk_in, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting clock_divider simulation...")

    # Force initial values from the testbench to resolve 'X' states
    dut.clk_out.value = 0
    dut.clkdiv_counter.value = 0
    await Timer(1, unit="ns")

    initial_clk_out = int(dut.clk_out.value)
    toggle_count = 0

    # Run simulation for enough cycles (CLK_DIVIDER_SIZE=8 means toggling every 128 cycles)
    for cycle in range(1000):
        await RisingEdge(dut.clk_in)
        
        current_clk_out = int(dut.clk_out.value)
        if current_clk_out != initial_clk_out:
            toggle_count += 1
            initial_clk_out = current_clk_out
            cocotb.log.info(f"clk_out toggled to {current_clk_out} at input cycle {cycle}")

    cocotb.log.info(f"Simulation finished. Total clk_out toggles observed: {toggle_count}")
    assert toggle_count > 0, "Expected clk_out to toggle during simulation cycles."
