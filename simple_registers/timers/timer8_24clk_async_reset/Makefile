SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/timer8_Nclk_async_reset.v
VERILOG_SOURCES += $(PWD)/timer8_24clk_async_reset.v

TOPLEVEL = timer8_24clk_async_reset
MODULE   = test_timer8_24clk_async_reset

include $(shell cocotb-config --makefiles)/sim.makefile
