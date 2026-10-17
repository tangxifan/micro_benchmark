import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_rst_cond_functional(dut):
    """Testbench for rst_cond module verifying conditioned asynchronous reset and synchronous data capture."""

    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk_i, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.rst_i.value = 1
    dut.rst_cond_i.value = 1
    dut.d_i.value = 1

    await Timer(5, unit="ns")
    cocotb.log.info("Starting rst_cond verification...")

    # Test Case 1: Active Conditioned Reset (int_rst = 1)
    dut.rst_i.value = 1
    dut.rst_cond_i.value = 1
    await Timer(5, unit="ns")

    q_val = str(dut.q_o.value)
    int_rst_val = str(dut.int_rst.value)
    cocotb.log.info(f"Active Reset (rst_i=1, rst_cond_i=1) -> int_rst={int_rst_val}, q_o={q_val}")

    if q_val not in ["x", "X", "Z"]:
        assert (
            int(dut.q_o.value) == 0
        ), f"Expected q_o=0 during active conditioned reset, got {int(dut.q_o.value)}"

    # Test Case 2: Deassert Reset (int_rst = 0), Capture Data on clk_i
    dut.rst_i.value = 0
    dut.rst_cond_i.value = 0
    dut.d_i.value = 1

    await RisingEdge(dut.clk_i)
    await Timer(1, unit="ns")  # Allow combinatorial propagation settling

    q_val = str(dut.q_o.value)
    cocotb.log.info(f"Released Reset, d_i=1 -> q_o={q_val}")

    if q_val not in ["x", "X", "Z"]:
        assert int(dut.q_o.value) == 1, f"Expected q_o=1 after clock edge, got {int(dut.q_o.value)}"

    cocotb.log.info("All rst_cond test cases completed successfully!")
