import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


def set_signals(dut, addr_val, d_in_val, wr_en_val):
    """Helper function to drive bit-flattened address inputs for syn_spram_4x1."""
    dut.addr_0.value = addr_val & 1
    dut.addr_1.value = (addr_val >> 1) & 1
    dut.d_in.value = d_in_val
    dut.wr_en.value = wr_en_val


@cocotb.test()
async def test_syn_spram_4x1_functional(dut):
    """Testbench for syn_spram_4x1 verifying synchronous write and read operations[cite: 6]."""

    # Start a 10ns period clock (100 MHz) using modern 'unit' argument
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize signals
    set_signals(dut, addr_val=0, d_in_val=0, wr_en_val=0)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Define test data: write to all 4 addresses (0 to 3)
    test_data = [(0, 1), (1, 0), (2, 1), (3, 1)]

    cocotb.log.info("Starting synchronous write operations[cite: 6]...")

    for addr, val in test_data:
        set_signals(dut, addr_val=addr, d_in_val=val, wr_en_val=1)
        await RisingEdge(dut.clk)

    # Disable write enable
    set_signals(dut, addr_val=0, d_in_val=0, wr_en_val=0)
    await RisingEdge(dut.clk)

    cocotb.log.info("Starting read and verification operations[cite: 6]...")

    # Read back and verify each address
    for addr, expected_val in test_data:
        # Address inputs are applied; since read is asynchronous combinational feeding a reg,
        # setting the address updates 'tmp' which is registered on the next clock edge.
        set_signals(dut, addr_val=addr, d_in_val=0, wr_en_val=0)

        # Wait for the rising edge where d_out captures the combinatorial value 'tmp'
        await RisingEdge(dut.clk)

        # Allow small delta for output to settle
        await Timer(1, unit="ns")

        actual_val = int(dut.d_out.value)
        assert (
            actual_val == expected_val
        ), f"Mismatch at address {addr}: expected {expected_val}, got {actual_val}"

        cocotb.log.info(f"Address {addr} verified successfully: got {actual_val}[cite: 6]")

    cocotb.log.info("All syn_spram_4x1 tests passed successfully[cite: 6]!")
