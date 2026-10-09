
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_blinking_toggle(dut):
    """Verify that out toggles on every rising edge of clk."""

    # Initialize the clock and seed the uninitialized output.
    # This is a simulation-only initialization.
    dut.clk.value = 0
    dut.out.value = 0
    expected = 0

    await Timer(2, unit="ns")

    for cycle in range(20):
        # Output should be stable before the rising edge.
        assert int(dut.out.value) == expected, (
            f"Cycle {cycle}: output changed unexpectedly before rising edge"
        )

        # Rising edge: output must toggle.
        dut.clk.value = 1
        await Timer(2, unit="ns")

        expected ^= 1

        assert int(dut.out.value) == expected, (
            f"Cycle {cycle}: expected out={expected}, "
            f"got out={dut.out.value}"
        )

        # Falling edge: output must remain unchanged.
        dut.clk.value = 0
        await Timer(2, unit="ns")

        assert int(dut.out.value) == expected, (
            f"Cycle {cycle}: output changed on falling edge"
        )

    dut._log.info("PASS: out toggled correctly for 20 clock cycles")

