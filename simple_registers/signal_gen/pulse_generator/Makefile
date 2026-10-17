# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += pulse_generator.v

# Top-level module name
TOPLEVEL = pulse_generator

# Python test module filename (without .py)
MODULE = test_pulse_generator

# Compiler flags for Icarus
COMPILE_ARGS += -g2012 -DVIVADO_SYNTHESIS

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
