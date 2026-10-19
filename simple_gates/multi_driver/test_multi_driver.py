import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_multi_driver(dut):
    """Testbench verifying multi_driver pipelined addition and active-low async reset."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting multi_driver simulation...")

    # 1. Test Active-Low Asynchronous Reset
    dut.rst_n.value = 0
    dut.ina1.value = 1
    dut.ina2.value = 1
    dut.inb1.value = 1
    dut.inb2.value = 1

    await Timer(3, unit="ns")
    assert int(dut.outa.value) == 0, f"Reset failed for outa! Expected 0, got {int(dut.outa.value)}"
    assert (
        int(dut.outb1.value) == 0
    ), f"Reset failed for outb1! Expected 0, got {int(dut.outb1.value)}"
    assert (
        int(dut.outb2.value) == 0
    ), f"Reset failed for outb2! Expected 0, got {int(dut.outb2.value)}"
    cocotb.log.info("Asynchronous reset verified successfully.")

    # Release reset
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # Test vectors: (ina1, ina2, inb1, inb2)
    test_vectors = [
        (0, 0, 0, 0),
        (1, 0, 0, 1),
        (0, 1, 1, 0),
        (1, 1, 1, 1),
        (1, 0, 1, 1),
    ]

    # Queue to track expected results across the 2-cycle pipeline depth
    pipeline_queue = []

    for v1, v2, v3, v4 in test_vectors:
        dut.ina1.value = v1
        dut.ina2.value = v2
        dut.inb1.value = v3
        dut.inb2.value = v4

        # Model pipeline registers (Stage 1)
        expected_outa = v1 + v2
        expected_outb = v3 + v4
        pipeline_queue.append((expected_outa, expected_outb))

        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

    # Wait for the remaining pipeline stages to flush out
    for _ in range(2):
        pipeline_queue.append((0, 0))
        dut.ina1.value = 0
        dut.ina2.value = 0
        dut.inb1.value = 0
        dut.inb2.value = 0
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

    # Verify outputs through the pipeline queue
    # Note: Due to 2-cycle latency, outputs align after 2 clock edges
    # Let's run a direct checked loop for clarity:

    cocotb.log.info("Running direct stimulus-response pipeline checks...")

    stimuli = [
        (1, 0, 0, 1),  # expected outa = 1, outb = 1
        (1, 1, 1, 0),  # expected outa = 2, outb = 1
        (0, 0, 1, 1),  # expected outa = 0, outb = 2
    ]

    for ina1_v, ina2_v, inb1_v, inb2_v in stimuli:
        dut.ina1.value = ina1_v
        dut.ina2.value = ina2_v
        dut.inb1.value = inb1_v
        dut.inb2.value = inb2_v

        await RisingEdge(dut.clk)
        await RisingEdge(dut.clk)  # 2-cycle pipeline latency
        await Timer(1, unit="ns")

        exp_a = ina1_v + ina2_v
        exp_b = inb1_v + inb2_v

        act_a = int(dut.outa.value)
        act_b1 = int(dut.outb1.value)
        act_b2 = int(dut.outb2.value)

        cocotb.log.info(
            f"Checked: outa={act_a} (exp {exp_a}), outb1={act_b1}, outb2={act_b2} (exp {exp_b})"
        )
        assert act_a == exp_a, f"outa mismatch! Expected {exp_a}, got {act_a}"
        assert act_b1 == exp_b, f"outb1 mismatch! Expected {exp_b}, got {act_b1}"
        assert act_b2 == exp_b, f"outb2 mismatch! Expected {exp_b}, got {act_b2}"

    cocotb.log.info("multi_driver simulation completed successfully!")
