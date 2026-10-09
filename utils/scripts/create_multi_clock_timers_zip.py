import os
import zipfile

# Variants to generate
variants = [4, 8, 16, 24, 32]

# Parameterized Multi-Clock 8-bit Timer Core
verilog_core_code = """///////////////////////////////////////////
//  Functionality: Parameterized N-Clock 8-bit Countdown Timer
//  Author:        Xifan Tang
////////////////////////////////////////

module timer8_Nclk_async_reset #(
    parameter N = 4
)(
    input  wire [N-1:0]     clk,
    input  wire             reset,
    input  wire [N-1:0]     en,
    input  wire [N*8-1:0]   period,
    output reg  [N*8-1:0]   count,
    output reg  [N-1:0]     timer_done
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_timer
            always @(posedge clk[i] or posedge reset) begin
                if (reset) begin
                    count[i*8 +: 8]      <= 8'h00;
                    timer_done[i]        <= 1'b0;
                end else if (en[i]) begin
                    if (count[i*8 +: 8] == 8'h00) begin
                        count[i*8 +: 8]  <= period[i*8 +: 8];
                        timer_done[i]    <= 1'b1;
                    end else begin
                        count[i*8 +: 8]  <= count[i*8 +: 8] - 1'b1;
                        timer_done[i]    <= 1'b0;
                    end
                end else begin
                    timer_done[i]        <= 1'b0;
                end
            end
        end
    endgenerate

endmodule
"""

# Universal cocotb Verification for Timers
cocotb_tb_code = """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_timer_n_clock(dut):
    \"\"\"Universal verification for N-clock 8-bit countdown timers.\"\"\"
    num_clks = int(dut.N.value) if hasattr(dut, "N") else len(dut.clk.value)
    dut._log.info(f"Testing {num_clks}-clock domain timer configuration...")

    for i in range(num_clks):
        period = 10 + (i * 2)
        cocotb.start_soon(Clock(dut.clk[i], period, units="ns").start())

    # 1. Assert Reset
    dut.reset.value = 1
    dut.en.value = 0
    dut.period.value = 0
    await Timer(50, units="ns")
    assert int(dut.count.value) == 0, "Reset count check failed"
    assert int(dut.timer_done.value) == 0, "Reset done check failed"

    # 2. De-assert Reset & Configure Timers
    dut.reset.value = 0
    await Timer(1, units="ns")

    # Set load period of 5 cycles for all domains
    period_val = 0
    for i in range(num_clks):
        period_val |= (5 << (i * 8))
    dut.period.value = period_val
    dut.en.value = (1 << num_clks) - 1  # Enable all timers

    # 3. Test Countdown and Done Pulse Execution
    for i in range(num_clks):
        dut._log.info(f"Checking countdown for timer domain {i}...")
        # Clock down from 5 to 0
        for step in range(5, -1, -1):
            await RisingEdge(dut.clk[i])
            await Timer(1, units="ns")
            curr_cnt = (int(dut.count.value) >> (i * 8)) & 0xFF
            done_bit = (int(dut.timer_done.value) >> i) & 0x1
            
            if step == 0:
                assert done_bit == 1, f"Domain {i} expected timer_done assertion"
            else:
                assert done_bit == 0, f"Domain {i} unexpected timer_done high"

    # 4. Mid-run Async Reset Test
    dut.reset.value = 1
    await Timer(5, units="ns")
    assert int(dut.count.value) == 0, "Mid-run async reset count failed"
    assert int(dut.timer_done.value) == 0, "Mid-run async reset done failed"
    dut.reset.value = 0
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
  <text x="400" y="45" text-anchor="middle" class="text-title">timer8_{n_clocks}clk_async_reset</text>
"""
    for i in range(n_clocks):
        y_pos = 60 + (i * 40)
        svg += f"""  <rect x="240" y="{y_pos}" width="320" height="32" rx="4" class="subbox"/>
  <text x="400" y="{y_pos + 20}" text-anchor="middle" class="text-sub">8-bit Timer (clk[{i}])</text>
  <path d="M 80 {y_pos + 16} L 240 {y_pos + 16}" class="line" marker-end="url(#arrow)"/>
  <text x="75" y="{y_pos + 20}" text-anchor="end" class="text-port">clk[{i}]</text>
  <path d="M 560 {y_pos + 10} L 720 {y_pos + 10}" class="bus" marker-end="url(#arrow)"/>
  <text x="725" y="{y_pos + 14}" text-anchor="start" class="text-port">count[{i}] [7:0]</text>
  <path d="M 560 {y_pos + 22} L 720 {y_pos + 22}" class="line" marker-end="url(#arrow)"/>
  <text x="725" y="{y_pos + 26}" text-anchor="start" class="text-port">timer_done[{i}]</text>
"""
    svg += f"""  <path d="M 80 {height - 20} L 160 {height - 20} L 160 76 L 240 76" class="line"/>
  <text x="75" y="{height - 16}" text-anchor="end" class="text-port">reset</text>
</svg>"""
    return svg


