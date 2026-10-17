.. _datasheet_simple_registers_rst_on_lut:

rst_on_lut
----------

Introduction
~~~~~~~~~~~~

The ``rst_on_lut`` module implements a register driven by combinational logic tied with an asynchronous reset signal. It features an asynchronously reset register (``q <= a`` when ``rst`` is active) alongside a combinatorial output branch ``out`` gated by an active-low reset term (``b & ~rst``). This benchmark evaluates FPGA logic mapping where control signals such as reset dual-purpose as inputs to adjacent Look-Up Table logic. 

Source codes
~~~~~~~~~~~~

See details in ``simple_registers/rst_on_lut_Nbit/rst_on_lut.v``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/rst_on_lut_schematic.svg
  :width: 70%
  :alt: rst_on_lut schematic

  rst_on_lut schematic

Performance
~~~~~~~~~~~

Expect to consume minimal FPGA resources (typically 1 LUT/gate and 1 Flip-Flop). The design analyzes resource utilization when asynchronous reset and control signals feed into surrounding combinational routing structures.

.. warning:: The following resource utilization is just an estimation! Different tools in different versions may result differently.

.. list-table:: Estimated Resource Utilization
  :header-rows: 1
  :class: longtable

  * - Tool/Resource
    - Inputs
    - Outputs
    - LUT4
    - FF
    - Carry
    - DSP
    - BRAM
  * - General
    - 4
    - 2
    - 1
    - 1
    - 0
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: rst_on_lut Top-Level Ports

  +------------+-------+-----------+------------------------------------+
  | Port       | Width | Direction | Description                        |
  +------------+-------+-----------+------------------------------------+
  | rst        | 1     | Input     | Asynchronous reset input |
  +------------+-------+-----------+------------------------------------+
  | clk        | 1     | Input     | System clock input       |
  +------------+-------+-----------+------------------------------------+
  | a          | 1     | Input     | Data input for register  |
  +------------+-------+-----------+------------------------------------+
  | b          | 1     | Input     | Combinational input for out|
  +------------+-------+-----------+------------------------------------+
  | q          | 1     | Output    | Registered output        |
  +------------+-------+-----------+------------------------------------+
  | out        | 1     | Output    | Combinational output (b & ~rst)|
  +------------+-------+-----------+------------------------------------+
