# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += rtl/ALU.v
VERILOG_SOURCES += rtl/Controller.v
VERILOG_SOURCES += rtl/IR.v
VERILOG_SOURCES += rtl/Memory.v
VERILOG_SOURCES += rtl/Mux_31.v
VERILOG_SOURCES += rtl/Mux_51.v
VERILOG_SOURCES += rtl/PC.v
VERILOG_SOURCES += rtl/Reg_1bit.v
VERILOG_SOURCES += rtl/Reg_8bit.v
VERILOG_SOURCES += rtl/RISC_core_mem_top.v
VERILOG_SOURCES += rtl/RISC_core_top.v

TOPLEVEL = RISC_core_mem_top
MODULE = test_risc_posedge_clk

include $(shell cocotb-config --makefiles)/Makefile.sim
