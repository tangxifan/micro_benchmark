.. _datasheet_dual_port_ram_8x16_mif_Nclk:

Dual-Port RAM 8x16 MIF N-Clock
------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing, memory initialization (`.mif` files), and multi-clock routing scalability across **4 dual-port memory instances**.
The module instantiates **N** independent 256x16 dual-port RAMs, each with its own write clock (`clk_a`) and read clock (`clk_b`).

Source codes
~~~~~~~~~~~~

See details in

- ``ram/dual_port_ram_8x16_mif_4clk``
- ``ram/dual_port_ram_8x16_mif_8clk``
- ``ram/dual_port_ram_8x16_mif_16clk``
- ``ram/dual_port_ram_8x16_mif_24clk``
- ``ram/dual_port_ram_8x16_mif_32clk``

Block Diagram
~~~~~~~~~~~~~

.. _fig_dual_port_ram_8x16_mif_Nclk:

.. figure:: ./figures/dual_port_ram_8x16_mif_Nclk.svg
  :width: 70%
  :alt: Dual-Port RAM 8x16 MIF N-Clock schematic

  Dual-Port RAM 8x16 MIF N-Clock schematic

Performance
~~~~~~~~~~~

Expect to consume **N** BRAM primitives (or equivalent LUT RAM logic).

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
  * - 4-Clock
    - 136
    - 64
    - 64
    - 64
    - 0
    - 0
    - 4
  * - 8-Clock
    - 272
    - 128
    - 128
    - 128
    - 0
    - 0
    - 8
  * - 16-Clock
    - 544
    - 256
    - 256
    - 256
    - 0
    - 0
    - 16
  * - 24-Clock
    - 816
    - 384
    - 384
    - 384
    - 0
    - 0
    - 24
  * - 32-Clock
    - 1088
    - 512
    - 512
    - 512
    - 0
    - 0
    - 32
