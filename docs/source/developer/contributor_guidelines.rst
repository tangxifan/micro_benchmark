.. _developer_contributor_guidelines:

Contributor Guidelines
======================

Motivation
----------
Github projects involve many parties with different interests.
It is necessary to establish rules to

- guarantee the quality of each pull request by establishing a standard
- code review for each pull request is straightforward
- contributors have confidence when submitting changes

Create Pull requests
--------------------

- Contributors should state clearly their motivation and the principles of code changes in each pull request
- Contributors should be active in resolving conflicts with other contributors as well as maintainers. In principle, all the maintainers want every pull request in and are looking for reasons to approve it.
- Each pull request should pass all the existing tests in CI (See :ref:`developer_contributor_guidelines_checkin_system` for details). Otherwise, it should not be merged unless you get a waiver from all the maintainers.
- Contributors should not modify any codes/tests which are unrelated to the scope of their pull requests.
- The size of each pull request should be small. Large pull request takes weeks to be merged. The recommend size of pull request is up to 500 lines of codes changes. If you have one large file, this can be waived. However, the number of files to be changed should be as small as possible.

  .. note:: For large pull requests, it is strongly recommended that contributors should talk to maintainers first or create an issue on the Github. Contributors should clearly define the motivation, detailed technical plan as well as deliverables. Through discussions, the technical plan may be requested to change. Please do not start code changes blindly before the technical plan is approved.

- For any new feature/functionality to be added, there should be

  - Dedicated test cases in CI which validates its correctness
  - An update on the documentation, if it changes user interface
  - Provide sufficient code comments to ease the maintenance

.. _developer_contributor_guidelines_checkin_system:

Check-in System
---------------

.. seealso:: The check-in system is based on continous integration (CI). See details in :ref:`developer_ci` 

The check-in system aims to offer a standardized way to 

- ensure quailty of each contribution
- resolve conflicts between teams

It is designed for efficient communication between teams.

Add Benchmarks
--------------

FPGA requires a set of benchmark suites to validate its correctness before tape-out.
When add a new benchmark to the project, the following steps have to followed.

Choose a benchmark suite
^^^^^^^^^^^^^^^^^^^^^^^^

Benchmarks are catorized into different suites, each of which are designed to validate a specific architecture enhancement of the FPGA.
For example, ``dsp`` are designed to validate DSP blocks in the FPGA architecture.
When adding a new benchmark, developer should propose to maintainers which category it should belong to.
Once agreed, the benchmark can be added to the dediciated directory, e.g., ``dsp/<benchmark_suite_name>``

.. note:: If your benchmark is out of any existing category, you may create a new category. But you should discuss with maintainer first.

Required files
^^^^^^^^^^^^^^

A benchmark should include the following files, so that it can be integrated to the design verification system

- HDL files (``.v``)

  - You may add multiple HDL files for a complex benchmark
  - Please name the top-level module to be the same as the name of benchmark.

- Cocotb testbenches (``.py``).

  - See details in `cocotb documentation <https://docs.cocotb.org/en/stable/examples.html>`_
  - Please name the testbench file as ``test_<benchmark_name>.py``

- Cocotb Makefile (``Makefile``).

  - This is used to run cocotb simulation using iVerilog or other simulators

.. note:: All the files should be placed or linked in a dedicated directory, e.g., ``benchmarks/<benchmark_suite_name>``

Update workflow
^^^^^^^^^^^^^^^

- If you are adding a benchmark to an existing category, you need to update the list.

See an example under ``utils/tasks/simple_gates_rtl_list.yaml``

.. note:: For file format of the list file, please see :ref:`file_format_rtl_list`

- If you are creating a new category for benchmark, you need to update workflows by adding the benchmark suite to configuration matrix.

See `example <https://github.com/tangxifan/micro_benchmark/blob/0c864fe677b52c1355923ba8d9effd387a4eab9b/.github/workflows/rtl_verification.yml#L65-L66>`_
