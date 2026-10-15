.. _datasheet_processors_vexriscv:

VexRiscv
--------

`VexRiscv <https://github.com/spinalhdl/vexriscv>`_ is a modular 32-bit RISC-V softcore processor written in SpinalHDL. Because of its modular plugins, developers can generate vastly different hardware profiles from the same codebase. 

Pre-packaged templates like **Small**, **Mutex** (Multicore/Linux), and **Full** trade off FPGA resource area (LUTs/FFs) for processing performance (DMIPS/MHz) and architectural features.

Source codes
~~~~~~~~~~~~

See details in

- ``processors/VexRiscv_small``
- ``processors/VexRiscv_murax``
- ``processors/VexRiscv_full``

VexRiscv Small
~~~~~~~~~~~~~~

The **Small** template strips away luxury architectural components to compress the logic footprint into minimal hardware.

* **Resource Preservation:** Merges or completely eliminates specific pipeline stages to save look-up tables (LUTs).
* **Data Stalls:** Lacks pipeline data forwarding/bypassing. Instructions must completely resolve in the WriteBack stage before successive dependent instructions can read their outputs.
* **Optimal Selection:** Ideal for simple state machines, basic I/O management, or replacing 8-bit/16-bit legacy microcontrollers where chip space is heavily constrained.

VexRiscv Mutex
~~~~~~~~~~~~~~

The **Mutex** profile (often called the Multicore template) is built to orchestrate Symmetric Multiprocessing (SMP) platforms, commonly leveraged within frameworks like LiteX.

* **Hardware Mutual Exclusion:** Implements the RISC-V **A (Atomic) extension**. This introduces atomic instructions like ``lr.w`` (Load-Reserved) and ``sc.w`` (Store-Conditional) that enable thread-safe software locks, spinlocks, and mutexes.
* **Cache Coherency:** Features custom bus-snooping interconnects to maintain data consistency across separate execution pipelines.
* **Optimal Selection:** Used for booting multi-core Linux or complex operating systems requiring strict process isolation and inter-core communication.

VexRiscv Full
~~~~~~~~~~~~~

The **Full** flavor maxes out single-threaded efficiency by enabling extensive structural optimizations.

* **No-Compromise Datapath:** Includes full result bypassing, hardware single-cycle multipliers, and barrel shifters.
* **Control Flow Acceleration:** Uses a robust Branch Target Buffer (BTB) or GShare dynamic branch predictor to drastically shrink cycle penalties on loops and conditional jumps.
* **Optimal Selection:** Perfect for math-heavy applications, single-core Real-Time Operating Systems (RTOS), and bare-metal high-throughput firmware.

Performance
~~~~~~~~~~~

The following table contrasts the three core configurations across critical design parameters.

.. warning:: The following resource utilization is just an estimation! Different tools in different versions may result differently.

+--------------------------+-----------------------+-----------------------------+------------------------------+
| Feature                  | Small                 | Mutex (Multicore)           | Full (Max Performance)       |
+==========================+=======================+=============================+==============================+
| **Target Use Case**      | Microcontrollers      | Linux SMP, Multi-core       | High-performance single-core |
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **ISA Extensions**       | RV32I or RV32IM       | RV32IMA                     | RV32IMAC (or Full IMC)       |
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **Performance**          | ~0.52 DMIPS/MHz       | ~1.1 to 1.2 DMIPS/MHz       | ~1.44+ DMIPS/MHz             |
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **Pipeline Bypassing**   | None (WB Stall)       | Full bypassing              | Full bypassing + late ALU    |
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **Caches**               | Cacheless             | Coherent I-Cache & D-Cache  | Large I-Cache & D-Cache      |
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **Branch Prediction**    | None                  | Dynamic (BTB)               | Advanced Dynamic (BTB/GShare)|
+--------------------------+-----------------------+-----------------------------+------------------------------+
| **Approx. Size (Artix-7)**| ~500 - 700 LUTs      | ~2,000 - 3,000+ LUTs        | ~1,500 - 2,500 LUTs          |
+--------------------------+-----------------------+-----------------------------+------------------------------+

