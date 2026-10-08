import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dpram_4_clk_flattened(dut):
    """Verification for 4-instance Dual-Port RAM with flattened scalar ports across concurrent clock domains."""
    num_clks = 4
    dut._log.info(f"Testing {num_clks}-instance dual-port RAM with flattened ports...")

    # Start separate clocks for write (clk_a) and read (clk_b) ports using scalar attribute handles
    for i in range(num_clks):
        cocotb.start_soon(Clock(getattr(dut, f"clk_a{i}"), 10 + i * 2, units="ns").start())
        cocotb.start_soon(Clock(getattr(dut, f"clk_b{i}"), 15 + i * 2, units="ns").start())
        getattr(dut, f"we_a{i}").value = 0

    await Timer(50, units="ns")

    # Test Write -> Read sequence for each DPRAM instance
    for i in range(num_clks):
        test_addr = 0x10 + i
        test_data = 0xA5A5 ^ (i * 0x1111)

        # Write data on Port A using scalar ports
        getattr(dut, f"addr_a{i}").value = test_addr
        getattr(dut, f"din_a{i}").value = test_data
        getattr(dut, f"we_a{i}").value = 1

        await RisingEdge(getattr(dut, f"clk_a{i}"))
        await Timer(1, units="ns")
        getattr(dut, f"we_a{i}").value = 0

        # Read data back on Port B using scalar ports
        getattr(dut, f"addr_b{i}").value = test_addr

        await RisingEdge(getattr(dut, f"clk_b{i}"))
        await Timer(1, units="ns")

        actual_dout = int(getattr(dut, f"dout_b{i}").value) & 0xFFFF
        assert actual_dout == test_data, f"Instance {i} mismatch: expected {hex(test_data)}, got {hex(actual_dout)}"

    dut._log.info("All flattened 4-clock dual-port RAM instances verified successfully!")
