# Micro Benchmarks for FPGA design verification

[![RTL Compatibility](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_compatibility.yml/badge.svg)](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_compatibility.yml)
[![RTL Verification](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_verification.yml/badge.svg)](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_verification.yml)
[![Documentation Status](https://readthedocs.org/projects/micro-benchmark/badge/?version=latest)](https://micro-benchmark.readthedocs.io/en/latest/?badge=latest)

Version: see [`VERSION.md`](VERSION.md)

Benchmarks are categorized in the following directories, depending their logic functions:

- dsp: Digital Signal Processing (DSP) -related applications
- fsm: Finite State Machine (FSM) - related applications
- interface: system bus and protocols, such as SPI, UART etc.
- processor: CPU cores
- ram: Memory blocks, including random access memories, FIFOs, etc.
- simple_gates: combinational circuits in small sizes
- simple_registers: sequential circuits in small sizes
