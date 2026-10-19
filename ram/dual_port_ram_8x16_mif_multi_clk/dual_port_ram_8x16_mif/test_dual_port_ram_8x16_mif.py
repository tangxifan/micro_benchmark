import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_dual_port_ram_8x16_mif(dut):
    """Testbench verifying dual_port_ram_8x16_mif with a frozen init.hex file."""

    # Explicitly defined memory entries present in the frozen init.hex
    initial_memory = {
        0: 0x138F,
        1: 0x0020,
        2: 0x37EA,
        7: 0x42FB,
    }

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting dual_port_ram_8x16_mif simulation...")

    # Initialize signals
    dut.wen.value = 0
    dut.ren.value = 0
    dut.waddr.value = 0
    dut.raddr.value = 0
    dut.din.value = 0

    await RisingEdge(dut.clk)

    # 1. Verify explicitly initialized memory contents from init.hex
    cocotb.log.info("Verifying explicitly initialized memory addresses from init.hex...")
    for addr, expected_val in initial_memory.items():
        dut.raddr.value = addr
        dut.ren.value = 1
        # 1-cycle read latency: wait 2 edges (1 to register address, 1 to clock out data)
        await RisingEdge(dut.clk)
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")  # Small propagation delay
        
        actual_val = int(dut.dout.value)
        cocotb.log.info(f"Read Addr {addr}: 0x{actual_val:04X} (Expected: 0x{expected_val:04X})")
        assert actual_val == expected_val, (
            f"Init mismatch at addr {addr}! Expected 0x{expected_val:04X}, got 0x{actual_val:04X}"
        )

    # 2. Test Dynamic Write and Read Operations (covering addresses 3-6 which were uninitialized in init.hex)
    cocotb.log.info("Testing dynamic write and read operations on addresses 3-6...")
    write_tests = [
        (3, 0xABCD),
        (4, 0x1111),
        (5, 0x2222),
        (6, 0xF00D),
    ]

    for addr, wdata in write_tests:
        dut.wen.value = 1
        dut.waddr.value = addr
        dut.din.value = wdata
        await RisingEdge(dut.clk)
        cocotb.log.info(f"Wrote 0x{wdata:04X} to address {addr}")

    # Disable write
    dut.wen.value = 0
    await RisingEdge(dut.clk)

    # Read back and verify updated memory state for addresses 3-6
    for addr, expected_wdata in write_tests:
        dut.raddr.value = addr
        dut.ren.value = 1
        await RisingEdge(dut.clk)
        await RisingEdge(dut.clk)  # 1-cycle read latency
        await Timer(1, unit="ns")

        actual_val = int(dut.dout.value)
        cocotb.log.info(f"Read back Addr {addr}: 0x{actual_val:04X} (Expected: 0x{expected_wdata:04X})")
        assert actual_val == expected_wdata, (
            f"Write/Read mismatch at addr {addr}! Expected 0x{expected_wdata:04X}, got 0x{actual_val:04X}"
        )

    cocotb.log.info("dual_port_ram_8x16_mif simulation completed successfully!")
