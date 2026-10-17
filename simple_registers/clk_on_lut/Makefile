# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += clk_on_lut.v

# Top-level module name
TOPLEVEL = clk_on_lut

# Python test module name (without .py)
MODULE = test_clk_on_lut

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
