.. _developer_naming_convention:

Naming Convention
=================

Counter Design Names
--------------------

We recommend developers to follow the naming convention when adding any counter designs

.. code-block::

   counter[down]<size>_[async|sync]_[set|reset|setb|resetb]

.. option:: down 
  
   represent a counting down counter

.. option:: size

   size is an integer, indicating the number of bits for a counter

.. option:: [async|sync]

   represent the feature of reset and set signal

.. option:: [setp|resetp|setn|resetn]

   indicates the existence of reset/set signal as well as polarity.
   In particular, suffix ``p`` denotes active-high signals while suffix ``n`` denotes active-low signals

For instance,

.. code-block::

    counterdown8_async_resetn

shows a counter with the following features:

- counting down
- 8-bit in width
- Asynchronous active-low reset

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

