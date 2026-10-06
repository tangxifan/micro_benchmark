import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge


@cocotb.test()
async def test_rst_sync(dut):

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # ---------------------------------------------------------
    # Initial reset assertion
    # ---------------------------------------------------------
    dut.arst.value = 1

    await Timer(1, units="ns")

    assert dut.srst.value == 1, f"Async assertion failed: srst={dut.srst.value}"

    print("PASS: Asynchronous reset assertion")

    # ---------------------------------------------------------
    # De-assert reset
    # ---------------------------------------------------------
    dut.arst.value = 0

    await Timer(1, units="ns")

    assert dut.srst.value == 1, "Reset de-asserted asynchronously!"

    print("PASS: Reset remains asserted after arst de-assertion")

    # ---------------------------------------------------------
    # First rising edge
    # ---------------------------------------------------------
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst.value == 1, "Reset released after only one clock"

    print("PASS: Reset remains asserted after first clock")

    # ---------------------------------------------------------
    # Second rising edge
    # ---------------------------------------------------------
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst.value == 0, "Reset did not synchronously de-assert"

    print("PASS: Reset synchronously de-asserted")

    # ---------------------------------------------------------
    # Assert reset BETWEEN clock edges
    # ---------------------------------------------------------
    await Timer(2, units="ns")

    dut.arst.value = 1

    await Timer(1, units="ns")

    assert dut.srst.value == 1, "Reset did not assert asynchronously"

    print("PASS: Reset asynchronously asserted between clocks")

    # ---------------------------------------------------------
    # De-assert again
    # ---------------------------------------------------------
    dut.arst.value = 0

    await Timer(1, units="ns")

    assert dut.srst.value == 1, "Reset released asynchronously"

    # First clock
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst.value == 1, "Reset released after only one clock"

    # Second clock
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst.value == 0, "Reset failed to release after two clocks"

    print("PASS: Second reset cycle")

    print("==========================================")
    print("TEST PASSED")
    print("==========================================")
