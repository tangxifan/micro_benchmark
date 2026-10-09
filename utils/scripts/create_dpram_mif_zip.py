import os
import zipfile

# Multi-clock domain variants
variants = [4, 8, 16, 24, 32]

# Parameterized Core dual-port RAM array
verilog_core_code = """///////////////////////////////////////////
//  Functionality: Parameterized N-Instance Dual-Port RAM (8x16) with Memory Preload
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_Nclk #(
    parameter N = 4,
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire [N-1:0]      clk_a,
    input  wire [N-1:0]      we_a,
    input  wire [N*8-1:0]    addr_a,
    input  wire [N*16-1:0]   din_a,
    
    input  wire [N-1:0]      clk_b,
    input  wire [N*8-1:0]    addr_b,
    output reg  [N*16-1:0]   dout_b
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_dpram
            reg [15:0] ram [0:255];

            initial begin
                if (RAM_INIT_FILE != "") begin
                    $readmemh(RAM_INIT_FILE, ram);
                end
            end

            // Port A - Synchronous Write
            always @(posedge clk_a[i]) begin
                if (we_a[i]) begin
                    ram[addr_a[i*8 +: 8]] <= din_a[i*16 +: 16];
                end
            end

            // Port B - Synchronous Read
            always @(posedge clk_b[i]) begin
                dout_b[i*16 +: 16] <= ram[addr_b[i*8 +: 8]];
            end
        end
    endgenerate

endmodule
"""

# Universal cocotb Verification for Multi-Clock DPRAM
cocotb_tb_code = """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_dpram_n_clk(dut):
    \"\"\"Verification for N-instance Dual-Port RAM.\"\"\"
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk_a.value)
    dut._log.info(f"Testing {num_clks}-instance dual-port RAM...")

    # Start separate clocks for write (clk_a) and read (clk_b) ports
    for i in range(num_clks):
        cocotb.start_soon(Clock(dut.clk_a[i], 10 + i * 2, units="ns").start())
        cocotb.start_soon(Clock(dut.clk_b[i], 15 + i * 2, units="ns").start())

    dut.we_a.value = 0
    await Timer(50, units="ns")

    # Test Write -> Read sequence for each DPRAM instance
    for i in range(num_clks):
        test_addr = 0x10 + i
        test_data = 0xA5A5 ^ (i * 0x1111)

        # Write data on Port A
        addr_a_val = test_addr << (i * 8)
        din_a_val = test_data << (i * 16)
        we_a_val = 1 << i

        dut.addr_a.value = addr_a_val
        dut.din_a.value = din_a_val
        dut.we_a.value = we_a_val

        await RisingEdge(dut.clk_a[i])
        await Timer(1, units="ns")
        dut.we_a.value = 0

        # Read data back on Port B
        addr_b_val = test_addr << (i * 8)
        dut.addr_b.value = addr_b_val

        await RisingEdge(dut.clk_b[i])
        await Timer(1, units="ns")

        actual_dout = (int(dut.dout_b.value) >> (i * 16)) & 0xFFFF
        assert actual_dout == test_data, f"Instance {i} mismatch: expected {hex(test_data)}, got {hex(actual_dout)}"

    dut._log.info("All dual-port RAM instances verified successfully!")
"""


def generate_svg(n_clocks):
    height = 120 + (n_clocks * 40)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 {height}" width="100%" height="100%">
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

  <rect x="220" y="20" width="410" height="{height - 40}" rx="8" class="box"/>
  <text x="425" y="45" text-anchor="middle" class="text-title">dual_port_ram_8x16_mif_{n_clocks}clk</text>
"""
    for i in range(n_clocks):
        y_pos = 60 + (i * 40)
        svg += f"""  <rect x="260" y="{y_pos}" width="330" height="32" rx="4" class="subbox"/>
  <text x="425" y="{y_pos + 20}" text-anchor="middle" class="text-sub">DPRAM 256x16 [{i}] (clk_a[{i}] / clk_b[{i}])</text>
  
  <!-- Port A Inputs -->
  <path d="M 80 {y_pos + 6} L 260 {y_pos + 6}" class="line" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 10}" text-anchor="end" class="text-port">clk_a[{i}], we_a[{i}]</text>
  <path d="M 80 {y_pos + 16} L 260 {y_pos + 16}" class="bus" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 20}" text-anchor="end" class="text-port">addr_a[{i}] [7:0], din_a[{i}] [15:0]</text>
  
  <!-- Port B Read -->
  <path d="M 80 {y_pos + 26} L 260 {y_pos + 26}" class="line" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 30}" text-anchor="end" class="text-port">clk_b[{i}], addr_b[{i}] [7:0]</text>
  <path d="M 590 {y_pos + 16} L 770 {y_pos + 16}" class="bus" marker-end="url(#arrow)"/>
  <text x="775" y="{y_pos + 20}" text-anchor="start" class="text-port">dout_b[{i}] [15:0]</text>
