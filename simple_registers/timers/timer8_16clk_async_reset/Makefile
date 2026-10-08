SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += timer8_async_reset.v
VERILOG_SOURCES += timer8_16clk_async_reset.v

TOPLEVEL = timer8_16clk_async_reset
MODULE   = test_timer8_16clk_async_reset

include $(shell cocotb-config --makefiles)/Makefile.sim
