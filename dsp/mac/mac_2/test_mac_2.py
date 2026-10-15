import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_2(dut):
    """Cocotb testbench for combinatorial mac_2 module"""

    # Test vector list: (a, b, c)
    # DATA_WIDTH = 2 (values range from 0 to 3)[cite: 4]
    test_vectors = [(1, 1, 0), (2, 3, 1), (3, 3, 2), (0, 2, 3), (1, 3, 1), (2, 2, 2)]

    dut._log.info("Starting combinatorial mac_2 verification...")

    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (2 bits -> mask 0x3)
        expected = (a_val * b_val + c_val) & 0x3

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_2 tests passed successfully!")
