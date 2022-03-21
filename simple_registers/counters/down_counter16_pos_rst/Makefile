# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += down_counter16_pos_rst.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = down_counter16_pos_rst

# MODULE is the basename of the Python test file
MODULE = test_down_counter16_pos_rst

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

