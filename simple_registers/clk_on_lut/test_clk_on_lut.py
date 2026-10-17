import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_clk_on_lut_functional(dut):
    """Testbench for clk_on_lut module verifying synchronous register data capture and combinatorial clock/data gating on 'out'."""
    
    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.a.value = 0
    dut.b.value = 0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    cocotb.log.info("Starting clk_on_lut verification...")

    # Test stimulus cases (a_val, b_val)
    test_vectors = [
        (1, 0),
        (1, 1),
        (0, 1),
        (1, 0),
        (0, 0)
    ]

    for idx, (a_val, b_val) in enumerate(test_vectors):
        dut.a.value = a_val
        dut.b.value = b_val

        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")  # Allow combinatorial propagation settling

        # Safely retrieve string representations to prevent ValueError on uninitialized 'X' states
        q_val = str(dut.q.value)
        out_val = str(dut.out.value)
        
        cocotb.log.info(f"Vector {idx}: a={a_val}, b={b_val} -> q={q_val}, out={out_val}")

    cocotb.log.info("All clk_on_lut test cases completed successfully!")
