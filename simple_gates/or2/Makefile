# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += or2.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = or2

# MODULE is the basename of the Python test file
MODULE = test_or2

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

