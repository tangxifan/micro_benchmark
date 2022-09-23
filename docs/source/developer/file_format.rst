.. _file_format:


.. _file_format_rtl_list:

RTL List
--------

The RTL list file is in yaml format, where users can define one or multiple RTL projects.

A quick example for including a RTL project:

.. code-block:: yaml

  <rtl_project_name>:
    source:
      - <rtl_source_0>
      - <rtl_source_1>
      - <rtl_source_2>
    top_module: <top-level_module name>
    cocotb_dir: <directory to the cocotb testbench for this project>

Detailed syntax are as follows:

.. option:: rtl_project_name

  Specify the name of this RTL project. This is the unique identifier for the project. 

.. option:: source
   
   You can define a number of rtl source files under this node. Please include the relative path to each source file, based on the project home. For example, ``simple_gates/and2/and2.v``

.. option:: top_module

  Specify the name of top-level module among all the source files

.. option:: cocotb_dir

  Specify the directory to the cocotb testbench for this project. For example, ``simple_gates/and2``. If not specified, cocotb tests will not be run on this project

  .. note:: Do not include the cocotb python script in the path. 
