# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += reset_generator.v

# Top-level module name
TOPLEVEL = reset_generator

# Python test module filename (without .py)
MODULE = test_reset_generator

# Compiler flags enabling SystemVerilog features and Vivado synthesis define
COMPILE_ARGS += -g2012 -DVIVADO_SYNTHESIS

# Pass non-zero parameter overrides to allow active cycle counting
COMPILE_ARGS += -P$(TOPLEVEL).ACTIVE_CYCLES=10 -P$(TOPLEVEL).INITIAL_VALUE=0

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
