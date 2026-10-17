import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_dual_port_ram(dut):
    """Testbench verifying dual_port_ram_8x16_8x32 read/write operations for both 8x16 and 8x32 cores."""

    # Start 100 MHz clock (10 ns period)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    cocotb.log.info("Starting dual_port_ram_8x16_8x32 simulation...")

    # Initialize control inputs to inactive state
    dut.wen.value = 0
    dut.ren.value = 0
    dut.waddr8x16.value = 0
    dut.raddr8x16.value = 0
    dut.din8x16.value = 0
    dut.waddr8x32.value = 0
    dut.raddr8x32.value = 0
    dut.din8x32.value = 0

    await RisingEdge(dut.clk)

    # -------------------------------------------------------------
    # 1. Read Test (Initial MIF contents loaded via $readmemh)
    # -------------------------------------------------------------
    cocotb.log.info("Testing read operation across both RAM cores...")
    dut.ren.value = 1

    for addr in range(3):
        dut.raddr8x16.value = addr
        dut.raddr8x32.value = addr
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")  # Settling delay for output assignment

        cocotb.log.info(
            f"Read Addr {addr} -> dout8x16 = 0x{int(dut.dout8x16.value):04X}, "
            f"dout8x32 = 0x{int(dut.dout8x32.value):08X}"
        )

    dut.ren.value = 0
    await RisingEdge(dut.clk)

    # -------------------------------------------------------------
    # 2. Write Test (Perform writes to both RAM cores)
    # -------------------------------------------------------------
    cocotb.log.info("Testing write operation to both RAM cores...")
    write_data_16 = [0xA5A5, 0x5A5A, 0x1234]
    write_data_32 = [0xDEADBEEF, 0xCAFEBABE, 0x87654321]

    dut.wen.value = 1
    for addr in range(3):
        dut.waddr8x16.value = addr
        dut.din8x16.value = write_data_16[addr]

        dut.waddr8x32.value = addr
        dut.din8x32.value = write_data_32[addr]

        await RisingEdge(dut.clk)

    dut.wen.value = 0
    await RisingEdge(dut.clk)

    # -------------------------------------------------------------
    # 3. Read-After-Write Verification
    # -------------------------------------------------------------
    cocotb.log.info("Verifying written data via read operations...")
    dut.ren.value = 1

    for addr in range(3):
        dut.raddr8x16.value = addr
        dut.raddr8x32.value = addr
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        val_16 = int(dut.dout8x16.value)
        val_32 = int(dut.dout8x32.value)

        cocotb.log.info(
            f"Addr {addr}: Read dout8x16 = 0x{val_16:04X} (Expected: 0x{write_data_16[addr]:04X}), "
            f"dout8x32 = 0x{val_32:08X} (Expected: 0x{write_data_32[addr]:08X})"
        )

        assert (
            val_16 == write_data_16[addr]
        ), f"Mismatch at 8x16 RAM address {addr}! Expected 0x{write_data_16[addr]:04X}, got 0x{val_16:04X}"
        assert (
            val_32 == write_data_32[addr]
        ), f"Mismatch at 8x32 RAM address {addr}! Expected 0x{write_data_32[addr]:08X}, got 0x{val_32:08X}"

    dut.ren.value = 0
    cocotb.log.info("dual_port_ram_8x16_8x32 simulation completed successfully!")
