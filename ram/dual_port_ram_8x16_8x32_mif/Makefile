# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (including sub-cores)
VERILOG_SOURCES += dual_port_ram_8x16_8x32_mif.v

# Top-level module name
TOPLEVEL = dual_port_ram_8x16_8x32

# Python test module name (without .py)
MODULE = test_dual_port_ram_8x16_8x32_mif

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
