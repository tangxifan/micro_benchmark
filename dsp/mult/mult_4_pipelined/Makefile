# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += mult_4_pipelined.v

# Top-level module name
TOPLEVEL = mult_4_pipelined

# Python test module filename (without .py)
MODULE = test_mult_4_pipelined

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
