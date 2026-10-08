SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/counter8_Nclk_async_reset.v
VERILOG_SOURCES += $(PWD)/counter8_32clk_async_reset.v

TOPLEVEL = counter8_32clk_async_reset
MODULE   = test_counter8_32clk_async_reset

include $(shell cocotb-config --makefiles)/Makefile.sim
