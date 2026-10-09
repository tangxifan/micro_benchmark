.. _datasheet_counter8_4clk_async_reset:

Counter 8-bit N-Clock Asynchronous Reset
----------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark is designed to test the flip-flop/registers across multiple clock domains in FPGAs.
This code generates **N** independent 8-bit counters, each operating on its own clock signal (`clk0`, `clk1`, `clk2`, and `clkN`). All four counters share a common active-high asynchronous reset input. When the reset signal is asserted high, all counter outputs are immediately cleared to 0 regardless of the clock transitions.

Source codes
~~~~~~~~~~~~

See details in 

- ``counters/counter8_4clk_async_reset``
- ``counters/counter8_8clk_async_reset``
- ``counters/counter8_16clk_async_reset``
- ``counters/counter8_24clk_async_reset``
- ``counters/counter8_32clk_async_reset``

Block Diagram
~~~~~~~~~~~~~

.. _fig_counter8_Nclk_async_reset:

.. figure:: ./figures/counter8_Nclk_async_reset.svg
  :width: 60%
  :alt: Counter 8-bit N Clock Asynchronous Reset schematic

  Counter 8-bit N Clock Asynchronous Reset schematic


Performance
~~~~~~~~~~~

Expect to consume only 32 flip-flops and minimal LUT logic of an FPGA.
It can evaluate the routability and performance of multi-clock networks and flip-flop asynchronous reset trees.

.. warning:: The following resource utilization is just an estimation! Different tools in different versions may result differently.

.. list-table:: Estimated resource Utilization
  :header-rows: 1
  :class: longtable

  * - Tool/Resource
    - Inputs
    - Outputs
    - LUT5
    - FF
    - Carry
    - DSP
    - BRAM
  * - General
    - 5
    - 32
    - 32
    - 32
    - 0
    - 0
    - 0
  * - 8-Clock
    - 9
    - 64
    - 64
    - 64
    - 0
    - 0
    - 0
  * - 16-Clock
    - 17
    - 128
    - 128
    - 128
    - 0
    - 0
    - 0
  * - 24-Clock
    - 25
    - 192
    - 192
    - 192
    - 0
    - 0
    - 0
  * - 32-Clock
    - 33
    - 256
    - 256
    - 256
    - 0
    - 0
    - 0
