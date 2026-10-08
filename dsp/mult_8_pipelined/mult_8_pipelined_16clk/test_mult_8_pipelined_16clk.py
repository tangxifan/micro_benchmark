import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_mult_8_16clk_pipelined(dut):
    """Verify 16-clock 8-bit pipelined multiplier functionality and 2-stage latency across concurrent domains."""

    num_clocks = 16

    # Define unique integer clock periods for all 16 independent domains to avoid float precision errors
    clock_periods = [10 + i for i in range(num_clocks)]
    for i, period in enumerate(clock_periods):
        clk_handle = getattr(dut, f"clk{i}")
        cocotb.start_soon(Clock(clk_handle, period, unit="ns").start())

    # Initialize inputs for all 16 channels
    for i in range(num_clocks):
        getattr(dut, f"a{i}").value = 0
        getattr(dut, f"b{i}").value = 0
    
    await Timer(20, unit="ns")

    # Define test vectors
    test_vectors = [(12, 5), (255, 255), (0, 100), (15, 15), (128, 2)]

    async def verify_channel(i, period):
        clk_handle = getattr(dut, f"clk{i}")
        a_handle = getattr(dut, f"a{i}")
        b_handle = getattr(dut, f"b{i}")
        p_handle = getattr(dut, f"p{i}")

        pipeline_queue = []

        for a_val, b_val in test_vectors:
            # Drive inputs
            a_handle.value = a_val
            b_handle.value = b_val
            expected_p = a_val * b_val
            pipeline_queue.append(expected_p)

            await RisingEdge(clk_handle)
            await Timer(1, unit="ns")

            # Check pipeline output after 2 clock cycles of latency
            if len(pipeline_queue) >= 2:
                expected_output = pipeline_queue.pop(0)
                actual_output = int(p_handle.value)
                dut._log.info(
                    f"Channel {i} - Checking output: Expected={expected_output}, Got={actual_output}"
                )
                assert (
                    actual_output == expected_output
                ), f"Channel {i} Mismatch: expected {expected_output}, got {actual_output}"

        # Flush remaining pipeline stages
        while len(pipeline_queue) > 0:
            await RisingEdge(clk_handle)
            await Timer(1, unit="ns")
            expected_output = pipeline_queue.pop(0)
            actual_output = int(p_handle.value)
            assert (
                actual_output == expected_output
            ), f"Channel {i} Mismatch during pipeline flush: expected {expected_output}, got {actual_output}"

    # Launch verification routines concurrently for all 16 channels
    tasks = [cocotb.start_soon(verify_channel(i, p)) for i, p in enumerate(clock_periods)]
    for task in tasks:
        await task

    dut._log.info("16-clock pipelined multiplier test completed successfully!")
