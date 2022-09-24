.. _datasheet_fsm_scalable_seq_detector:

Scalable Sequence Detector
------------------------
.. warning:: This benchmark may have some modification/addition of features in future.

.. _datasheet_scalable_seq_detector_introduction:

Introduction
~~~~~~~~~~~~~
This benchmark is to detect any sequence of length equal to 2^STATE_BITS. This is a finite state machine based on moore model. All output signals/msgs depends only on current state of machine. The design is scalable, STATE_BITS defines the number of states, the hardware shall be generated based on STATE_BITS. Also, the sequence needs to be passed to DUT as a bus signal, while the x inputs takes sequence bit by bit for detection and msgs are shown on output signals. 

.. _fig_scalable_seq_detector:

Block Diagram / Schematic
~~~~~~~~~~~~~
.. figure:: ./figures/scalable_seq_detector.svg
  :width: 100%
  :alt: Scalable Sequence Detector schematic

  Scalable Sequence Detector schematic

.. _performance_scalable_seq_detector:

Performance
~~~~~~~~~~~~~
.. figure:: ./figures/scalable_seq_detector_synthesis_report.png
  :width: 100%
  :alt: Scalable Sequence Detector schematic
Scalable Sequence Detector schematic
