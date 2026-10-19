# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += clk_gate.v

# Top-level module name
TOPLEVEL = clk_gate

# Python test module filename (without .py)
MODULE = test_clk_gate

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
