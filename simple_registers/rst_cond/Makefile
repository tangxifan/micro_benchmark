# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += rst_cond.v

# Top-level module name
TOPLEVEL = rst_cond

# Python test module name (without .py)
MODULE = test_rst_cond

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
