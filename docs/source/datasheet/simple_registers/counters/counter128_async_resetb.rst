.. _datasheet_simple_registers_counter128_async_resetb:

counter128_async_reset(b)
-------------------------

Introduction
~~~~~~~~~~~~

This module implements multiple version of 128-bit wide synchronous up-counters equipped with an active-high/low asynchronous reset (`reset`/`resetb`).
On every rising edge of the clock, the 128-bit result increments by 1, while asserting `reset`/`resetb` hight/low immediately clears the output register to zero asynchronously.

Source codes
~~~~~~~~~~~~

See details in 

- ``simple_registers/counter128_async_reset``
- ``simple_registers/counter128_async_resetb``

Block Diagram
~~~~~~~~~~~~~

The following shows an example of the active-low version

.. figure:: ./figures/counter128_async_resetb_schematic.svg
  :width: 60%
  :alt: counter128_async_resetb schematic

  counter128_async_resetb schematic


Performance
~~~~~~~~~~~

Expect to consume 128 flip-flops and associated carry/LUT logic to support the 128-bit wide arithmetic incrementer and asynchronous reset path.

.. warning:: The following resource utilization is just an estimation! Different tools in different versions may result differently.

.. list-table:: Estimated resource Utilization
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
    - 128
    - ~128
    - 128
    - ~32
    - 0
    - 0
