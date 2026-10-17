# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += cnt_8.v
VERILOG_SOURCES += pwm_cnt8.v

# Top-level module name
TOPLEVEL = pwm_cnt8

# Python test module filename (without .py)
MODULE = test_pwm_cnt8

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
