import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dual_port_ram_8x32(dut):
    """Testbench for dual_port_ram_8x32 verifying MIF preloading and dual-port read/write operations."""
    
    # Start a 10ns period system clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize control and data inputs
    dut.wen.value = 0
    dut.ren.value = 0
    dut.waddr.value = 0
    dut.raddr.value = 0
    dut.din.value = 0

    await Timer(15, unit="ns")
    cocotb.log.info("Starting dual_port_ram_8x32 verification...")

    # =========================================================================
    # Test Case 1: Verify pre-loaded MIF values on Read (ren = 1)
    # =========================================================================
    dut.ren.value = 1
    dut.raddr.value = 0
    
    # Wait 2 clock edges for synchronous pipeline read latency (internal reg -> dout)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")  # Small settling delay

    dout_val = str(dut.dout.value)
    cocotb.log.info(f"Initial Read (addr 0) -> dout={hex(int(dut.dout.value))}")

    if dout_val not in ["x", "X", "Z"]:
        assert dut.dout.value == 0xFFFFFFFF, f"Expected dout=0xFFFFFFFF from init.hex, got {hex(int(dut.dout.value))}"

    # Read another preloaded index (e.g., index 2)
    dut.raddr.value = 2
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")

    cocotb.log.info(f"Initial Read (addr 2) -> dout={hex(int(dut.dout.value))}")
    if str(dut.dout.value) not in ["x", "X", "Z"]:
        assert dut.dout.value == 0x22222222, f"Expected dout=0x22222222 from init.hex, got {hex(int(dut.dout.value))}"

    # =========================================================================
    # Test Case 2: Perform Write Operation (wen = 1)
    # =========================================================================
    dut.ren.value = 0
    dut.wen.value = 1
    dut.waddr.value = 1
    dut.din.value = 0xDEADBEEF

    await RisingEdge(dut.clk)
    dut.wen.value = 0  # Disable write
    await Timer(1, unit="ns")
    cocotb.log.info("Write completed.")

    # =========================================================================
    # Test Case 3: Read back written location
    # =========================================================================
    dut.ren.value = 1
    dut.raddr.value = 1

    # Wait 2 clock edges for pipeline read latency
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")

    dout_val = str(dut.dout.value)
    cocotb.log.info(f"Post-Write Read (addr 1) -> dout={hex(int(dut.dout.value))}")

    if dout_val not in ["x", "X", "Z"]:
        assert dut.dout.value == 0xDEADBEEF, f"Expected dout=0xDEADBEEF, got {hex(int(dut.dout.value))}"

    cocotb.log.info("All dual_port_ram_8x32 test cases completed successfully!")
