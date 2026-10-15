# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (include both fifo and the underlying RAM primitive)
VERILOG_SOURCES += fifo.v
VERILOG_SOURCES += sync_dual_port_ram.v

# Top-level module name
TOPLEVEL = fifo

# Python test module name (without .py)
MODULE = test_fifo

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
