# Makefile
#
SHELL = bash
PYTHON_EXEC ?= python3
BENCHMARK_SUITE_NAME = simple_gates

.SILENT:

compile:
	cd ${BENCHMARK_SUITE_NAME} && \
	${PYTHON_EXEC} ../run_reg_test.py --file rtl_list.yaml

clean:
	rm **/*.o
