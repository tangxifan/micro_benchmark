.. _datasheet_counter8_32clk_async_reset:

Counter 8-bit 32 Clock Asynchronous Reset
--------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests flip-flop/register networks and clock routing scalability across **32 independent clock domains** in FPGAs.

Source codes
~~~~~~~~~~~~

See details in ``counters/counter8_32clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

This design is a 32-clock version of the illustrative schematic in :numref:`fig_counter8_32clk_async_reset`

.. _fig_counter8_32clk_async_reset

.. figure:: ./figures/counter8_Nclk_async_reset.svg
  :width: 70%
  :alt: Counter 8-bit 32 Clock Asynchronous Reset schematic

  Counter 8-bit 32 Clock Asynchronous Reset schematic

Performance
~~~~~~~~~~~

Expect to consume 256 flip-flops and minimal LUT logic of an FPGA.

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
  * - 32-Clock
    - 33
    - 256
    - 256
    - 256
    - 0
    - 0
    - 0
