# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += asyn_spram_4x1.v

# Top-level module name
TOPLEVEL = asyn_spram_4x1

# Python test module name (without .py)
MODULE = test_asyn_spram_4x1

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
