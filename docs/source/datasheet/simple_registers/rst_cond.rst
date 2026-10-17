.. _datasheet_simple_registers_rst_cond:

rst_cond
--------

Introduction
~~~~~~~~~~~~

The ``rst_cond`` module implements a locally generated reset signal used for testing reset distribution networks with internal drivers. It combines an external reference reset (``rst_i``) with a reset condition input (``rst_cond_i``) via an internal combinatorial AND gate (``int_rst``) to asynchronously reset a registered data path (``q_o <= d_i``)].

Source codes
~~~~~~~~~~~~

See details in ``simple_registers/rst_cond.v``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/rst_cond_schematic.svg
  :width: 70%
  :alt: rst_cond schematic

  rst_cond schematic

Performance
~~~~~~~~~~~

Expect to consume minimal FPGA resources (typically 1 LUT/gate and 1 register) for locally conditioned asynchronous reset distribution and internal reset network testing.

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
    - 1
    - 1
    - 1
    - 0
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: rst_cond Top-Level Ports

  +--------------+-------+-----------+------------------------------------+
  | Port         | Width | Direction | Description                        |
  +--------------+-------+-----------+------------------------------------+
  | rst_cond_i   | 1     | Input     | Reset gating condition input|
  +--------------+-------+-----------+------------------------------------+
  | rst_i        | 1     | Input     | Primary reference reset input|
  +--------------+-------+-----------+------------------------------------+
  | clk_i        | 1     | Input     | Primary reference system clock|
  +--------------+-------+-----------+------------------------------------+
  | d_i          | 1     | Input     | Data input              |
  +--------------+-------+-----------+------------------------------------+
  | q_o          | 1     | Output    | Registered data output   |
  +--------------+-------+-----------+------------------------------------+
