.. _datasheet_simple_registers_signal_gen_clock_divider:

Configurable Clock Divider (clock_divider)
------------------------------------------

Introduction
~~~~~~~~~~~~

The ``clock_divider`` module provides a configurable frequency division circuit driven by an input clock (`clk_in`). 
It utilizes a parameterized counter width (`CLK_DIVIDER_SIZE`) to divide the incoming clock frequency and produce a toggled output clock (`clk_out`).

Source Codes
~~~~~~~~~~~~

See details in ``simple_registers/signal_gen/clock_divider``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/clock_divider.svg
  :width: 70%
  :alt: Configurable Clock Divider schematic

  Configurable Clock Divider schematic

Parameters
~~~~~~~~~~~

.. list-table:: Module Parameters
  :header-rows: 1
  :class: longtable

  * - Parameter
    - Default
    - Description
  * - ``CLK_DIVIDER_SIZE``
    - ``8``
    - Bit width of the internal counter, determining the division factor.

Performance & Resource Utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Expect minimal resource utilization, scaling linearly with the counter bit width.

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
  * - Clock Divider (8-bit)
    - 1
    - 1
    - 8
    - 8
    - 0
    - 0
    - 0
