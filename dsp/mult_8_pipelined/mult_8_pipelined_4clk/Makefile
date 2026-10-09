SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += mult_8_pipelined.v
VERILOG_SOURCES += mult_8_pipelined_4clk.v

TOPLEVEL = mult_8_pipelined_4clk
MODULE   = test_mult_8_pipelined_4clk

include $(shell cocotb-config --makefiles)/Makefile.sim
