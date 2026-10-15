# Makefile for cocotb verification
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += mac_32.v
TOPLEVEL = mac_32
MODULE = test_mac_32

include $(shell cocotb-config --makefiles)/Makefile.sim
