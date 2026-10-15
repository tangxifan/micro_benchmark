# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += test_mode_low.v

# Top-level module name
TOPLEVEL = test_mode_low

# Python test module name (without .py)
MODULE = test_test_mode_low

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
