# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files (order matters for dependencies/includes)
VERILOG_SOURCES += EFX_RAM_5K.v
VERILOG_SOURCES += clock_divider.v
VERILOG_SOURCES += reset_generator.v
VERILOG_SOURCES += bitstream_loader.v
VERILOG_SOURCES += configuration_manager.v

TOPLEVEL = configuration_manager
MODULE = test_configuration_manager

include $(shell cocotb-config --makefiles)/Makefile.sim
