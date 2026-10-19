# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += counter8_negedge_async_reset.v

# Top-level module name
TOPLEVEL = counter8_negedge_async_reset

# Python test module filename (without .py)
MODULE = test_counter8_negedge_async_reset

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
