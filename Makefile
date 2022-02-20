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
	echo "======== Run Cocotb tests for ${BENCHMARK_SUITE_NAME} ========"; \
	currDir=$${PWD} && cd ${BENCHMARK_SUITE_NAME} && \
	${PYTHON_EXEC} ../run_reg_test.py --type cocotb_test --file ${RTL_LIST_YAML} && \
	cd $${currDir} \

clean:
	echo "======== Remove all the iverilog outputs ========"; \
	find . -name '*.o' -delete
	echo "======== Remove all the cocotb tests ========"; \
	find . -type f -name '__pycache__' -delete
	find . -name 'results.xml' -delete
	find . -type f -name 'sim_build' -delete
