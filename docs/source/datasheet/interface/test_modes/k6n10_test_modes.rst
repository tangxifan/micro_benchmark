.. _datasheet_interface_k6n10_test_modes:

k6n10_test_modes
----------------

Introduction
~~~~~~~~~~~~

The ``test_modes`` module implements a comprehensive K8-architecture test benchmark. 
It integrates a 12-stage serial shift register pipeline (tapped at stages 3, 7, and 11 to drive outputs ``x``, ``y``, and ``z``), a customizable combinatorial logic gating term (``d0 = (e && g) || !f``), and a parallel 4-bit adder with carry-in/carry-out support (``n0 = a + b + reg_cin``).

Source codes
~~~~~~~~~~~~

See details in ``interface/test_modes/k6_N10/K6N10_test_modes.v``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/k6n10_test_modes_schematic.svg
  :width: 70%
  :alt: test_modes schematic

  test_modes schematic

Performance
~~~~~~~~~~~

Expect to consume moderate FPGA routing resources and logic cells to support the wide shift-register chain, input bit registers, and the 4-bit arithmetic adder block.

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
    - 13
    - 9
    - 24
    - 25
    - 4
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: test_modes Top-Level Ports

  +------------+-------+-----------+------------------------------------+
  | Port       | Width | Direction | Description                        |
  +------------+-------+-----------+------------------------------------+
  | clk        | 1     | Input     | System clock input      |
  +------------+-------+-----------+------------------------------------+
  | a_0 - a_3  | 1     | Input     | 4-bit Operand A inputs |
  +------------+-------+-----------+------------------------------------+
  | b_0 - b_3  | 1     | Input     | 4-bit Operand B inputs  |
  +------------+-------+-----------+------------------------------------+
  | cin        | 1     | Input     | Adder carry-in input    |
  +------------+-------+-----------+------------------------------------+
  | e, f, g    | 1     | Input     | Control logic inputs  |
  +------------+-------+-----------+------------------------------------+
  | sum_0-sum_3| 1     | Output    | 4-bit adder sum outputs|
  +------------+-------+-----------+------------------------------------+
  | cout       | 1     | Output    | Adder carry-out output  |
  +------------+-------+-----------+------------------------------------+
  | x          | 1     | Output    | Pipeline tap at stage 3 |
  +------------+-------+-----------+------------------------------------+
  | y          | 1     | Output    | Pipeline tap at stage 7 |
  +------------+-------+-----------+------------------------------------+
  | z          | 1     | Output    | Pipeline tap at stage 11|
  +------------+-------+-----------+------------------------------------+
