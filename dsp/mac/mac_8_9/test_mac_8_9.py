import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_8_9(dut):
    """Cocotb testbench for mac_8_9 dual 8-bit/9-bit slice MAC module"""

    # Test vector list: tuples of ((a_slice1, b_slice1, c_slice1), (a_slice2, b_slice2, c_slice2))
    # Slice 1: 8-bit (values 0 to 255)
    # Slice 2: 9-bit (values 0 to 511)
    test_vectors = [
        ((1, 1, 0), (2, 2, 1)),
        ((15, 20, 10), (30, 40, 50)),
        ((100, 50, 25), (255, 128, 64)),
        ((255, 255, 255), (511, 511, 511)),
        ((42, 13, 7), (123, 45, 67)),
    ]

    dut._log.info("Starting dual-slice mac_8_9 verification...")

    for slice1_vals, slice2_vals in test_vectors:
        a1, b1, c1 = slice1_vals
        a2, b2, c2 = slice2_vals

        # Pack inputs into the 18-bit vector: a[17:9] and a[8:0]
        dut.a.value = (a2 << 9) | (a1 & 0x1FF)
        dut.b.value = (b2 << 9) | (b1 & 0x1FF)
        dut.c.value = (c2 << 9) | (c1 & 0x1FF)

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Expected outputs for each slice with respective bitmasks (8-bit / 9-bit)
        expected_slice1 = (a1 * b1 + c1) & 0x1FF  # 9-bit slice container
        expected_slice2 = (a2 * b2 + c2) & 0x1FF  # 9-bit slice container
        expected_full = (expected_slice2 << 9) | expected_slice1

        try:
            actual_full = int(dut.out.value)
        except ValueError:
            actual_full = 0

        actual_slice1 = actual_full & 0x1FF
        actual_slice2 = (actual_full >> 9) & 0x1FF

        dut._log.info(
            f"Slice 1 (8-bit) - In: ({a1}, {b1}, {c1}) -> Exp: {expected_slice1}, Got: {actual_slice1} | "
            f"Slice 2 (9-bit) - In: ({a2}, {b2}, {c2}) -> Exp: {expected_slice2}, Got: {actual_slice2}"
        )

        assert (
            actual_slice1 == expected_slice1
        ), f"Slice 1 Mismatch: expected {expected_slice1}, got {actual_slice1}"
        assert (
            actual_slice2 == expected_slice2
        ), f"Slice 2 Mismatch: expected {expected_slice2}, got {actual_slice2}"

    dut._log.info("All dual-slice mac_8_9 tests passed successfully!")
