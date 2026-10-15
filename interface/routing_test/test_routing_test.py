import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_routing_test_functional(dut):
    """Testbench for routing_test module verifying synchronous signal routing."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize input signals to 0
    dut.IN0.value = 0
    dut.IN1.value = 0
    dut.IN2.value = 0

    # Wait for a couple of cycles after startup
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Define test vectors: (IN0, IN1, IN2)
    test_vectors = [(1, 0, 1), (0, 1, 1), (1, 1, 0), (0, 0, 0), (1, 1, 1)]

    cocotb.log.info("Starting sequential routing tests...")

    for in0, in1, in2 in test_vectors:
        # Drive inputs
        dut.IN0.value = in0
        dut.IN1.value = in1
        dut.IN2.value = in2

        # Wait for the positive clock edge where inputs are registered
        await RisingEdge(dut.clk)

        # Allow a tiny delta for non-blocking assignments to settle
        await Timer(1, unit="ns")

        # Verify outputs match the driven inputs from the previous cycle
        assert (
            int(dut.OUT0.value) == in0
        ), f"OUT0 mismatch: expected {in0}, got {int(dut.OUT0.value)}"
        assert (
            int(dut.OUT1.value) == in1
        ), f"OUT1 mismatch: expected {in1}, got {int(dut.OUT1.value)}"
        assert (
            int(dut.OUT2.value) == in2
        ), f"OUT2 mismatch: expected {in2}, got {int(dut.OUT2.value)}"

        cocotb.log.info(
            f"Verified vector IN=({in0},{in1},{in2}) -> OUT=({int(dut.OUT0.value)},{int(dut.OUT1.value)},{int(dut.OUT2.value)})"
        )

    cocotb.log.info("All routing test cases passed successfully!")
