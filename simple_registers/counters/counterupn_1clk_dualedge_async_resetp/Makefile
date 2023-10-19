
# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += counterupn_1clk_dualedge_async_resetp.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counterupn_1clk_dualedge_async_resetp

#PLUSARGS += +define+UNIT_DELAY
MODULE = test_counterupn_1clk_dualedge_async_resetp

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
