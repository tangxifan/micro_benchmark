# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += adder_8.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = adder_8

# MODULE is the basename of the Python test file
MODULE = test_adder_8

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

