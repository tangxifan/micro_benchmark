SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/mult_8_pipelined_Nclk.v
VERILOG_SOURCES += $(PWD)/mult_8_pipelined_16clk.v

TOPLEVEL = mult_8_pipelined_16clk
MODULE   = test_mult_8_pipelined_16clk

include $(shell cocotb-config --makefiles)/sim.makefile
