# Simulator setup
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
#WAVES=1
COMPILE_ARGS += -DCOCOTB_SIM=1


# Design file location
VERILOG_SOURCES += counter8_4clk_async_reset.v

# Top module and Python test script names
TOPLEVEL = counter8_4clk_async_reset
MODULE   = test_counter8_4clk_async_reset

# Include cocotb build rules
include $(shell cocotb-config --makefiles)/Makefile.sim
