import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dpram_single_clk(dut):
    """Verification for single-instance Dual-Port RAM."""
    dut._log.info("Testing single-instance dual-port RAM...")

    # Start separate clocks for write (clk_a) and read (clk_b) ports
    cocotb.start_soon(Clock(dut.clk_a, 10, unit="ns").start())
    cocotb.start_soon(Clock(dut.clk_b, 15, unit="ns").start())

    dut.we_a.value = 0
    await Timer(50, unit="ns")

    test_addr = 0x10
    test_data = 0xA5A5

    # Write data on Port A
    dut.addr_a.value = test_addr
    dut.din_a.value = test_data
    dut.we_a.value = 1

    await RisingEdge(dut.clk_a)
    await Timer(1, unit="ns")
    dut.we_a.value = 0

    # Read data back on Port B
    dut.addr_b.value = test_addr

    await RisingEdge(dut.clk_b)
    await Timer(1, unit="ns")

    actual_dout = int(dut.dout_b.value) & 0xFFFF
    assert actual_dout == test_data, f"Mismatch: expected {hex(test_data)}, got {hex(actual_dout)}"

    dut._log.info("Single-instance dual-port RAM verified successfully!")
