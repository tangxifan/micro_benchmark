# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += multi_driver.v

# Top-level module name
TOPLEVEL = multi_driver

# Python test module filename (without .py)
MODULE = test_multi_driver

# Include cocotb standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
