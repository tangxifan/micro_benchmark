# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += discrete_dffn.v

# Top-level module name
TOPLEVEL = discrete_dffn

# Python test module name (without .py)
MODULE = test_discrete_dffn

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
