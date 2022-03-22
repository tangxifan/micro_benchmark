# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += counterup16_1clk_posedge_async_resetn.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counterup16_1clk_posedge_async_resetn

# MODULE is the basename of the Python test file
MODULE = test_counterup16_1clk_posedge_async_resetn

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

