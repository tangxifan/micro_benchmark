SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += counter8_async_reset.v
VERILOG_SOURCES += counter8_16clk_async_reset.v

TOPLEVEL = counter8_16clk_async_reset
MODULE   = test_counter8_16clk_async_reset

include $(shell cocotb-config --makefiles)/Makefile.sim
