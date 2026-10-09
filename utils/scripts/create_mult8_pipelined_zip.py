import os
import zipfile

# Multi-clock variants to generate
variants = [4, 8, 16, 24, 32]

# Parameterized Multi-Clock 8-bit Pipelined Multiplier Core
verilog_core_code = """///////////////////////////////////////////
//  Functionality: Parameterized N-Clock 8-bit Pipelined Multiplier
//  Author:        Xifan Tang
////////////////////////////////////////

module mult_8_pipelined_Nclk #(
    parameter N = 4
)(
    input  wire [N-1:0]     clk,
    input  wire [N*8-1:0]   a,
    input  wire [N*8-1:0]   b,
    output reg  [N*16-1:0]  p
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_mult
            // Stage 1 Pipeline Registers
            reg [7:0] a_reg;
            reg [7:0] b_reg;

            always @(posedge clk[i]) begin
                a_reg <= a[i*8 +: 8];
                b_reg <= b[i*8 +: 8];
            end

            // Stage 2 Pipeline Output Register
            always @(posedge clk[i]) begin
                p[i*16 +: 16] <= a_reg * b_reg;
            end
        end
    endgenerate

endmodule
"""

# Universal cocotb Verification for Pipelined Multipliers
cocotb_tb_code = """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_mult_8_pipelined_n_clk(dut):
    \"\"\"Universal verification for N-clock 8-bit pipelined multipliers.\"\"\"
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
"""


def generate_svg(n_clocks):
    height = 120 + (n_clocks * 40)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {height}" width="100%" height="100%">
  <defs>
    <style>
      .box {{ fill: #f8f9fa; stroke: #212529; stroke-width: 2; }}
      .subbox {{ fill: #ffffff; stroke: #495057; stroke-dasharray: 4; stroke-width: 1.5; }}
      .text-title {{ font-family: sans-serif; font-weight: bold; font-size: 16px; fill: #212529; }}
      .text-sub {{ font-family: sans-serif; font-weight: bold; font-size: 11px; fill: #343a40; }}
      .text-port {{ font-family: monospace; font-size: 11px; fill: #212529; }}
      .line {{ stroke: #212529; stroke-width: 1.5; fill: none; }}
      .bus {{ stroke: #212529; stroke-width: 3; fill: none; }}
      .arrow {{ fill: #212529; }}
    </style>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" class="arrow"/>
    </marker>
  </defs>

  <rect x="200" y="20" width="400" height="{height - 40}" rx="8" class="box"/>
  <text x="400" y="45" text-anchor="middle" class="text-title">mult_8_pipelined_{n_clocks}clk</text>
"""
    for i in range(n_clocks):
        y_pos = 60 + (i * 40)
        svg += f"""  <rect x="240" y="{y_pos}" width="320" height="32" rx="4" class="subbox"/>
  <text x="400" y="{y_pos + 20}" text-anchor="middle" class="text-sub">8x8 Pipelined Multiplier (clk[{i}])</text>
  <path d="M 80 {y_pos + 8} L 240 {y_pos + 8}" class="bus" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 12}" text-anchor="end" class="text-port">a[{i}] [7:0]</text>
  <path d="M 80 {y_pos + 16} L 240 {y_pos + 16}" class="bus" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 20}" text-anchor="end" class="text-port">b[{i}] [7:0]</text>
  <path d="M 80 {y_pos + 24} L 240 {y_pos + 24}" class="line" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 28}" text-anchor="end" class="text-port">clk[{i}]</text>
  <path d="M 560 {y_pos + 16} L 720 {y_pos + 16}" class="bus" marker-end="url(#arrow)"/>
  <text x="725" y="{y_pos + 20}" text-anchor="start" class="text-port">p[{i}] [15:0]</text>
"""
    svg += "</svg>"
    return svg


def generate_rst(n_clocks):
    return f""".. _datasheet_mult_8_pipelined_{n_clocks}clk:

8-bit Pipelined Multiplier {n_clocks} Clock
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests DSP blocks, multiplier logic, and clock domain routing across **{n_clocks} independent clock domains** in FPGAs.
The design instantiates {n_clocks} parallel 8-bit pipelined multipliers with registered input operands and registered output products.

Source codes
~~~~~~~~~~~~

See details in ``mult/mult_8_pipelined_{n_clocks}clk``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/mult_8_pipelined_{n_clocks}clk.svg
  :width: 70%
  :alt: 8-bit Pipelined Multiplier {n_clocks} Clock schematic

  8-bit Pipelined Multiplier {n_clocks} Clock schematic

Performance
~~~~~~~~~~~

Expect to consume {n_clocks} DSP blocks (or equivalent LUT multiplier logic) and {n_clocks * 32} flip-flops.

.. list-table:: Estimated Resource Utilization
  :header-rows: 1
  :class: longtable

  * - Benchmark
    - Inputs
    - Outputs
    - LUT5
    - FF
    - Carry
    - DSP
    - BRAM
  * - {n_clocks}-Clock
    - {n_clocks * 17}
    - {n_clocks * 16}
    - {n_clocks * 40}
    - {n_clocks * 32}
    - 0
    - {n_clocks}
    - 0
"""


# Generate ZIP Bundle
zip_filename = "mult_8_pipelined_multi_clk.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for n in variants:
        folder = f"mult_8_pipelined_{n}clk"

        # Discrete Top Module Verilog Wrapper
        wrapper_verilog = f"""///////////////////////////////////////////
// Functionality: {n}-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_{n}clk (
    input [{n-1}:0] clk,
    input [{n*8-1}:0] a,
    input [{n*8-1}:0] b,
    output [{n*16-1}:0] p
);

    mult_8_pipelined_Nclk #(.N({n})) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
"""

        # Makefile
        makefile_code = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/mult_8_pipelined_Nclk.v
VERILOG_SOURCES += $(PWD)/mult_8_pipelined_{n}clk.v

TOPLEVEL = mult_8_pipelined_{n}clk
MODULE   = test_mult_8_pipelined_{n}clk

include $(shell cocotb-config --makefiles)/sim.makefile
"""

        # Write files into ZIP
        zipf.writestr(f"{folder}/mult_8_pipelined_Nclk.v", verilog_core_code)
        zipf.writestr(f"{folder}/mult_8_pipelined_{n}clk.v", wrapper_verilog)
        zipf.writestr(
            f"{folder}/test_mult_8_pipelined_{n}clk.py", cocotb_tb_code
        )
        zipf.writestr(f"{folder}/Makefile", makefile_code)
        zipf.writestr(
            f"{folder}/doc/mult_8_pipelined_{n}clk.rst", generate_rst(n)
        )
        zipf.writestr(
            f"{folder}/doc/figures/mult_8_pipelined_{n}clk.svg", generate_svg(n)
        )

print(f"Archive successfully created: {os.path.abspath(zip_filename)}")