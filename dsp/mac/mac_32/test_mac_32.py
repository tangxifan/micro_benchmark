import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_32(dut):
    """Cocotb testbench for combinatorial mac_32 module"""

    # Test vector list: (a, b, c)
    # DATA_WIDTH = 32, so values range from 0 to 4294967295
    test_vectors = [
        (1, 1, 0),
        (65536, 65536, 1000),
        (1048576, 1048576, 50000),
        (16777216, 16777216, 1000000),
        (2147483647, 1000, 5000000),
        (4294967295, 4294967295, 4294967295),
    ]

    dut._log.info("Starting combinatorial mac_32 verification...")

    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (32 bits -> mask 0xFFFFFFFF)
        expected = (a_val * b_val + c_val) & 0xFFFFFFFF

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_32 tests passed successfully!")
