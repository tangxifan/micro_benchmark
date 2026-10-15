# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += K6N10_test_modes.v

# Top-level module name
TOPLEVEL = test_modes

# Python test module name (without .py)
MODULE = test_k6n10_test_modes

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
