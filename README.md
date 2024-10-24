# Micro Benchmarks for FPGA design verification

[![RTL Compatibility](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_compatibility.yml/badge.svg)](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_compatibility.yml)
[![RTL Verification](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_verification.yml/badge.svg)](https://github.com/tangxifan/micro_benchmark/actions/workflows/rtl_verification.yml)
[![Documentation Status](https://readthedocs.org/projects/micro-benchmark/badge/?version=latest)](https://micro-benchmark.readthedocs.io/en/latest/?badge=latest)

Version: see [`VERSION.md`](VERSION.md)

## Licenses

Most of the benchmarks are in MIT license. 

> [!NOTE]
> Please note that external benchmarks which may not be in compatible licenses. For each external benchmarks, LICENSE file can be found under its location


The list of external benchmarks is as follows. Please double check before using.

- interface/opencores\_can
- interface/opencores\_gpio
- interface/opencores\_i2c
- interface/opencores\_ptc
- interface/opencores\_spi
- interface/opencores\_simple\_spi
- interface/opencores\_uart16550
- interface/verilog\_spi
- processors/VexRiscv\_full
- processors/VexRiscv\_murax
- processors/VexRiscv\_small
- dsp/dspfilters
- dsp/cordic

## Documentation

Full documentation can be found at [here](https://micro-benchmark.readthedocs.io/)
## Benchmarks

Benchmarks are categorized in the following directories, depending their logic functions:

- dsp: Digital Signal Processing (DSP) -related applications
- fsm: Finite State Machine (FSM) - related applications
- interface: system bus and protocols, such as SPI, UART etc.
- processor: CPU cores
- ram: Memory blocks, including random access memories, FIFOs, etc.
- simple_gates: combinational circuits in small sizes
- simple_registers: sequential circuits in small sizes
