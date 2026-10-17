# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += clock_divider.v

# Top-level module name
TOPLEVEL = clock_divider

# Python test module filename (without .py)
MODULE = test_clock_divider

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
