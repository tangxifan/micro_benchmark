import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mult16(dut):
    """Testbench verifying purely combinational 16-bit multiplier (mult16)."""

    cocotb.log.info("Starting mult16 simulation...")

    # Test vectors: list of (a, b) tuples for 16-bit operands
    test_vectors = [
        (0, 0),
        (1, 1),
        (10, 20),
        (255, 255),
        (1000, 2000),
        (65535, 1),          # Max 16-bit unsigned * 1
        (65535, 65535),      # Max 16-bit unsigned multiplication (4294836225)
        (0xDEAD, 0x1234),
        (0xFFFF, 0x0002),
    ]

    for val_a, val_b in test_vectors:
        # Drive 16-bit inputs a and b[cite: 11]
        dut.a.value = val_a
        dut.b.value = val_b

        # Allow combinational logic to propagate
        await Timer(1, unit="ns")

        expected_product = val_a * val_b
        actual_product = int(dut.out.value)

        cocotb.log.info(
            f"0x{val_a:04X} ({val_a}) * 0x{val_b:04X} ({val_b}) = "
            f"0x{actual_product:08X} ({actual_product}) [Expected: 0x{expected_product:08X}]"
        )

        assert actual_product == expected_product, (
            f"Mismatch! {val_a} * {val_b}: Expected {expected_product}, got {actual_product}"
        )

    cocotb.log.info("mult16 simulation completed successfully!")
