import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mac_36(dut):
    """Cocotb testbench for combinatorial mac_36 module with safe width handling"""

    # Dynamically check the actual width of the DUT signal from simulation handle
    # Fallback to 36 if width attribute isn't directly exposed
    try:
        width_a = len(dut.a)
    except TypeError:
        width_a = 36

    max_val = (1 << width_a) - 1
    mask = max_val

    dut._log.info(f"Detected signal 'a' width: {width_a} bits (max value: {max_val})")

    # Test vector list with values scaled to fit whatever DATA_WIDTH is active in simulation
    raw_test_vectors = [
        (1, 1, 0),
        (65536, 65536, 1000),
        (1048576, 1048576, 50000),
        (268435456, 1024, 1000000),
        (8589934591, 4096, 50000000),
        (68719476735, 68719476735, 68719476735),
    ]

    dut._log.info("Starting combinatorial mac_36 verification...")

    for a_raw, b_raw, c_raw in raw_test_vectors:
        # Mask inputs to fit the actual instantiated width of the DUT to prevent out-of-range errors
        a_val = a_raw & mask
        b_val = b_raw & mask
        c_val = c_raw & mask

        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val

        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")

        # Calculate expected output using the same bitmask width
        expected = (a_val * b_val + c_val) & mask

        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0

        dut._log.info(
            f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}"
        )
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"

    dut._log.info("All combinatorial mac_36 tests passed successfully!")
