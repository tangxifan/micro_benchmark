# Makefile for running cocotb simulation of SAPone with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (include SAPone and all necessary underlying modules)
VERILOG_SOURCES += rtl/ACC.v
VERILOG_SOURCES += rtl/ADDSUB.v
VERILOG_SOURCES += rtl/BRegister.v
VERILOG_SOURCES += rtl/Controller.v
VERILOG_SOURCES += rtl/IR.v
VERILOG_SOURCES += rtl/MAR.v
VERILOG_SOURCES += rtl/OutputRegister.v
VERILOG_SOURCES += rtl/PC.v
VERILOG_SOURCES += rtl/ROM.v
VERILOG_SOURCES += rtl/SAPone.v

# Top-level module name matching the top entity in SAPone design
TOPLEVEL = SAPone

# Python test module name (without .py)
MODULE = test_sapone

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
