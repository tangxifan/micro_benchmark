.. _datasheet_dual_port_ram_8x16_mif_24clk:

Dual-Port RAM 8x16 MIF 24 Clock
----------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing, memory initialization (`.mif` files), and multi-clock routing scalability across **24 dual-port memory instances**.
The module instantiates 24 independent 256x16 dual-port RAMs, each with its own write clock (`clk_a`) and read clock (`clk_b`).

Source codes
~~~~~~~~~~~~

See details in ``ram/dual_port_ram_8x16_mif_24clk``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/dual_port_ram_8x16_mif_24clk.svg
  :width: 70%
  :alt: Dual-Port RAM 8x16 MIF 24 Clock schematic

  Dual-Port RAM 8x16 MIF 24 Clock schematic

Performance
~~~~~~~~~~~

Expect to consume 24 BRAM primitives (or equivalent LUT RAM logic).

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
  * - 24-Clock
    - 816
    - 384
    - 384
    - 384
    - 0
    - 0
    - 24
