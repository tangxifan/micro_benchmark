# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += K4N4_test_modes.v

# Top-level module name
TOPLEVEL = K4n4_test

# Python test module name (without .py)
MODULE = test_k4n4_test_modes

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
