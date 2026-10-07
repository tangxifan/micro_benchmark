import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_mult_8_pipelined_n_clk(dut):
    """Universal verification for N-clock 8-bit pipelined multipliers."""
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk.value)
    dut._log.info(f"Testing {num_clks}-clock domain pipelined multiplier...")

    # Start clocks with varying periods across domains
    for i in range(num_clks):
        period = 10 + (i * 2)
        cocotb.start_soon(Clock(dut.clk[i], period, units="ns").start())

    # Set test operands across all domains
    a_val = 0
    b_val = 0
    expected_products = []

    for i in range(num_clks):
        op_a = 12 + i
        op_b = 5 + i
        expected_products.append(op_a * op_b)
        a_val |= (op_a << (i * 8))
        b_val |= (op_b << (i * 8))

    dut.a.value = a_val
    dut.b.value = b_val

    # Verify 2-stage pipeline delay (2 clock cycles per domain)
    for i in range(num_clks):
        dut._log.info(f"Checking pipeline response for domain {i}...")
        
        # Cycle 1: Input registered
        await RisingEdge(dut.clk[i])
        await Timer(1, units="ns")
        
        # Cycle 2: Output registered
        await RisingEdge(dut.clk[i])
        await Timer(1, units="ns")
        
        actual_p = (int(dut.p.value) >> (i * 16)) & 0xFFFF
        expected_p = expected_products[i]
        assert actual_p == expected_p, f"Domain {i} mismatch: expected {expected_p}, got {actual_p}"

    dut._log.info("All pipelined multiplier domains verified successfully!")
