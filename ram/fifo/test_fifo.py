import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_fifo_functional(dut):
    """Testbench for synchronous FIFO module."""
    
    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize control and input signals
    dut.reset.value = 1
    dut.read.value = 0
    dut.write.value = 0
    dut.write_data.value = 0

    # Hold reset for a couple of cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.reset.value = 0
    await RisingEdge(dut.clk)

    # Verify initial empty state
    assert dut.empty.value == 1, "FIFO should be empty after reset"
    assert dut.full.value == 0, "FIFO should not be full after reset"
    cocotb.log.info("Reset and initial empty state verified successfully.")

    # Define test data sequence
    test_data = [0xA, 0x5, 0xC, 0x3, 0xF]

    cocotb.log.info("Starting sequential write operations...")
    for val in test_data:
        await RisingEdge(dut.clk)
        dut.write.value = 1
        dut.write_data.value = val

    # Disable write enable
    await RisingEdge(dut.clk)
    dut.write.value = 0

    cocotb.log.info("Starting sequential read and verification operations...")
    for expected_val in test_data:
        await RisingEdge(dut.clk)
        dut.read.value = 1
        
        # Wait for the read data to register and update output
        await RisingEdge(dut.clk)
        
        # Check value
        actual_val = int(dut.read_data.value)
        assert actual_val == expected_val, \
            f"Data mismatch: expected {hex(expected_val)}, got {hex(actual_val)}"
        
        cocotb.log.info(f"Verified data: {hex(actual_val)}")

    # Stop reading
    await RisingEdge(dut.clk)
    dut.read.value = 0

    # Verify FIFO is empty again
    await RisingEdge(dut.clk)
    assert dut.empty.value == 1, "FIFO should be empty after reading all items"
    
    cocotb.log.info("All FIFO tests passed successfully!")
