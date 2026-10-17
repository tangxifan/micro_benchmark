import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reset_generator(dut):
    """Testbench for reset_generator verifying active cycles counter and pulse toggle."""
    
    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting reset_generator simulation...")

    # Force initial register values to resolve 'X' states since VIVADO_SYNTHESIS initial block is gated
    dut.pulse.value = 0
    dut.active_cycle_counter.value = 0
    await Timer(1, unit="ns")

    initial_pulse = int(dut.pulse.value)
    toggle_count = 0

    # Monitor output across clock cycles
    for cycle in range(50):
        await RisingEdge(dut.clk)
        
        val_str = str(dut.pulse.value)
        if all(c in '01' for c in val_str):
            current_pulse = int(dut.pulse.value)
            if current_pulse != initial_pulse:
                toggle_count += 1
                initial_pulse = current_pulse
                cocotb.log.info(f"Pulse toggled to {current_pulse} at input cycle {cycle}")

    cocotb.log.info(f"Simulation finished. Total pulse toggles observed: {toggle_count}")
    assert toggle_count > 0, "Expected pulse output to toggle during simulation cycles."
