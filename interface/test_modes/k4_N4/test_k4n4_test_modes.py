import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_k4n4_functional(dut):
    """Testbench for K4n4_test module verifying combinatorial logic gates and their synchronous register counterparts."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs to 0
    dut.a.value = 0
    dut.b.value = 0
    dut.c.value = 0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Define test input combinations (a, b, c)
    test_vectors = [
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
    ]

    cocotb.log.info("Starting K4n4_test logic verification...")

    for a, b, c in test_vectors:
        # Drive inputs
        dut.a.value = a
        dut.b.value = b
        dut.c.value = c

        # Wait for a tiny delta for combinatorial paths to settle
        await Timer(1, unit="ns")

        # Compute expected combinatorial values
        exp_xor = a ^ b ^ c
        exp_xnor = 0 if exp_xor else 1
        exp_or = 1 if (a or b or c) else 0
        exp_nor = 0 if (a or b or c) else 1
        exp_and = 1 if (a and b and c) else 0
        exp_nand = 0 if (a and b and c) else 1

        # Check combinatorial outputs immediately
        assert int(dut.XOR.value) == exp_xor, f"XOR mismatch for ({a},{b},{c})"
        assert int(dut.XNOR.value) == exp_xnor, f"XNOR mismatch for ({a},{b},{c})"
        assert int(dut.OR.value) == exp_or, f"OR mismatch for ({a},{b},{c})"
        assert int(dut.NOR.value) == exp_nor, f"NOR mismatch for ({a},{b},{c})"
        assert int(dut.AND.value) == exp_and, f"AND mismatch for ({a},{b},{c})"
        assert int(dut.NAND.value) == exp_nand, f"NAND mismatch for ({a},{b},{c})"

        # Wait for the positive clock edge to latch sync outputs
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        # Verify synchronous registers capture the previous combinatorial values
        assert int(dut.XOR_sync.value) == exp_xor, f"XOR_sync mismatch"
        assert int(dut.XNOR_sync.value) == exp_xnor, f"XNOR_sync mismatch"
        assert int(dut.OR_sync.value) == exp_or, f"OR_sync mismatch"
        assert int(dut.NOR_sync.value) == exp_nor, f"NOR_sync mismatch"
        assert int(dut.AND_sync.value) == exp_and, f"AND_sync mismatch"
        assert int(dut.NAND_sync.value) == exp_nand, f"NAND_sync mismatch"

        cocotb.log.info(
            f"Verified vector a={a}, b={b}, c={c} -> Comb & Sync outputs matched successfully."
        )

    cocotb.log.info("All K4n4_test test cases passed successfully!")
