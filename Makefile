# Makefile
#
SHELL = bash
PYTHON_EXEC = python3

.SILENT:

rtl_compilation:
	${PYTHON_EXEC} run_reg_test.py --file regression_tasks/rtl_tasks.yaml

clean:
	rm **/*.o
