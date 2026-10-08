.. _datasheet_mult_8_pipelined_8clk:

8-bit Pipelined Multiplier 8 Clock
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests DSP blocks, multiplier logic, and clock domain routing across **8 independent clock domains** in FPGAs.
The design instantiates 8 parallel 8-bit pipelined multipliers with registered input operands and registered output products.

Source codes
~~~~~~~~~~~~

See details in ``mult/mult_8_pipelined_8clk``

Block Diagram
~~~~~~~~~~~~~

This design is a 8-clock version of the illustrative schematic in :numref:`fig_mult_8_pipelined_8clk`

.. _fig_mult_8_pipelined_8clk

.. figure:: ./figures/mult_8_pipelined_Nclk.svg
  :width: 70%
  :alt: 8-bit Pipelined Multiplier 8 Clock schematic

  8-bit Pipelined Multiplier 8 Clock schematic

Performance
~~~~~~~~~~~

Expect to consume 8 DSP blocks (or equivalent LUT multiplier logic) and 256 flip-flops.

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
  * - 8-Clock
    - 136
    - 128
    - 320
    - 256
    - 0
    - 8
    - 0
