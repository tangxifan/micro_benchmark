import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_mult_8_pipelined(dut):
    """Verify 8-bit pipelined multiplier functionality and 2-stage latency."""

    # Start a 10ns clock (100 MHz)
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Initialize inputs
    dut.a.value = 0
    dut.b.value = 0
    await Timer(20, unit="ns")

    # Define test vectors
    test_vectors = [(12, 5), (255, 255), (0, 100), (15, 15), (128, 2)]

    # Queue to track expected results across the 2-cycle pipeline
    pipeline_queue = []

    for a_val, b_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        expected_p = a_val * b_val
        pipeline_queue.append(expected_p)

        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        # Check pipeline output after 2 clock cycles of latency
        if len(pipeline_queue) >= 2:
            expected_output = pipeline_queue.pop(0)
            actual_output = int(dut.p.value)
            dut._log.info(
                f"Checking output: Expected={expected_output}, Got={actual_output}"
            )
            assert (
                actual_output == expected_output
            ), f"Mismatch: expected {expected_output}, got {actual_output}"

    # Flush remaining pipeline stages
    while len(pipeline_queue) > 0:
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        expected_output = pipeline_queue.pop(0)
        actual_output = int(dut.p.value)
        assert (
            actual_output == expected_output
        ), f"Mismatch during pipeline flush: expected {expected_output}, got {actual_output}"

    dut._log.info("Pipelined multiplier test completed successfully!")
