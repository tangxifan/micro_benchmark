.. _datasheet_timer8_24clk_async_reset:

Timer 8-bit 24 Clock Asynchronous Reset
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests flip-flop/register networks and clock routing scalability across **24 independent clock domains** in FPGAs.
The design generates 24 independent 8-bit countdown timers with configurable load periods, enable signals, and timer complete flags.

Source codes
~~~~~~~~~~~~

See details in ``timers/timer8_24clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

This design is a 24-clock version of the illustrative schematic in :numref:`fig_timer8_24clk_async_reset`

.. _fig_timer8_24clk_async_reset:

.. figure:: ./figures/timer8_Nclk_async_reset.svg
  :width: 70%
  :alt: Timer 8-bit 24 Clock Asynchronous Reset schematic

  Timer 8-bit 24 Clock Asynchronous Reset schematic

Performance
~~~~~~~~~~~

Expect to consume 216 flip-flops and minimal LUT logic of an FPGA.

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
    - 217
    - 216
    - 384
    - 216
    - 0
    - 0
    - 0
