import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_two_mult8_ram32(dut):
    """Testbench verifying dual 8-bit multipliers combined into a 32-bit dual-port RAM[cite: 15, 16]."""

    # Start a 10ns period clock (100 MHz)[cite: 15, 16]
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting two_mult8_ram32 simulation...")

    # Initialize inputs
    dut.a0.value = 0
    dut.b0.value = 0
    dut.a1.value = 0
    dut.b1.value = 0
    dut.waddr.value = 0
    dut.raddr.value = 0

    await RisingEdge(dut.clk)

    # Test vectors: (a0, b0, a1, b1, address)
    test_vectors = [
        (10, 20, 5, 5, 0),
        (12, 12, 15, 2, 1),
        (255, 1, 128, 2, 2),
        (100, 200, 50, 60, 3),
        (7, 8, 9, 10, 4),
    ]

    # Step 1: Write multiplication products into RAM
    for a0_val, b0_val, a1_val, b1_val, addr in test_vectors:
        dut.a0.value = a0_val
        dut.b0.value = b0_val
        dut.a1.value = a1_val
        dut.b1.value = b1_val
        dut.waddr.value = addr
        dut.raddr.value = addr  # Drive raddr as well

        await RisingEdge(dut.clk)

        mult0 = a0_val * b0_val
        mult1 = a1_val * b1_val
        expected_32bit = (mult1 << 16) | mult0
        cocotb.log.info(
            f"Writing Addr {addr}: a0*b0 = {mult0} (0x{mult0:04X}), "
            f"a1*b1 = {mult1} (0x{mult1:04X}) -> Packed: 0x{expected_32bit:08X}"
        )

    # Allow write to settle
    await Timer(1, unit="ns")

    # Step 2: Read back from RAM addresses and verify
    for a0_val, b0_val, a1_val, b1_val, addr in test_vectors:
        dut.raddr.value = addr

        # Dual-port RAM has a 1-cycle read latency
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        mult0 = a0_val * b0_val
        mult1 = a1_val * b1_val
        expected_product = (mult1 << 16) | mult0
        actual_product = int(dut.out.value)

        cocotb.log.info(
            f"Read Addr {addr}: out = 0x{actual_product:08X} (Expected: 0x{expected_product:08X})"
        )

        assert (
            actual_product == expected_product
        ), f"Mismatch at address {addr}! Expected 0x{expected_product:08X}, got 0x{actual_product:08X}"

    cocotb.log.info("two_mult8_ram32 simulation completed successfully!")
