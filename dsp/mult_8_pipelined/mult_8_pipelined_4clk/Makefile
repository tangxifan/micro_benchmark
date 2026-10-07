SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/mult_8_pipelined_Nclk.v
VERILOG_SOURCES += $(PWD)/mult_8_pipelined_4clk.v

TOPLEVEL = mult_8_pipelined_4clk
MODULE   = test_mult_8_pipelined_4clk

include $(shell cocotb-config --makefiles)/sim.makefile
