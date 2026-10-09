.. _datasheet_dual_port_ram_8x16_mif_32clk:

Dual-Port RAM 8x16 MIF 32 Clock
----------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing, memory initialization (`.mif` files), and multi-clock routing scalability across **32 dual-port memory instances**.
The module instantiates 32 independent 256x16 dual-port RAMs, each with its own write clock (`clk_a`) and read clock (`clk_b`).

Source codes
~~~~~~~~~~~~

See details in ``ram/dual_port_ram_8x16_mif_32clk``

Block Diagram
~~~~~~~~~~~~~

This design is a 32-clock version of the illustrative schematic in :numref:`fig_dual_port_ram_8x16_mif_32clk`

.. _fig_dual_port_ram_8x16_mif_32clk:

.. figure:: ./figures/dual_port_ram_8x16_mif_Nclk.svg
  :width: 70%
  :alt: Dual-Port RAM 8x16 MIF 32 Clock schematic

  Dual-Port RAM 8x16 MIF 32 Clock schematic

Performance
~~~~~~~~~~~

Expect to consume 32 BRAM primitives (or equivalent LUT RAM logic).

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
  * - 32-Clock
    - 1088
    - 512
    - 512
    - 512
    - 0
    - 0
    - 32
