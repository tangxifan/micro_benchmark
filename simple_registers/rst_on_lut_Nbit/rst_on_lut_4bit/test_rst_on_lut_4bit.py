import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_rst_on_lut_4bit_functional(dut):
    """Testbench for rst_on_lut_4bit module verifying asynchronous reset register capture and 4-bit combinatorial output gating."""

    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.rst.value = 1
    dut.a.value = 0
    dut.b0.value = 0
    dut.b1.value = 0
    dut.b2.value = 0
    dut.b3.value = 0

    await Timer(5, unit="ns")
    cocotb.log.info("Starting rst_on_lut_4bit verification...")

    # Test Case 1: Active Reset (rst = 1)
    dut.rst.value = 1
    dut.b0.value = 1
    dut.b1.value = 1
    dut.b2.value = 1
    dut.b3.value = 1
    await Timer(5, unit="ns")

    q_val = str(dut.q.value)
    out0_val = str(dut.out0.value)
    out1_val = str(dut.out1.value)
    out2_val = str(dut.out2.value)
    out3_val = str(dut.out3.value)
    cocotb.log.info(
        f"Active Reset (rst=1) -> q={q_val}, out0-3=[{out0_val},{out1_val},{out2_val},{out3_val}]"
    )

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 0, f"Expected q=0 during active reset, got {int(dut.q.value)}"

    for name, val_str, sig in [
        ("out0", out0_val, dut.out0),
        ("out1", out1_val, dut.out1),
        ("out2", out2_val, dut.out2),
        ("out3", out3_val, dut.out3),
    ]:
        if val_str not in ["x", "X", "Z"]:
            assert (
                int(sig.value) == 0
            ), f"Expected {name}=0 when rst=1 (b & ~rst), got {int(sig.value)}"

    # Test Case 2: Deassert Reset (rst = 0), Drive Data (a = 1, mixed b inputs)
    dut.rst.value = 0
    dut.a.value = 1
    dut.b0.value = 1
    dut.b1.value = 0
    dut.b2.value = 1
    dut.b3.value = 0

    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")  # Allow combinatorial propagation settling

    q_val = str(dut.q.value)
    out0_val = str(dut.out0.value)
    out1_val = str(dut.out1.value)
    out2_val = str(dut.out2.value)
    out3_val = str(dut.out3.value)
    cocotb.log.info(
        f"Released Reset (rst=0) -> q={q_val}, out0-3=[{out0_val},{out1_val},{out2_val},{out3_val}]"
    )

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 1, f"Expected q=1 after clock edge, got {int(dut.q.value)}"

    expected_outs = [1, 0, 1, 0]
    for name, val_str, sig, exp in [
        ("out0", out0_val, dut.out0, 1),
        ("out1", out1_val, dut.out1, 0),
        ("out2", out2_val, dut.out2, 1),
        ("out3", out3_val, dut.out3, 0),
    ]:
        if val_str not in ["x", "X", "Z"]:
            assert int(sig.value) == exp, f"Expected {name}={exp}, got {int(sig.value)}"

    cocotb.log.info("All rst_on_lut_4bit test cases completed successfully!")
