import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_clk_gate(dut):
    """Testbench verifying clk_gate synchronous reset and clock-gated output logic."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk_i, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting clk_gate simulation...")

    # Initialize inputs
    dut.rst_i.value = 1
    dut.data_i.value = 0

    await RisingEdge(dut.clk_i)
    await Timer(1, unit="ns")

    # 1. Test Synchronous Reset (q should be 0, data_o should be 0)
    assert (
        int(dut.data_o.value) == 0
    ), f"Reset failed! Expected data_o=0, got {int(dut.data_o.value)}"
    cocotb.log.info("Synchronous reset verified: data_o = 0")

    # 2. Release reset and test with data_i = 1
    dut.rst_i.value = 0
    dut.data_i.value = 1

    # Before the next clock edge, q is still 0
    await Timer(2, unit="ns")

    # Wait for positive clock edge where q <= 1
    await RisingEdge(dut.clk_i)
    await Timer(1, unit="ns")

    assert (
        int(dut.data_o.value) == 1
    ), f"Clock gating failed! Expected data_o=1, got {int(dut.data_o.value)}"
    cocotb.log.info("Clock gating active: data_o = 1")

    # 3. Test toggling data_i while q remains 1
    dut.data_i.value = 0
    await Timer(2, unit="ns")
    assert (
        int(dut.data_o.value) == 0
    ), f"data_i low failed! Expected data_o=0, got {int(dut.data_o.value)}"

    dut.data_i.value = 1
    await Timer(2, unit="ns")
    assert (
        int(dut.data_o.value) == 1
    ), f"data_i high failed! Expected data_o=1, got {int(dut.data_o.value)}"

    # 4. Assert reset again and check output goes low
    dut.rst_i.value = 1
    await RisingEdge(dut.clk_i)
    await Timer(1, unit="ns")

    assert (
        int(dut.data_o.value) == 0
    ), f"Re-asserting reset failed! Expected data_o=0, got {int(dut.data_o.value)}"

    cocotb.log.info("clk_gate simulation completed successfully!")
