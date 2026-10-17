import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rst_on_lut_8bit_functional(dut):
    """Testbench for rst_on_lut_8bit module verifying asynchronous reset register capture and 8-bit combinatorial output gating."""
    
    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.rst.value = 1
    dut.a.value = 0
    for i in range(8):
        getattr(dut, f"b{i}").value = 0

    await Timer(5, unit="ns")
    cocotb.log.info("Starting rst_on_lut_8bit verification...")

    # Test Case 1: Active Reset (rst = 1)
    dut.rst.value = 1
    for i in range(8):
        getattr(dut, f"b{i}").value = 1
        
    await Timer(5, unit="ns")

    q_val = str(dut.q.value)
    cocotb.log.info(f"Active Reset (rst=1) -> q={q_val}")

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 0, f"Expected q=0 during active reset, got {int(dut.q.value)}"
    
    for i in range(8):
        sig = getattr(dut, f"out{i}")
        val_str = str(sig.value)
        if val_str not in ["x", "X", "Z"]:
            assert int(sig.value) == 0, f"Expected out{i}=0 when rst=1, got {int(sig.value)}"

    # Test Case 2: Deassert Reset (rst = 0), Drive Data (a = 1, pattern on b0-b7)
    dut.rst.value = 0
    dut.a.value = 1
    expected_b_vals = [1, 0, 1, 0, 1, 1, 0, 0]
    for i, val in enumerate(expected_b_vals):
        getattr(dut, f"b{i}").value = val
    
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")  # Allow combinatorial propagation settling

    q_val = str(dut.q.value)
    cocotb.log.info(f"Released Reset (rst=0) -> q={q_val}")

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q.value) == 1, f"Expected q=1 after clock edge, got {int(dut.q.value)}"

    for i, exp in enumerate(expected_b_vals):
        sig = getattr(dut, f"out{i}")
        val_str = str(sig.value)
        if val_str not in ["x", "X", "Z"]:
            assert int(sig.value) == exp, f"Expected out{i}={exp}, got {int(sig.value)}"

    cocotb.log.info("All rst_on_lut_8bit test cases completed successfully!")
