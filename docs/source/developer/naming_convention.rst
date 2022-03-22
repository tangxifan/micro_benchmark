.. _developer_naming_convention:

Naming Convention
=================

Cell Names
----------

.. note:: we refer to standard cell wrapper here. Wrappers are built to make netlists portable between PDKs as well as across standard cell libraries in a PDK.

For code readability, the cell name should follow the convention
::
  <Cell_Function><Set_Features><Reset_Features><Output_Features><Drive_Strength>_<Wrapper>

.. option:: Cell_Function

  Name of logic function, e.g., AND2, XNOR3, etc.

.. option:: Set_Features

  This is mainly for sequential cells, e.g., D-type flip-flops. If a cell contains a set signal, its existence and polarity must be inferreable by the cell name. The available options are 
  
  - S: Asynchronous active-high set 
  - SYNS: Synchronous active-hight set
  - SN: Asynchronous active-low set
  - SYNSN: Synchronous active-low set

  .. note:: For cells without set, this keyword should be empty

.. option:: Reset_Features

  This is mainly for sequential cells, e.g., D-type flip-flops. If a cell contains a reset signal, its existence and polarity must be inferreable by the cell name. The available options are 
  
  - R: Asynchronous active-high reset 
  - SYNR: Synchronous active-hight reset
  - RN: Asynchronous active-low reset
  - SYNRN: Synchronous active-low reset

  .. note:: For cells without reset, this keyword should be empty

.. option:: Output_Features

  This is mainly for sequential cells, e.g., D-type flip-flops.

  - If not specified, the sequential cell contains a pair of differential outputs, e.g., ``Q`` and ``QN``
  - If specified, the sequential cell only contains single output, e.g., ``Q`` 

  The available options are
  
  - Q: single output which is positive
  - QN: single ouput which is negative

  .. note:: For cells without reset, this keyword should be empty

.. option:: Drive_Strength

  This is to specify the drive strength of a cell

  - If not specified, we assume minimum drive strength, i.e., ``D0``.
  - If specified, we expect a format of ``D<int>``, where the integer indicates the drive strength

.. option:: Wrapper

  This is to specify if the cell is a wrapper of an existing standard cell

  - If not specified, we assume this cell contains RTL
  - If specified, we assume this cell is a wrapper of an existing standard cell

A quick example
::
  NAND2D4_WRAPPER

represents a wrapper for a standard cell that is a 2-input NAND gate with a drive strength of 4

Another example
::
  SDFFSSYNRNQ

represents a scan-chain flip-flop which contains
 
  - Asynchronous active-high set
  - Synchronous active-low reset
  - Single output


Pin Names
---------

.. note:: Please use lowercase as much as you can

For code readability, the pin name should follow the convention
::
  <Pin_Name>_<Polarity><Direction>


.. option:: Pin_Name

  Represents the pin name

.. option:: Polarity

  Represents polarity of the pin, it can be 

  - ``n`` denotes a negative-enable (active_low) signal 

  .. note:: When not specified, by default we assume this is a postive-enable (active-high) signal

.. option:: Direction

  Represents the direction of a pin, it can be 

  - ``i`` denotes an input signal
  - ``o`` denotes an output signal

A quick example
::
  clk_ni

represents an input clock signal which is negative-enable

Another example
::
  q_no

represents an output Q signal which is negative to the input

