# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += dual_port_ram_8x16_8x32_mif.v

# Top-level module name
TOPLEVEL = dual_port_ram_8x16_8x32

# Python test module filename (without .py)
MODULE = test_dual_port_ram_8x16_8x32_mif

# Pass the correct filename parameters to iverilog and format hex files
# (This injects @<index> format into sim_build copies without altering your repo files)
COMPILED_LANG=verilog
#EXTRA_ARGS += -DPARAM_FILE_16=init_8x16.hex -DPARAM_FILE_32=init_8x32.hex

all: copy_hex

copy_hex:
	@mkdir -p sim_build
	# Copy and transform files: prepend '@' to index numbers so $readmemh reads them correctly
	@sed 's/^[[:space:]]*\([0-9a-fA-F]\+\)[[:space:]]\+\(0x[0-9a-fA-F]*\)/@\1 \2/g' $(PWD)/init_8x16.hex > sim_build/init_8x16_2.hex
	@sed 's/^[[:space:]]*\([0-9a-fA-F]\+\)[[:space:]]\+\(0x[0-9a-fA-F]*\)/@\1 \2/g' $(PWD)/init_8x32.hex > sim_build/init_8x32_2.hex
	# Also alias them to default names just in case
	@cp sim_build/init_8x16_2.hex sim_build/init_8x16.hex
	@cp sim_build/init_8x32_2.hex sim_build/init_8x32.hex

include $(shell cocotb-config --makefiles)/Makefile.sim
