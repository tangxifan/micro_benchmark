.. _datasheet_mult_8_pipelined_24clk:

8-bit Pipelined Multiplier 24 Clock
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests DSP blocks, multiplier logic, and clock domain routing across **24 independent clock domains** in FPGAs.
The design instantiates 24 parallel 8-bit pipelined multipliers with registered input operands and registered output products.

Source codes
~~~~~~~~~~~~

See details in ``mult/mult_8_pipelined_24clk``

Block Diagram
~~~~~~~~~~~~~

This design is a 24-clock version of the illustrative schematic in :numref:`fig_mult_8_pipelined_24clk`

.. _fig_mult_8_pipelined_24clk:

.. figure:: ./figures/mult_8_pipelined_Nclk.svg
  :width: 70%
  :alt: 8-bit Pipelined Multiplier 24 Clock schematic

  8-bit Pipelined Multiplier 24 Clock schematic

Performance
~~~~~~~~~~~

Expect to consume 24 DSP blocks (or equivalent LUT multiplier logic) and 768 flip-flops.

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
  * - 24-Clock
    - 408
    - 384
    - 960
    - 768
    - 0
    - 24
    - 0
