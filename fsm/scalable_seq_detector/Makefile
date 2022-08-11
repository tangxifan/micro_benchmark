# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += scalable_seq_detector.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = scalable_seq_detector

# MODULE is the basename of the Python test file
MODULE = test_scalable_seq_detector

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
