SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/mult_8_pipelined_Nclk.v
VERILOG_SOURCES += $(PWD)/mult_8_pipelined_32clk.v

TOPLEVEL = mult_8_pipelined_32clk
MODULE   = test_mult_8_pipelined_32clk

include $(shell cocotb-config --makefiles)/Makefile.sim
