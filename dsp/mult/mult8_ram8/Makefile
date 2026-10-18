# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (top module and submodules)
VERILOG_SOURCES += mult8_ram8.v
VERILOG_SOURCES += dual_port_ram_1k.v

# Top-level module name
TOPLEVEL = mult8_ram8

# Python test module filename (without .py)
MODULE = test_mult8_ram8

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
