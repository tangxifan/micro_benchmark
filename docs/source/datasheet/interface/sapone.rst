.. _datasheet_interface_sapone:

SAP-1 8-Bit Computer (SAPone)
-----------------------------

Introduction
~~~~~~~~~~~~

The ``SAPone`` module implements a complete SAP-1 (Simple-As-Possible) 8-bit educational computer architecture. 
It integrates a centralized FSM controller, program ROM memory, an instruction register, an ALU supporting addition and subtraction, and multiple working registers connected via an internal system bus.

Source codes
~~~~~~~~~~~~

See details in ``interface/SAPone``

Block Diagram
~~~~~~~~~~~~~

.. figure:: ./figures/SAPone_schematic.svg
  :width: 70%
  :alt: SAP-1 Computer schematic

  SAP-1 Computer schematic

Architecture & Major Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SAPone core consists of the following primary submodules:

- **Program Counter (PC)**: 4-bit synchronous counter tracking instruction addresses.
- **Memory Address Register (MAR)**: Latches address inputs for ROM access.
- **Program ROM**: Provides instruction and data bytes based on MAR address lines.
- **Instruction Register (IR)**: Splits incoming bytes into a 4-bit opcode and 4-bit operand.
- **Controller**: Finite state machine that decodes opcodes and generates a 12-bit control word (`con`).
- **Accumulator (ACC)**: Stores working arithmetic results with dual outputs.
- **Adder/Subtractor (ADDSUB)**: Combinational ALU performing addition or subtraction governed by the ``su`` control signal.
- **B-Register**: Temporary operand holding register for ALU operations.
- **Output Register**: Latches final values onto the external ``SAP_out`` display bus.

Supported Instructions
^^^^^^^^^^^^^^^^^^^^^^

The internal FSM controller supports the following instruction set architecture (ISA):
- ``LDA`` (Opcode 0x0): Load Accumulator from memory.
- ``ADD`` (Opcode 0x1, 0x2): Add memory content to Accumulator.
- ``SUB`` (Opcode 0x3): Subtract memory content from Accumulator.
- ``OUT`` (Opcode 0xe): Transfer Accumulator value to output display register.
- ``HLT`` (Opcode 0xf): Halt execution.

Performance
~~~~~~~~~~~

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
    - 20
    - 135
    - 52
    - 4
    - 0
    - 0

IO Ports
~~~~~~~~

.. table:: SAPone Top-Level Ports

  +------------+-------+-----------+------------------------------------+
  | Port       | Width | Direction | Description                        |
  +------------+-------+-----------+------------------------------------+
  | clk        | 1     | Input     | System clock input      |
  +------------+-------+-----------+------------------------------------+
  | clr_       | 1     | Input     | Active-low asynchronous clear|
  +------------+-------+-----------+------------------------------------+
  | SAP_out    | 8     | Output    | Output register bus data|
  +------------+-------+-----------+------------------------------------+
  | con        | 12    | Output    | Control word status signals|
  +------------+-------+-----------+------------------------------------+
  | bus        | 8     | Inout     | Central internal data bus|
  +------------+-------+-----------+------------------------------------+
