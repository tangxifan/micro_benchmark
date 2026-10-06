# Makefile

# defaults
SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += rst_sync.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = rst_sync

# MODULE is the basename of the Python test file
MODULE = test_rst_sync

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

