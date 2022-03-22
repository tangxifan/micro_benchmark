Makefile System
===============

To keep EDA flows simple, all the design flows are called through Makefiles and python scripts.

.. _developer_build_system_makefile_principles:

Principles
^^^^^^^^^^

Makefiles exist in either top-level or lower-level directories, each of which may contain multiple build targets.

- The build targets in top-level makefile are most frequently used design flows across multiple domains, e.g., generate bitstreams
- The build targets in low-level makefile are frequently used design flows within a specific domain, e.g., run HDL simulations.

When call a makefile, please follow the convention

```
make <build_target_name> <variables>
```

.. _developer_build_system_variables:

Variables
^^^^^^^^^

.. option:: BENCHMARK_SUITE_NAME=<string>

  Define the name of benchmark suite to be run. This is required when running RTL compatibility and RTL verification tests.
