import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


def set_signals(dut, waddr_val, raddr_val, a_val, b_val, wen_val, ren_val):
    """Helper function to drive bit-flattened input buses for pipelined_8bit_adder."""
    for i in range(6):
        getattr(dut, f"waddr_{i}_").value = (waddr_val >> i) & 1
        getattr(dut, f"raddr_{i}_").value = (raddr_val >> i) & 1
    for i in range(7):
        getattr(dut, f"a_{i}_").value = (a_val >> i) & 1
        getattr(dut, f"b_{i}_").value = (b_val >> i) & 1
    dut.wen.value = wen_val
    dut.ren.value = ren_val


@cocotb.test()
async def test_pipelined_adder_functional(dut):
    """Testbench for pipelined_8bit_adder verifying pipelined addition and RAM storage."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize all signals to 0
    set_signals(dut, 0, 0, 0, 0, 0, 0)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Define test cases: (waddr, operand_a, operand_b) - operands must fit in 7 bits (0 to 127)
    test_data = [
        (0x01, 10, 20),  # Expected sum: 30
        (0x02, 50, 50),  # Expected sum: 100
        (0x05, 5, 15),  # Expected sum: 20
        (0x0A, 60, 65),  # Expected sum: 125 (both operands <= 127)
    ]

    cocotb.log.info("Starting pipelined write operations...")

    # Stream write operations into the pipeline
    for waddr, a, b in [(tc[0], tc[1], tc[2]) for tc in test_data]:
        set_signals(dut, waddr_val=waddr, raddr_val=0, a_val=a, b_val=b, wen_val=1, ren_val=0)
        await RisingEdge(dut.clk)

    # Flush the 2-stage pipeline (st0, st1) to ensure data commits to RAM
    for _ in range(3):
        set_signals(dut, 0, 0, 0, 0, 0, 0)
        await RisingEdge(dut.clk)

    cocotb.log.info("Starting read and verification operations...")

    # Read back and verify each stored result
    for waddr, a, b in [(tc[0], tc[1], tc[2]) for tc in test_data]:
        expected_sum = a + b

        # Issue read command at address matching waddr
        set_signals(dut, waddr_val=0, raddr_val=waddr, a_val=0, b_val=0, wen_val=0, ren_val=1)
        await RisingEdge(dut.clk)

        # Deassert read enable and wait for the synchronous read register output update
        set_signals(dut, 0, 0, 0, 0, 0, 0)
        await RisingEdge(dut.clk)

        # Wait a tiny delta for combinatorial settling
        await Timer(1, unit="ns")

        # Reconstruct output q from bit-flattened outputs q_0_ to q_7_
        actual_q = 0
        for i in range(8):
            val = int(getattr(dut, f"q_{i}_").value)
            actual_q |= val << i

        assert (
            actual_q == expected_sum
        ), f"Mismatch at address {hex(waddr)}: expected {expected_sum} ({a}+{b}), got {actual_q}"

        cocotb.log.info(f"Address {hex(waddr)} verified successfully: {a} + {b} = {actual_q}")

    cocotb.log.info("All pipelined 8-bit adder tests passed successfully!")
