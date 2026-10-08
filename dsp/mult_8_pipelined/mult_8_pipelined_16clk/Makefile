SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += mult_8_pipelined.v
VERILOG_SOURCES += mult_8_pipelined_16clk.v

TOPLEVEL = mult_8_pipelined_16clk
MODULE   = test_mult_8_pipelined_16clk

include $(shell cocotb-config --makefiles)/Makefile.sim
