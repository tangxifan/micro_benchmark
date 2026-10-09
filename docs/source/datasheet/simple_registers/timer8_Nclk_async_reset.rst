.. _datasheet_timer8_Nclk_async_reset:

Timer 8-bit N-Clock Asynchronous Reset
------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests flip-flop/register networks and clock routing scalability across **N independent clock domains** in FPGAs.
The design generates N independent 8-bit countdown timers with configurable load periods, enable signals, and timer complete flags.

Source codes
~~~~~~~~~~~~

See details in

- ``timers/timer8_4clk_async_reset``
- ``timers/timer8_8clk_async_reset``
- ``timers/timer8_16clk_async_reset``
- ``timers/timer8_24clk_async_reset``
- ``timers/timer8_32clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

.. _fig_timer8_Nclk_async_reset:

.. figure:: ./figures/timer8_Nclk_async_reset.svg
  :width: 70%
  :alt: Timer 8-bit N-Clock Asynchronous Reset schematic

  Timer 8-bit N-Clock Asynchronous Reset schematic

Performance
~~~~~~~~~~~

Expect to consume 36 flip-flops and minimal LUT logic of an FPGA.

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
    - 37
    - 36
    - 64
    - 36
    - 0
    - 0
    - 0
  * - 8-Clock
    - 73
    - 72
    - 128
    - 72
    - 0
    - 0
    - 0
  * - 16-Clock
    - 145
    - 144
    - 256
    - 144
    - 0
    - 0
    - 0
  * - 24-Clock
    - 217
    - 216
    - 384
    - 216
    - 0
    - 0
    - 0
  * - 32-Clock
    - 289
    - 288
    - 512
    - 288
    - 0
    - 0
    - 0
