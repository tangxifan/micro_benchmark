SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/mult_8_pipelined_Nclk.v
VERILOG_SOURCES += $(PWD)/mult_8_pipelined_24clk.v

TOPLEVEL = mult_8_pipelined_24clk
MODULE   = test_mult_8_pipelined_24clk

include $(shell cocotb-config --makefiles)/sim.makefile