def generate_rst(n_clocks):
    return f""".. _datasheet_timer8_{n_clocks}clk_async_reset:

Timer 8-bit {n_clocks} Clock Asynchronous Reset
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests flip-flop/register networks and clock routing scalability across **{n_clocks} independent clock domains** in FPGAs.
The design generates {n_clocks} independent 8-bit countdown timers with configurable load periods, enable signals, and timer complete flags.

Source codes
~~~~~~~~~~~~

See details in ``timers/timer8_{n_clocks}clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/timer8_{n_clocks}clk_async_reset.svg
  :width: 70%
  :alt: Timer 8-bit {n_clocks} Clock Asynchronous Reset schematic

  Timer 8-bit {n_clocks} Clock Asynchronous Reset schematic

Performance
~~~~~~~~~~~

Expect to consume {n_clocks * 9} flip-flops and minimal LUT logic of an FPGA.

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
    - {n_clocks * 9 + 1}
    - {n_clocks * 9}
    - {n_clocks * 16}
    - {n_clocks * 9}
    - 0
    - 0
    - 0
"""


# Create Zip Archive
zip_filename = "timers_multi_clk.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for n in variants:
        folder = f"timer8_{n}clk_async_reset"

        # Discrete Top Module Verilog Wrapper
        wrapper_verilog = f"""///////////////////////////////////////////
// Functionality: {n}-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_{n}clk_async_reset (
    input [{n-1}:0] clk,
    input reset,
    input [{n-1}:0] en,
    input [{n*8-1}:0] period,
    output [{n*8-1}:0] count,
    output [{n-1}:0] timer_done
);

    timer8_Nclk_async_reset #(.N({n})) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
"""

        # Makefile
        makefile_code = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/timer8_Nclk_async_reset.v
VERILOG_SOURCES += $(PWD)/timer8_{n}clk_async_reset.v

TOPLEVEL = timer8_{n}clk_async_reset
MODULE   = test_timer8_{n}clk_async_reset

include $(shell cocotb-config --makefiles)/sim.makefile
"""

        # Write into ZIP bundle
        zipf.writestr(f"{folder}/timer8_Nclk_async_reset.v", verilog_core_code)
        zipf.writestr(f"{folder}/timer8_{n}clk_async_reset.v", wrapper_verilog)
        zipf.writestr(f"{folder}/test_timer8_{n}clk_async_reset.py", cocotb_tb_code)
        zipf.writestr(f"{folder}/Makefile", makefile_code)
        zipf.writestr(f"{folder}/doc/timer8_{n}clk_async_reset.rst", generate_rst(n))
        zipf.writestr(
            f"{folder}/doc/figures/timer8_{n}clk_async_reset.svg",
            generate_svg(n),
        )

print(f"Archive successfully created: {os.path.abspath(zip_filename)}")