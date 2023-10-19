# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += counterup8_1clk_async_resetp.v
VERILOG_SOURCES += counterup10_1clk_async_resetp.v
VERILOG_SOURCES += counterup12_1clk_async_resetp.v
VERILOG_SOURCES += counterup16_1clk_async_resetp.v
VERILOG_SOURCES += counterup36_8_2clk_async_resetp.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counterup36_8_2clk_async_resetp

# MODULE is the basename of the Python test file
MODULE = test_counterup36_8_2clk_async_resetp

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

