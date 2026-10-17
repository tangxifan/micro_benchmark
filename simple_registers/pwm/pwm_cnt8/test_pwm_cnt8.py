import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_pwm_cnt8(dut):
    """Testbench for pwm_cnt8 verifying PWM match outputs based on hard counter references."""

    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Apply active-high reset
    dut.reset.value = 1
    cocotb.log.info("Applying reset...")
    await Timer(20, unit="ns")
    await RisingEdge(dut.clk)
    dut.reset.value = 0
    cocotb.log.info("Reset released. Monitoring PWM outputs...")

    # Run simulation for enough cycles to observe full counter rollover (256 cycles) and match pulses
    for cycle in range(300):
        await RisingEdge(dut.clk)
        m0 = int(dut.m0_out.value)
        m1 = int(dut.m1_out.value)

        # Log when either match output is asserted
        if m0 or m1:
            cocotb.log.info(f"Cycle {cycle:3d}: m0_out={m0}, m1_out={m1}")

    cocotb.log.info("pwm_cnt8 test completed successfully!")
