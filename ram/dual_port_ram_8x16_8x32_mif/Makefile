# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += dual_port_ram_8x16_8x32_mif.v

# Top-level module name
TOPLEVEL = dual_port_ram_8x16_8x32

# Python test module filename (without .py)
MODULE = test_dual_port_ram_8x16_8x32_mif

# Preprocess hex files in the root directory so iverilog finds them at runtime
all: preprocess_hex

preprocess_hex:
	@grep -v '^[[:space:]]*//' $(PWD)/init_8x16.hex | \
		sed 's/^[[:space:]]*\([0-9a-fA-F]\+\)[[:space:]]\+\(0x[0-9a-fA-F]*\)/@\1 \2/g' > sim_build/init_8x16.hex
	@grep -v '^[[:space:]]*//' $(PWD)/init_8x32.hex | \
		sed 's/^[[:space:]]*\([0-9a-fA-F]\+\)[[:space:]]\+\(0x[0-9a-fA-F]*\)/@\1 \2/g' > sim_build/init_8x32.hex

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
