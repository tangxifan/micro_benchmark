import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge


@cocotb.test()
async def test_rstn_sync(dut):

    # Start clock
    cocotb.start_soon(
        Clock(dut.clk, 10, units="ns").start()
    )

    # ---------------------------------------------------------
    # Initial conditions
    # ---------------------------------------------------------
    dut.arst_n.value = 0

    # Allow async reset to propagate
    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        f"Async assertion failed: srst_n={dut.srst_n.value}"
    )

    print("PASS: Asynchronous reset assertion")

    # ---------------------------------------------------------
    # De-assert reset
    # ---------------------------------------------------------
    dut.arst_n.value = 1

    # De-assertion should NOT immediately propagate
    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        "Reset de-asserted asynchronously!"
    )

    print("PASS: Reset remains asserted after arst_n de-assertion")

    # ---------------------------------------------------------
    # First rising edge
    # ---------------------------------------------------------
    await RisingEdge(dut.clk)

    # Give NBA/nonblocking assignment time to update
    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        f"Reset released too early after first clock: "
        f"srst_n={dut.srst_n.value}"
    )

    print("PASS: Reset remains asserted after first clock")

    # ---------------------------------------------------------
    # Second rising edge
    # ---------------------------------------------------------
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst_n.value == 1, (
        f"Reset did not release after second clock: "
        f"srst_n={dut.srst_n.value}"
    )

    print("PASS: Reset synchronously de-asserted")

    # ---------------------------------------------------------
    # Assert reset BETWEEN clock edges
    # ---------------------------------------------------------
    await Timer(2, units="ns")

    dut.arst_n.value = 0

    # Don't wait for a clock!
    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        "Reset did not assert asynchronously"
    )

    print("PASS: Reset asynchronously asserted between clocks")

    # ---------------------------------------------------------
    # De-assert again
    # ---------------------------------------------------------
    dut.arst_n.value = 1

    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        "Reset released asynchronously on second attempt"
    )

    # First clock
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst_n.value == 0, (
        "Reset released after only one clock"
    )

    # Second clock
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.srst_n.value == 1, (
        "Reset failed to release after two clocks"
    )

    print("PASS: Second reset cycle")

    print("==========================================")
    print("TEST PASSED")
    print("==========================================")
