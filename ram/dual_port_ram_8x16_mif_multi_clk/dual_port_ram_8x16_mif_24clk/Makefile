SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/dual_port_ram_8x16_mif_Nclk.v
VERILOG_SOURCES += $(PWD)/dual_port_ram_8x16_mif_24clk.v

TOPLEVEL = dual_port_ram_8x16_mif_24clk
MODULE   = test_dual_port_ram_8x16_mif_24clk

include $(shell cocotb-config --makefiles)/sim.makefile
