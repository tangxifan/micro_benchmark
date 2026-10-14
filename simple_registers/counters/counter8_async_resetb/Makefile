# Simulator setup
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Design file location
VERILOG_SOURCES += counter8_async_resetb.v

# Top module and Python test script names
TOPLEVEL = counter8_async_resetb
MODULE   = test_counter8_async_resetb

# Include cocotb build rules
include $(shell cocotb-config --makefiles)/Makefile.sim
