.. _datasheet_ram_dual_port_ram_1k:

Dual-Port RAM 1K (128x8)
------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing and basic dual-port memory functionality.
The module instantiates a 128x8-bit dual-port RAM (``dual_port_sram_1kb``) with independent write and read address/control buses driven by a shared clock (``clk``).

Source codes
~~~~~~~~~~~~

See details in ``ram/dual_port_ram_1k``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/dual_port_ram_1k.svg
  :width: 70%
  :alt: Dual-Port RAM 1K schematic

  Dual-Port RAM 1K schematic

Performance
~~~~~~~~~~~

Expect to consume BRAM primitives or equivalent memory logic resources.

.. list-table:: Estimated Resource Utilization
  :header-rows: 1
  :class: longtable

  * - Benchmark
    - Inputs
    - Outputs
    - LUTs
    - FF / Registers
    - Carry
    - DSP
    - BRAM
  * - DUAL_PORT_RAM_1K
    - 25
    - 8
    - 0
    - 8
    - 0
    - 0
    - 1
