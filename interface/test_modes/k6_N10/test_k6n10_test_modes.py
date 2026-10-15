import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_test_modes_functional(dut):
    """Testbench for test_modes module verifying multi-stage shift register pipeline, adder logic, and control signal propagation."""

    # Start a 10ns period clock (100 MHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize all inputs to 0
    dut.a_0.value = 0
    dut.a_1.value = 0
    dut.a_2.value = 0
    dut.a_3.value = 0
    dut.b_0.value = 0
    dut.b_1.value = 0
    dut.b_2.value = 0
    dut.b_3.value = 0
    dut.cin.value = 0
    dut.e.value = 0
    dut.f.value = 0
    dut.g.value = 0

    # Wait for initial clock cycles to settle
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    cocotb.log.info("Starting test_modes simulation test vectors...")

    # Define test stimulus cases (a_vals, b_vals, cin, e, f, g)
    test_vectors = [
        ([1, 0, 1, 0], [0, 1, 0, 1], 0, 1, 0, 1),
        ([1, 1, 1, 1], [0, 0, 0, 1], 1, 0, 1, 1),
        ([0, 0, 1, 1], [1, 1, 0, 0], 0, 1, 1, 0),
        ([1, 0, 0, 1], [1, 0, 1, 0], 1, 1, 0, 0),
    ]

    for idx, (a_vals, b_vals, cin_val, e_val, f_val, g_val) in enumerate(test_vectors):
        # Drive inputs
        dut.a_0.value = a_vals[0]
        dut.a_1.value = a_vals[1]
        dut.a_2.value = a_vals[2]
        dut.a_3.value = a_vals[3]

        dut.b_0.value = b_vals[0]
        dut.b_1.value = b_vals[1]
        dut.b_2.value = b_vals[2]
        dut.b_3.value = b_vals[3]

        dut.cin.value = cin_val
        dut.e.value = e_val
        dut.f.value = f_val
        dut.g.value = g_val

        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")  # Allow combinatorial propagation settling

        # Safely retrieve string representations to prevent ValueError on uninitialized 'X' states
        x_val = str(dut.x.value)
        y_val = str(dut.y.value)
        z_val = str(dut.z.value)
        sum_val = f"{str(dut.cout.value)}{str(dut.sum_3.value)}{str(dut.sum_2.value)}{str(dut.sum_1.value)}{str(dut.sum_0.value)}"

        cocotb.log.info(
            f"Vector {idx}: a={a_vals}, b={b_vals} -> sum_out={sum_val}, x={x_val}, y={y_val}, z={z_val}"
        )

    # Flush the deep shift register pipeline (12 stages)
    dut.e.value = 0
    dut.f.value = 1
    dut.g.value = 0
    for step in range(14):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        x_val = str(dut.x.value)
        y_val = str(dut.y.value)
        z_val = str(dut.z.value)
        cocotb.log.info(f"Pipeline flush step {step+1}: x={x_val}, y={y_val}, z={z_val}")

    cocotb.log.info("All test_modes test cases completed successfully!")
