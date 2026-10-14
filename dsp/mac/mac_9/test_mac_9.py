import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mac_9(dut):
    """Cocotb testbench for combinatorial mac_9 module"""
    
    # Test vector list: (a, b, c)
    # DATA_WIDTH = 9, so values range from 0 to 511
    test_vectors = [
        (1, 1, 0),
        (15, 20, 10),
        (100, 200, 50),
        (255, 255, 128),
        (350, 100, 250),
        (511, 511, 511)
    ]
    
    dut._log.info("Starting combinatorial mac_9 verification...")
    
    for a_val, b_val, c_val in test_vectors:
        # Drive inputs
        dut.a.value = a_val
        dut.b.value = b_val
        dut.c.value = c_val
        
        # Allow small propagation delay for combinatorial logic to settle
        await Timer(1, units="ns")
        
        # Calculate expected output: (a * b + c) wrapped to DATA_WIDTH (9 bits -> mask 0x1FF)
        expected = (a_val * b_val + c_val) & 0x1FF
        
        try:
            actual = int(dut.out.value)
        except ValueError:
            actual = 0
            
        dut._log.info(f"Inputs a={a_val}, b={b_val}, c={c_val} -> Expected out={expected}, Got out={actual}")
        assert actual == expected, f"Mismatch: expected {expected}, got {actual}"
        
    dut._log.info("All combinatorial mac_9 tests passed successfully!")
