# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += pipelined_8bit_adder.v

# Top-level module name
TOPLEVEL = pipelined_8bit_adder

# Python test module name (without .py)
MODULE = test_pipelined_8bit_adder

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
