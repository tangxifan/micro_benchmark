# Makefile

# defaults
SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += mult_2x2.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = mult_2x2

# MODULE is the basename of the Python test file
MODULE = test_mult_2x2

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
