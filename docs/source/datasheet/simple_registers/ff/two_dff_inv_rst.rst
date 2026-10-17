.. _datasheet_simple_registers_two_dff_inv_rst:

two_dff_inv_rst
---------------

Introduction
~~~~~~~~~~~~

The ``two_dff_inv_rst`` module implements two flip-flops sharing a differential pair of reset signals. One register is controlled directly by the primary reset input (``rst_i``), while the second register is controlled by an inverted version of the reset (``int_rst = ~rst_i``). This benchmark is useful for validating reset signal routing from global networks and assessing reset signals generated via internal programmable logic resources.

Source codes
~~~~~~~~~~~~

See details in ``simple_registers/ff/two_dff_inv_rst.v``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/two_dff_inv_rst_schematic.svg
  :width: 70%
  :alt: two_dff_inv_rst schematic

  two_dff_inv_rst schematic

Performance
~~~~~~~~~~~

Expect to consume minimal FPGA resources (typically 1 LUT/inverter for the reset inversion and 2 Flip-Flops). The design validates differential reset distribution and asynchronous reset behavior across dual flip-flop paths.

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
    - 3
    - 2
    - 1
    - 2
    - 0
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: two_dff_inv_rst Top-Level Ports

  +------------+-------+-----------+------------------------------------+
  | Port       | Width | Direction | Description                        |
  +------------+-------+-----------+------------------------------------+
  | clk_i      | 1     | Input     | Primary reference system clock|
  +------------+-------+-----------+------------------------------------+
  | rst_i      | 1     | Input     | Primary asynchronous reset input|
  +------------+-------+-----------+------------------------------------+
  | d_i        | 1     | Input     | Data input              |
  +------------+-------+-----------+------------------------------------+
  | d0_o       | 1     | Output    | Registered output (active rst_i)|
  +------------+-------+-----------+------------------------------------+
  | d1_o       | 1     | Output    | Registered output (active int_rst)|
  +------------+-------+-----------+------------------------------------+
