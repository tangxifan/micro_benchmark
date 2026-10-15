import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_asyn_spram_functional(dut):
    """Test bench for 4x1 asynchronous read single-port RAM."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize control and input signals
    dut.wr_en.value = 0
    dut.addr_0.value = 0
    dut.addr_1.value = 0
    dut.d_in.value = 0

    # Wait for initial synchronization
    await RisingEdge(dut.clk)

    # Define test patterns to write into the 4 locations
    test_data = [1, 0, 1, 1]

    cocotb.log.info("Starting memory write operations...")
    for addr in range(4):
        await RisingEdge(dut.clk)
        dut.wr_en.value = 1
        dut.addr_0.value = addr & 1
        dut.addr_1.value = (addr >> 1) & 1
        dut.d_in.value = test_data[addr]

    # Disable write enable after writing all values
    await RisingEdge(dut.clk)
    dut.wr_en.value = 0

    cocotb.log.info("Verifying asynchronous read operations...")
    for addr in range(4):
        # Change address asynchronously (without waiting for clock edge)
        dut.addr_0.value = addr & 1
        dut.addr_1.value = (addr >> 1) & 1

        # Wait a short combinatorial propagation delay
        await Timer(1, units="ns")

        # Check if output matches expected value
        actual_val = int(dut.d_out.value)
        expected_val = test_data[addr]

        assert (
            actual_val == expected_val
        ), f"Mismatch at address {addr}: expected {expected_val}, got {actual_val}"

        cocotb.log.info(f"Address {addr}: Data verified correctly as {actual_val}")

    cocotb.log.info("All SPRAM tests passed successfully!")
