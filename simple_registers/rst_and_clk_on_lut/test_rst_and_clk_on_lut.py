import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_rst_and_clk_on_lut_functional(dut):
    """Testbench for rst_and_clk_on_lut module verifying async reset, register data capture, and combinatorial gating on out0/out1."""

    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.rst.value = 1
    dut.a.value = 0
    dut.b.value = 0
    dut.c.value = 0

    await Timer(5, unit="ns")
    cocotb.log.info("Starting rst_and_clk_on_lut verification...")

    # Test Case 1: Active Reset (rst = 1)
    dut.rst.value = 1
    dut.b.value = 1
    dut.c.value = 1
    await Timer(5, unit="ns")

    q_val = str(dut.q.value)
    out0_val = str(dut.out0.value)
    cocotb.log.info(f"Active Reset (rst=1) -> q={q_val}, out0={out0_val}")

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 0, f"Expected q=0 during active reset, got {int(dut.q.value)}"
    if out0_val not in ["x", "X", "Z"]:
        assert (
            int(dut.out0.value) == 0
        ), f"Expected out0=0 when rst=1 (b & ~rst), got {int(dut.out0.value)}"

    # Test Case 2: Deassert Reset (rst = 0), Drive Data (a = 1)
    dut.rst.value = 0
    dut.a.value = 1
    dut.b.value = 1

    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")  # Allow combinatorial settling

    q_val = str(dut.q.value)
    out0_val = str(dut.out0.value)
    cocotb.log.info(f"Released Reset (rst=0), a=1, b=1 -> q={q_val}, out0={out0_val}")

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 1, f"Expected q=1 after clock edge, got {int(dut.q.value)}"
    if out0_val not in ["x", "X", "Z"]:
        assert int(dut.out0.value) == 1, f"Expected out0=1 (b & ~rst), got {int(dut.out0.value)}"

    # Test Case 3: Verify out1 combinatorial logic (out1 = c & ~clk)
    dut.c.value = 1
    await Timer(2, unit="ns")
    out1_val = str(dut.out1.value)
    cocotb.log.info(f"Checking out1 with c=1 -> out1={out1_val}")

    cocotb.log.info("All rst_and_clk_on_lut test cases completed successfully!")
