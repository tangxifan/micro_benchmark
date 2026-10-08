SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/timer8_Nclk_async_reset.v
VERILOG_SOURCES += $(PWD)/timer8_4clk_async_reset.v

TOPLEVEL = timer8_4clk_async_reset
MODULE   = test_timer8_4clk_async_reset

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
