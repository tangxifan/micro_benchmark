# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += dual_port_ram_1k.v

# Top-level module name
TOPLEVEL = dual_port_ram_1k

# Python test module name (without .py)
MODULE = test_dual_port_ram_1k

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