"""
    svg += "</svg>"
    return svg


def generate_rst(n_clocks):
    return f""".. _datasheet_dual_port_ram_8x16_mif_{n_clocks}clk:

Dual-Port RAM 8x16 MIF {n_clocks} Clock
----------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing, memory initialization (`.mif` files), and multi-clock routing scalability across **{n_clocks} dual-port memory instances**.
The module instantiates {n_clocks} independent 256x16 dual-port RAMs, each with its own write clock (`clk_a`) and read clock (`clk_b`).

Source codes
~~~~~~~~~~~~

See details in ``ram/dual_port_ram_8x16_mif_{n_clocks}clk``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/dual_port_ram_8x16_mif_{n_clocks}clk.svg
  :width: 70%
  :alt: Dual-Port RAM 8x16 MIF {n_clocks} Clock schematic

  Dual-Port RAM 8x16 MIF {n_clocks} Clock schematic

Performance
~~~~~~~~~~~

Expect to consume {n_clocks} BRAM primitives (or equivalent LUT RAM logic).

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
    - {n_clocks * 34}
    - {n_clocks * 16}
    - {n_clocks * 16}
    - {n_clocks * 16}
    - 0
    - 0
    - {n_clocks}
"""


# Sample MIF memory file
mif_sample = """0000
1111
2222
3333
4444
5555
6666
7777
"""

# Build Zip Package
zip_filename = "dual_port_ram_8x16_mif_multi_clk.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for n in variants:
        folder = f"dual_port_ram_8x16_mif_{n}clk"

        wrapper_verilog = f"""///////////////////////////////////////////
// Functionality: {n}-Clock Domain 256x16 Dual-Port RAM Array
///////////////////////////////////////////

module dual_port_ram_8x16_mif_{n}clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input [{n-1}:0] clk_a,
    input [{n-1}:0] we_a,
    input [{n*8-1}:0] addr_a,
    input [{n*16-1}:0] din_a,
    
    input [{n-1}:0] clk_b,
    input [{n*8-1}:0] addr_b,
    output [{n*16-1}:0] dout_b
);

    dual_port_ram_8x16_mif_Nclk #(
        .N({n}),
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) core (
        .clk_a(clk_a),
        .we_a(we_a),
        .addr_a(addr_a),
        .din_a(din_a),
        .clk_b(clk_b),
        .addr_b(addr_b),
        .dout_b(dout_b)
    );

endmodule
"""

        makefile_code = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/dual_port_ram_8x16_mif_Nclk.v
VERILOG_SOURCES += $(PWD)/dual_port_ram_8x16_mif_{n}clk.v

TOPLEVEL = dual_port_ram_8x16_mif_{n}clk
MODULE   = test_dual_port_ram_8x16_mif_{n}clk

include $(shell cocotb-config --makefiles)/sim.makefile
"""

        zipf.writestr(
            f"{folder}/dual_port_ram_8x16_mif_Nclk.v", verilog_core_code
        )
        zipf.writestr(
            f"{folder}/dual_port_ram_8x16_mif_{n}clk.v", wrapper_verilog
        )
        zipf.writestr(
            f"{folder}/test_dual_port_ram_8x16_mif_{n}clk.py", cocotb_tb_code
        )
        zipf.writestr(f"{folder}/Makefile", makefile_code)
        zipf.writestr(f"{folder}/ram.mif", mif_sample)
        zipf.writestr(
            f"{folder}/doc/dual_port_ram_8x16_mif_{n}clk.rst", generate_rst(n)
        )
        zipf.writestr(
            f"{folder}/doc/figures/dual_port_ram_8x16_mif_{n}clk.svg",
            generate_svg(n),
        )

print(f"Archive successfully generated at: {os.path.abspath(zip_filename)}")