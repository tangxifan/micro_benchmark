SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += dual_port_ram_8x16_mif.v
VERILOG_SOURCES += dual_port_ram_8x16_mif_32clk.v

TOPLEVEL = dual_port_ram_8x16_mif_32clk
MODULE   = test_dual_port_ram_8x16_mif_32clk

include $(shell cocotb-config --makefiles)/Makefile.sim
