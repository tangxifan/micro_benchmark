import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_dual_port_ram_1k_functional(dut):
    """Testbench for dual_port_ram_1k (128x8-bit dual-port RAM)."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize control and input signals to known states
    dut.wen.value = 0
    dut.ren.value = 0
    dut.waddr.value = 0
    dut.raddr.value = 0
    dut.din.value = 0

    # Wait for initial synchronization
    await RisingEdge(dut.clk)

    # Define test patterns to write to specific 7-bit addresses (0 to 127)
    test_addresses = [0x00, 0x01, 0x20, 0x7F]
    test_data = [0xA5, 0x5A, 0x33, 0xCC]

    cocotb.log.info("Starting memory write operations...")

    # Write data to multiple addresses
    for addr, data in zip(test_addresses, test_data):
        await RisingEdge(dut.clk)
        dut.wen.value = 1
        dut.waddr.value = addr
        dut.din.value = data

    # Disable write enable
    await RisingEdge(dut.clk)
    dut.wen.value = 0

    cocotb.log.info("Starting memory read and verification operations...")

    # Read back and verify the written data synchronously
    for addr, expected_val in zip(test_addresses, test_data):
        # 1. Setup read address and assert ren on a rising clock edge
        await RisingEdge(dut.clk)
        dut.ren.value = 1
        dut.raddr.value = addr

        # 2. Wait for the next rising edge where the RAM captures raddr and updates 'internal'
        await RisingEdge(dut.clk)

        # 3. Wait a tiny delta after the edge to let combinatorial outputs settle
        await Timer(1, units="ns")

        # Check for undefined (X/Z) values using standard str() conversion
        val_str = str(dut.dout.value)
        if "x" in val_str.lower() or "z" in val_str.lower():
            raise ValueError(f"Output dout contains undefined values: {val_str}")

        actual_val = int(dut.dout.value)
        assert (
            actual_val == expected_val
        ), f"Mismatch at address {hex(addr)}: expected {hex(expected_val)}, got {hex(actual_val)}"

        cocotb.log.info(f"Address {hex(addr)}: Data verified correctly as {hex(actual_val)}")

    # Disable read enable after checks
    await RisingEdge(dut.clk)
    dut.ren.value = 0

    cocotb.log.info("All dual-port RAM 1K tests passed successfully!")
