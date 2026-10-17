.. _datasheet_ram_dual_port_ram_8x16_8x32_mif:

Dual-Port RAM 8x16 and 8x32 MIF Single Clock
--------------------------------------------

Introduction
~~~~~~~~~~~~

This benchmark tests Block RAM (BRAM) primitive inferencing, memory initialization (`.hex` files), and dual-width dual-port memory functionality.
The module instantiates two parallel memory sub-cores—an 8-depth by 16-bit width RAM and an 8-depth by 32-bit width RAM—sharing a common system clock and control lines.

Source codes
~~~~~~~~~~~~

See details in ``ram/dual_port_ram_8x16_8x32_mif``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/dual_port_ram_8x16_8x32_mif.svg
  :width: 70%
  :alt: Dual-Port RAM 8x16 and 8x32 MIF Single Clock schematic

  Dual-Port RAM 8x16 and 8x32 MIF Single Clock schematic

Performance
~~~~~~~~~~~

Expect to consume multiple Block RAM or distributed RAM primitives to support both 16-bit and 32-bit channels.

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
  * - Dual-Width Single-Clock
    - 48
    - 48
    - 48
    - 48
    - 0
    - 0
    - 2
