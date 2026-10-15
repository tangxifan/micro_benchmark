import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_20(dut):
    """Cocotb testbench for combinatorial mac_20 module"""

    # Test vector list: (a, b, c)
    # DATA_WIDTH = 20, so values range from 0 to 1048575
    test_vectors = [
        (1, 1, 0),
        (1024, 2048, 100),
        (16384, 16384, 50000),
        (65535, 32768, 100000),
        (524287, 262143, 500000),
        (1048575, 1048575, 1048575),
    ]

    dut._log.info("Starting combinatorial mac_20 verification...")

    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (20 bits -> mask 0xFFFFF)
        expected = (a_val * b_val + c_val) & 0xFFFFF

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_20 tests passed successfully!")
