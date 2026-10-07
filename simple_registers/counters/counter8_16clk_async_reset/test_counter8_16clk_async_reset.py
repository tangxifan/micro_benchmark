import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_counter_n_clock(dut):
    """Universal verification for N-clock async reset counters."""
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk.value)
    dut._log.info(f"Testing {num_clks}-clock domain counter configuration...")

    for i in range(num_clks):
        period = 10 + (i * 2)
        cocotb.start_soon(Clock(dut.clk[i], period, units="ns").start())

    # Reset test
    dut.reset.value = 1
    await Timer(50, units="ns")
    assert int(dut.result.value) == 0, "Reset verification failed"

    # Increment test
    dut.reset.value = 0
    await Timer(1, units="ns")

    for i in range(num_clks):
        expected_val = 0
        for step in range(1, 6):
            await RisingEdge(dut.clk[i])
            await Timer(1, units="ns")
            expected_val = (expected_val + 1) & 0xFF
            actual_val = (int(dut.result.value) >> (i * 8)) & 0xFF
            assert actual_val == expected_val, f"Domain {i} mismatch: expected {expected_val}, got {actual_val}"

    # Asynchronous reset test mid-run
    dut.reset.value = 1
    await Timer(5, units="ns")
    assert int(dut.result.value) == 0, "Mid-run async reset failed"
    dut.reset.value = 0
