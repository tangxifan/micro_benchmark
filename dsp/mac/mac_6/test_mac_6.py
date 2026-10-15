import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_6(dut):
    """Cocotb testbench for combinatorial mac_6 module"""

    # Test vector list: (a, b, c)
    # DATA_WIDTH = 6, so values range from 0 to 63
    test_vectors = [(1, 1, 0), (5, 7, 12), (15, 20, 10), (31, 31, 31), (45, 12, 8), (63, 63, 63)]

    dut._log.info("Starting combinatorial mac_6 verification...")

    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (6 bits -> mask 0x3F)
        expected = (a_val * b_val + c_val) & 0x3F

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_6 tests passed successfully!")
