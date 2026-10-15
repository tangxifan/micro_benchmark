# Simulator setup
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Design file location
VERILOG_SOURCES += counter8_sync_reset.v

# Top module and Python test script names
TOPLEVEL = counter8_sync_reset
MODULE   = test_counter8_sync_reset

# Include cocotb build rules
include $(shell cocotb-config --makefiles)/Makefile.sim
