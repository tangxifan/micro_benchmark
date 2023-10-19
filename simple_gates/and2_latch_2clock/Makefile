# Makefile

# defaults
SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += and2_latch_2clock.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = and2_latch_2clock

# MODULE is the basename of the Python test file
MODULE = test_and2_latch_2clock

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

