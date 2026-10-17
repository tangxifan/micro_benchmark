# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += two_dff_inv_rst.v

# Top-level module name
TOPLEVEL = two_dff_inv_rst

# Python test module name (without .py)
MODULE = test_two_dff_inv_rst

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
