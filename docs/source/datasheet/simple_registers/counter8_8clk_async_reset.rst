.. _datasheet_counter8_8clk_async_reset:

Counter 8-bit 8 Clock Asynchronous Reset
--------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests flip-flop/register networks and clock routing scalability across **8 independent clock domains** in FPGAs.

Source codes
~~~~~~~~~~~~

See details in ``counters/counter8_8clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/counter8_8clk_async_reset.svg
  :width: 70%
  :alt: Counter 8-bit 8 Clock Asynchronous Reset schematic

  Counter 8-bit 8 Clock Asynchronous Reset schematic

Performance
~~~~~~~~~~~

Expect to consume 64 flip-flops and minimal LUT logic of an FPGA.

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
    - 9
    - 64
    - 64
    - 64
    - 0
    - 0
    - 0
