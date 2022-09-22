# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += counterup32_1clk_async_reset_n_instances.v   

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counterup32_1clk_async_reset_n_instances    

#PLUSARGS += +define+UNIT_DELAY
MODULE = test_counterup32_1clk_async_reset_n_instances

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
