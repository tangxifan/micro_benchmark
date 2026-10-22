# Makefile

# defaults
SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += mult_32x32.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = mult_32x32

# MODULE is the basename of the Python test file
MODULE = test_mult_32x32

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
