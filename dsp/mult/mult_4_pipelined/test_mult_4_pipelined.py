import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_mult_4_pipelined(dut):
    """Testbench verifying 4-bit pipelined multiplier with 2-stage latency."""

    # Start a 100 MHz clock (10 ns period)[cite: 10]
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting mult_4_pipelined simulation...")

    # Force initial register states to prevent 'X' propagation since no reset pin exists[cite: 10]
    dut.a.value = 0
    dut.b.value = 0
    dut.a_reg.value = 0
    dut.b_reg.value = 0
    dut.out_reg.value = 0

    await Timer(1, unit="ns")
    await RisingEdge(dut.clk)

    # Test vectors: list of (a, b) tuples for 4-bit operands (0 to 15)[cite: 10]
    test_vectors = [
        (3, 5),  # 3 * 5 = 15
        (12, 10),  # 12 * 10 = 120
        (15, 15),  # 15 * 15 = 225
        (0, 9),  # 0 * 9 = 0
        (7, 8),  # 7 * 8 = 56
    ]

    # Queue to track expected results across the 2-cycle pipeline depth[cite: 10]
    pipeline_queue = []

    for val_a, val_b in test_vectors:
        # Drive inputs on current clock cycle
        dut.a.value = val_a
        dut.b.value = val_b

        expected_product = val_a * val_b
        pipeline_queue.append((val_a, val_b, expected_product))

        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        # After 2 clock cycles, the first result reaches the output stage[cite: 10]
        if len(pipeline_queue) >= 2:
            check_a, check_b, expected = pipeline_queue.pop(0)
            actual = int(dut.out.value)
            cocotb.log.info(
                f"[Pipeline Output] {check_a} * {check_b} = {actual} (Expected: {expected})"
            )
            assert (
                actual == expected
            ), f"Pipeline mismatch for {check_a} * {check_b}! Expected {expected}, got {actual}"

    # Drain remaining items in the pipeline queue
    while pipeline_queue:
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        check_a, check_b, expected = pipeline_queue.pop(0)
        actual = int(dut.out.value)
        cocotb.log.info(
            f"[Pipeline Drain]  {check_a} * {check_b} = {actual} (Expected: {expected})"
        )
        assert (
            actual == expected
        ), f"Pipeline drain mismatch for {check_a} * {check_b}! Expected {expected}, got {actual}"

    cocotb.log.info("mult_4_pipelined simulation completed successfully!")
