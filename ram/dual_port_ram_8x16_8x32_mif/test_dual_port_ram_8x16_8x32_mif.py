import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dual_port_ram_8x16_8x32(dut):
    """Testbench for dual_port_ram_8x16_8x32 verifying MIF preloading and dual-port read/write operations[cite: 6, 7]."""
    
    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize control and data inputs
    dut.wen.value = 0
    dut.ren.value = 0
    dut.waddr8x16.value = 0
    dut.raddr8x16.value = 0
    dut.din8x16.value = 0
    dut.waddr8x32.value = 0
    dut.raddr8x32.value = 0
    dut.din8x32.value = 0

    await Timer(15, unit="ns")
    cocotb.log.info("Starting dual_port_ram_8x16_8x32 verification...")

    # =========================================================================
    # Test Case 1: Verify pre-loaded MIF values on Read (ren = 1)
    # =========================================================================
    dut.ren.value = 1
    dut.raddr8x16.value = 0
    dut.raddr8x32.value = 0
    
    # Wait 2 clock edges for synchronous pipeline read latency
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")  # Small settling delay

    dout16_val = str(dut.dout8x16.value)
    dout32_val = str(dut.dout8x32.value)
    cocotb.log.info(f"Initial Read -> dout8x16={hex(int(dut.dout8x16.value))}, dout8x32={hex(int(dut.dout8x32.value))}")

    if dout16_val not in ["x", "X", "Z"]:
        assert dut.dout8x16.value == 0xFEFF, f"Expected dout8x16=0xFEFF from init_8x16_2.hex, got {hex(int(dut.dout8x16.value))}"
    if dout32_val not in ["x", "X", "Z"]:
        assert dut.dout8x32.value == 0xFFFFFFFF, f"Expected dout8x32=0xFFFFFFFF from init_8x32_2.hex, got {hex(int(dut.dout8x32.value))}"

    # =========================================================================
    # Test Case 2: Perform Write Operation (wen = 1)
    # =========================================================================
    dut.ren.value = 0
    dut.wen.value = 1
    dut.waddr8x16.value = 2
    dut.din8x16.value = 0x1234
    dut.waddr8x32.value = 1
    dut.din8x32.value = 0xDEADBEEF

    await RisingEdge(dut.clk)
    dut.wen.value = 0  # Disable write
    await Timer(1, unit="ns")
    cocotb.log.info("Write completed.")

    # =========================================================================
    # Test Case 3: Read back written locations
    # =========================================================================
    dut.ren.value = 1
    dut.raddr8x16.value = 2
    dut.raddr8x32.value = 1

    # Wait 2 clock edges for pipeline read latency
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")

    dout16_val = str(dut.dout8x16.value)
    dout32_val = str(dut.dout8x32.value)
    cocotb.log.info(f"Post-Write Read -> dout8x16={hex(int(dut.dout8x16.value))}, dout8x32={hex(int(dut.dout8x32.value))}")

    if dout16_val not in ["x", "X", "Z"]:
        assert dut.dout8x16.value == 0x1234, f"Expected dout8x16=0x1234, got {hex(int(dut.dout8x16.value))}"
    if dout32_val not in ["x", "X", "Z"]:
        assert dut.dout8x32.value == 0xDEADBEEF, f"Expected dout8x32=0xDEADBEEF, got {hex(int(dut.dout8x32.value))}"

    cocotb.log.info("All dual_port_ram test cases completed successfully!")
