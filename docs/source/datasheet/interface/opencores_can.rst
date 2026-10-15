.. _datasheet_interface_opencores_can:

CAN Protocol Controller IP Core
===============================

.. figure:: ./figures/OpenCores.png

Specification

Authors
-------

*Igor Mohor*

igorm@opencores.org

**Rev. 1.0**

Source codes
~~~~~~~~~~~~

See details in ``interface/opencores_can``

Technical Notes
~~~~~~~~~~~~~~~

.. note:: Full details can be found at `opencores <https://opencores.org/projects/can>`_

Controller Area Network or CAN is a control network protocol from
Bosch that has found wide use in Industrial Automation and the
Automotive Industry.

Most of the patents of CAN are owned by Bosch and although there
are no restictions on developing an opensource CAN IP but for any
commercial use the protocol license from Bosch is an indispensable prerequisite.

Size is approximately 12k gates (930 flip-flops).

Features

- Non-Destructive bit-wise arbitration (CSMA/CA)
- Message Based Addressing/Filtering
- Broadcast Communication
- 1 Mbit/Sec Operation
- WISHBONE SoC interface
- 8051 interface
- SJA1000 (Philips) compatible interface.
