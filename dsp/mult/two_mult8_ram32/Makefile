# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (top module and submodules)
VERILOG_SOURCES += two_mult8_ram32.v
VERILOG_SOURCES += dual_port_ram_16k.v

# Top-level module name
TOPLEVEL = two_mult8_ram32

# Python test module filename (without .py)
MODULE = test_two_mult8_ram32

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
