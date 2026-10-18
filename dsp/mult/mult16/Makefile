# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (top module and submodule)
VERILOG_SOURCES += mult16.v
VERILOG_SOURCES += mult_16.v

# Top-level module name
TOPLEVEL = mult16

# Python test module filename (without .py)
MODULE = test_mult16

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
