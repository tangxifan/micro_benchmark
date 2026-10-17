# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += clk_cond.v

# Top-level module name
TOPLEVEL = clk_cond

# Python test module name (without .py)
MODULE = test_clk_cond

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
