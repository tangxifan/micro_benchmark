# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += dual_port_ram_8x16_8x32_mif.v
TOPLEVEL = dual_port_ram_8x16_8x32
MODULE = test_dual_port_ram_8x16_8x32_mif

# Hook to copy .hex files into sim_build before running
all: copy_hex

copy_hex:
	@mkdir -p sim_build
	@cp $(PWD)/*.hex sim_build/

include $(shell cocotb-config --makefiles)/Makefile.sim
