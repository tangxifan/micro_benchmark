.. _datasheet_interface_cf_ldpc:

CF LDPC Decoder
---------------

.. note:: This project comes from `opencores <https://opencores.org/projects/cf_ldpc>`_

.. only:: builder_html

Source Code
~~~~~~~~~~~

You can find source files under ``interface/cf_ldpc``

Technical Notes
~~~~~~~~~~~~~~~


.. note:: Detailed manual can be found on Opencores


This LDPC error corrector implements Gallager's "A" algorithm: an iterative, hard-decision decoder that opts for simplicity over performance. The architecture elaborates all logic required to implement the message-passing algorithm from message nodes, to check nodes, then back to message nodes -- one iteration occurs every clock cycle.

The core is primarily meant as an LDPC evaluation platform, as the fully parallel architecture may be inappropriate for synthesis of large block length LDPC decoders.

The Confluence source code generates an LDPC error corrector given an arbitrary parity-check matrix. This core implements Gallager's (20, 3, 4) parity-check matrix:


.. code-block::

  1 1 1 1 . . . . . . . . . . . . . . . .
  . . . . 1 1 1 1 . . . . . . . . . . . .
  . . . . . . . . 1 1 1 1 . . . . . . . .
  . . . . . . . . . . . . 1 1 1 1 . . . .
  . . . . . . . . . . . . . . . . 1 1 1 1
  1 . . . 1 . . . 1 . . . 1 . . . . . . .
  . 1 . . . 1 . . . 1 . . . . . . 1 . . .
  . . 1 . . . 1 . . . . . . 1 . . . 1 . .
  . . . 1 . . . . . . 1 . . . 1 . . . 1 .
  . . . . . . . 1 . . . 1 . . . 1 . . . 1
  1 . . . . 1 . . . . . 1 . . . . . 1 . .
  . 1 . . . . 1 . . . 1 . . . . 1 . . . .
  . . 1 . . . . 1 . . . . 1 . . . . . 1 .
  . . . 1 . . . . 1 . . . . 1 . . 1 . . .
  . . . . 1 . . . . 1 . . . . 1 . . . . 1
