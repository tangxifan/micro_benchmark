.. _datasheet_mult_8_pipelined_Nclk:

8-bit Pipelined Multiplier N-Clock
----------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests DSP blocks, multiplier logic, and clock domain routing across **N independent clock domains** in FPGAs.
The design instantiates **N** parallel 8-bit pipelined multipliers with registered input operands and registered output products.

Source codes
~~~~~~~~~~~~

See details in

- ``mult/mult_8_pipelined_4clk``
- ``mult/mult_8_pipelined_8clk``
- ``mult/mult_8_pipelined_16clk``
- ``mult/mult_8_pipelined_24clk``
- ``mult/mult_8_pipelined_32clk``

Block Diagram
~~~~~~~~~~~~~

.. _fig_mult_8_pipelined_Nclk:

.. figure:: ./figures/mult_8_pipelined_Nclk.svg
  :width: 70%
  :alt: 8-bit Pipelined Multiplier N-Clock schematic

  8-bit Pipelined Multiplier N-Clock schematic

Performance
~~~~~~~~~~~

Expect to consume N DSP blocks (or equivalent LUT multiplier logic) and 128 flip-flops.

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
  * - 4-Clock
    - 68
    - 64
    - 160
    - 128
    - 0
    - 4
    - 0
  * - 8-Clock
    - 136
    - 128
    - 320
    - 256
    - 0
    - 8
    - 0
  * - 16-Clock
    - 272
    - 256
    - 640
    - 512
    - 0
    - 16
    - 0
  * - 24-Clock
    - 408
    - 384
    - 960
    - 768
    - 0
    - 24
    - 0
  * - 32-Clock
    - 544
    - 512
    - 1280
    - 1024
    - 0
    - 32
    - 0
