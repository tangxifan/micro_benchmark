# Makefile
#
SHELL = bash
PYTHON_EXEC ?= python3
BENCHMARK_SUITE_NAME = simple_gates
RTL_LIST_YAML = rtl_list.yaml

.SILENT:

rtl_list:
	echo "======== Create RTL file list for ${BENCHMARK_SUITE_NAME} ========"; \
	currDir=$${PWD} && cd ${BENCHMARK_SUITE_NAME} && \
	find . -name *.v > ${RTL_LIST_YAML} && \
	sed -i 's/$$/:/' ${RTL_LIST_YAML} && \
	cd $${currDir} \

compile:
	echo "======== Test RTL compilation for ${BENCHMARK_SUITE_NAME} ========"; \
	currDir=$${PWD} && cd ${BENCHMARK_SUITE_NAME} && \
	${PYTHON_EXEC} ../run_reg_test.py --type compile --file ${RTL_LIST_YAML} && \
	cd $${currDir} \

cocotb_test:
	echo "======== Test RTL compilation for ${BENCHMARK_SUITE_NAME} ========"; \
	currDir=$${PWD} && cd ${BENCHMARK_SUITE_NAME} && \
	${PYTHON_EXEC} ../run_reg_test.py --type cocotb_test --file ${RTL_LIST_YAML} && \
	cd $${currDir} \

clean:
	rm **/*.o
