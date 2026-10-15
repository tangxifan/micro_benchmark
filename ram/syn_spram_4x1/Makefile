# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += syn_spram_4x1.v

# Top-level module name
TOPLEVEL = syn_spram_4x1

# Python test module name (without .py)
MODULE = test_syn_spram_4x1

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
