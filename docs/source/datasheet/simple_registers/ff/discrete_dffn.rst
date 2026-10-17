.. _datasheet_simple_registers_discrete_dffn:

discrete_dffn
-------------

Introduction
~~~~~~~~~~~~

The ``discrete_dffn`` module implements a flip-flop triggered on an inverted (negative-edged) clock signal. This benchmark is specifically designed to verify whether an FPGA architecture natively supports internal clock inversion or negative-edged clocking resources[cite: 4]. It uses an internal combinatorial inverter (``int_clk = ~clk_ni``) to clock the data register (``d_o <= d_i``).

Source codes
~~~~~~~~~~~~

See details in ``simple_registers/ff/discrete_dffn.v``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/discrete_dffn_schematic.svg
  :width: 70%
  :alt: discrete_dffn schematic

  discrete_dffn schematic

Performance
~~~~~~~~~~~

Expect to consume minimal FPGA resources (typically 1 LUT/inverter and 1 Flip-Flop). The design evaluates clock network inversion handling and negative-edge register mapping.

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
    - 2
    - 1
    - 1
    - 1
    - 0
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: discrete_dffn Top-Level Ports

  +------------+-------+-----------+------------------------------------+
  | Port       | Width | Direction | Description                        |
  +------------+-------+-----------+------------------------------------+
  | clk_ni     | 1     | Input     | Negative clock reference input|
  +------------+-------+-----------+------------------------------------+
  | d_i        | 1     | Input     | Data input                |
  +------------+-------+-----------+------------------------------------+
  | d_o        | 1     | Output    | Registered data output    |
  +------------+-------+-----------+------------------------------------+
