import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_mult8_ram8(dut):
    """Testbench verifying mult8_ram8 combinational multiplication stored and read from dual-port RAMs[cite: 14, 15]."""

    # Start a 10ns period clock (100 MHz)[cite: 14, 15]
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting mult8_ram8 simulation...")

    # Initialize inputs
    dut.a.value = 0
    dut.b.value = 0
    dut.waddr.value = 0
    dut.raddr.value = 0

    await RisingEdge(dut.clk)

    # Test vectors: (a, b, ram_address)
    test_vectors = [
        (12, 10, 0),
        (15, 15, 1),
        (255, 2, 2),
        (100, 200, 3),
        (7, 8, 4),
    ]

    # Step 1: Write multiplication results into RAM at specified addresses
    for val_a, val_b, addr in test_vectors:
        dut.a.value = val_a
        dut.b.value = val_b
        dut.waddr.value = addr
        dut.raddr.value = addr  # Point read address elsewhere or same for pipeline check

        await RisingEdge(dut.clk)
        expected_prod = val_a * val_b
        cocotb.log.info(f"Writing {val_a} * {val_b} = {expected_prod} to address {addr}")

    # Allow write to settle
    await Timer(1, unit="ns")

    # Step 2: Read back from RAM addresses and verify
    for val_a, val_b, addr in test_vectors:
        dut.raddr.value = addr
        
        # Dual-port RAM has a 1-cycle read latency
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        expected_product = val_a * val_b
        actual_product = int(dut.out.value)

        cocotb.log.info(
            f"Read Addr {addr}: Product = {actual_product} (Expected: {expected_product})"
        )

        assert actual_product == expected_product, (
            f"Mismatch at address {addr}! Expected {expected_product}, got {actual_product}"
        )

    cocotb.log.info("mult8_ram8 simulation completed successfully!")
