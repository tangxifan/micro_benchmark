import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_4(dut):
    """Cocotb testbench for combinatorial mac_4 module"""

    # Test vector list: (a, b, c)
    # DATA_WIDTH = 4, so values range from 0 to 15
    test_vectors = [(1, 1, 0), (3, 5, 2), (7, 8, 5), (12, 3, 10), (15, 15, 15), (4, 4, 4)]

    dut._log.info("Starting combinatorial mac_4 verification...")

    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (4 bits -> mask 0xF)
        expected = (a_val * b_val + c_val) & 0xF

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_4 tests passed successfully!")
