# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += routing_test.v

# Top-level module name
TOPLEVEL = routing_test

# Python test module name (without .py)
MODULE = test_routing_test

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
