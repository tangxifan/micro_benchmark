import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dpram_n_clk(dut):
    """Verification for N-instance Dual-Port RAM."""
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk_a.value)
    dut._log.info(f"Testing {num_clks}-instance dual-port RAM...")

    # Start separate clocks for write (clk_a) and read (clk_b) ports
    for i in range(num_clks):
        cocotb.start_soon(Clock(dut.clk_a[i], 10 + i * 2, units="ns").start())
        cocotb.start_soon(Clock(dut.clk_b[i], 15 + i * 2, units="ns").start())

    dut.we_a.value = 0
    await Timer(50, units="ns")

    # Test Write -> Read sequence for each DPRAM instance
    for i in range(num_clks):
        test_addr = 0x10 + i
        test_data = 0xA5A5 ^ (i * 0x1111)

        # Write data on Port A
        addr_a_val = test_addr << (i * 8)
        din_a_val = test_data << (i * 16)
        we_a_val = 1 << i

        dut.addr_a.value = addr_a_val
        dut.din_a.value = din_a_val
        dut.we_a.value = we_a_val

        await RisingEdge(dut.clk_a[i])
        await Timer(1, units="ns")
        dut.we_a.value = 0

        # Read data back on Port B
        addr_b_val = test_addr << (i * 8)
        dut.addr_b.value = addr_b_val

        await RisingEdge(dut.clk_b[i])
        await Timer(1, units="ns")

        actual_dout = (int(dut.dout_b.value) >> (i * 16)) & 0xFFFF
        assert actual_dout == test_data, f"Instance {i} mismatch: expected {hex(test_data)}, got {hex(actual_dout)}"

    dut._log.info("All dual-port RAM instances verified successfully!")
