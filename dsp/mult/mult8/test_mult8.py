import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mult8(dut):
    """Testbench verifying purely combinational 8-bit multiplier (mult8)."""

    cocotb.log.info("Starting mult8 simulation...")

    # Test vectors: list of (a, b) tuples for 8-bit operands (0 to 255)
    test_vectors = [
        (0, 0),
        (1, 1),
        (5, 10),
        (15, 15),
        (127, 2),
        (255, 255),  # Max 8-bit unsigned multiplication (65025)
        (0xAB, 0x12),
        (0xFF, 0x01),
    ]

    for val_a, val_b in test_vectors:
        # Drive 8-bit inputs a and b[cite: 12]
        dut.a.value = val_a
        dut.b.value = val_b

        # Allow combinational logic to propagate
        await Timer(1, unit="ns")

        expected_product = val_a * val_b
        actual_product = int(dut.out.value)

        cocotb.log.info(
            f"0x{val_a:02X} ({val_a}) * 0x{val_b:02X} ({val_b}) = "
            f"0x{actual_product:04X} ({actual_product}) [Expected: 0x{expected_product:04X}]"
        )

        assert (
            actual_product == expected_product
        ), f"Mismatch! {val_a} * {val_b}: Expected {expected_product}, got {actual_product}"

    cocotb.log.info("mult8 simulation completed successfully!")
