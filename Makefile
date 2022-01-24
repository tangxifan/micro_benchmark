# Makefile
#
SHELL = bash
PYTHON_EXEC = python3

.SILENT:

compile_rtl:
	${PYTHON_EXEC} run_reg_test.py --file regression_tasks/rtl_tasks.yaml

clean:
	rm **/*.o
