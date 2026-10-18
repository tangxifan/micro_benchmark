# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Include top-level and submodule Verilog sources
VERILOG_SOURCES += dual_mult8_mix_regin.v
VERILOG_SOURCES += mult_8.v
VERILOG_SOURCES += mult_8_regin.v

# Top-level module name
TOPLEVEL = dual_mult8_mix_regin

# Python test module filename (without .py)
MODULE = test_dual_mult8_mix_regin

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
