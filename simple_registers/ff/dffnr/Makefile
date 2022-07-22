# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += dffnr.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = dffnr

# MODULE is the basename of the Python test file
MODULE = test_dffnr

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

