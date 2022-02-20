# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += and2.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = and2

# MODULE is the basename of the Python test file
MODULE = test_and2

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

