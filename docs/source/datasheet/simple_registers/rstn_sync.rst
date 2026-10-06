rstn_sync
=========

Introduction
------------

This benchmark is designed to test an asynchronous reset assertion and
synchronous reset de-assertion circuit. The reset input is active-low.

The benchmark uses a two-stage flip-flop synchronizer. When the asynchronous
reset is asserted, the internal flip-flops are reset immediately. When the
reset is de-asserted, the reset release is synchronized to the rising edge
of the clock.

Source codes
------------

See details in ``simple_registers/rstn_sync``

Block Diagram
-------------

.. figure:: figures/reset_sync_active_low.png
   :alt: Asynchronous assert and synchronous de-assert reset synchronizer
   :align: center

   Asynchronous assert and synchronous de-assert reset synchronizer.

Functionality
-------------

The reset input ``arst_n`` is active-low and the synchronized reset output
``srst_n`` is also active-low.

The expected behavior is:

* ``arst_n = 0``: ``srst_n`` is asserted asynchronously.
* ``arst_n`` transitions from ``0`` to ``1``: ``srst_n`` remains asserted.
* After the first rising clock edge: the first synchronizer stage is released.
* After the second rising clock edge: ``srst_n`` is de-asserted.

Therefore, reset assertion is asynchronous while reset de-assertion is
synchronous to ``clk``.

Verification
------------

The benchmark includes a cocotb self-checking testbench.

The testbench verifies:

* Asynchronous reset assertion.
* Synchronous reset de-assertion.
* Two-clock-cycle reset release.
* Reset assertion occurring between clock edges.
* Repeated assertion and de-assertion sequences.

The testbench automatically reports an error when the reset behavior does
not match the expected behavior.

Performance
-----------

The design primarily consists of two flip-flops used as the reset
synchronizer. The expected resource utilization is therefore very small.

The synchronizer introduces two clock cycles of latency between reset
de-assertion and the release of ``srst_n``.

Estimated resource Utilization
------------------------------

.. list-table::
   :header-rows: 1

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
     - 0
     - 2
     - 0
     - 0
     - 0

.. warning::

   The resource utilization shown above is an estimation. Different FPGA
   architectures, synthesis tools, and tool versions may produce different
   results.
