# Makefile for running cocotb simulation with Icarus Verilog

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Source files
VERILOG_SOURCES += dual_port_ram_8x32_mif.v

# Top-level module name
TOPLEVEL = dual_port_ram_8x32

# Python test module filename (without .py)
MODULE = test_dual_port_ram_8x32

# Preprocess init.hex in the root directory so iverilog finds it at runtime
all: preprocess_hex

preprocess_hex:
	@grep -v '^[[:space:]]*//' $(PWD)/init.hex | \
		sed 's/^[[:space:]]*\([0-9a-fA-F]\+\)[[:space:]]\+\(0x[0-9a-fA-F]*\)/@\1 \2/g' > $(PWD)/init.hex.tmp
	@mv $(PWD)/init.hex.tmp $(PWD)/init.hex

# Clean up generated temporary file on make clean
clean::
	@rm -f $(PWD)/init.hex

# Include cocotb's standard Makefile rules
include $(shell cocotb-config --makefiles)/Makefile.sim
