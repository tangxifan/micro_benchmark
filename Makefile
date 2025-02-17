# 
# Top Makefile
# ============
# 
# This is the top-level makefile of the project
# 
SHELL = bash
PYTHON_EXEC ?= python3
VERSION_FILE = VERSION.md
TAGGED_COMMIT_FILE = .TAGGED_COMMIT
INFRA_ROOT = ${PWD}/utils/
VERSION_BUMP_TYPE = minor
FORCE_COMMIT_VERSION_UPDATE = off
BENCHMARK_SUITE_NAME = simple_gates
UTIL_DIR = utils
UTIL_SCRIPT_DIR = ${UTIL_DIR}/scripts
UTIL_TASK_DIR = ${UTIL_DIR}/tasks
RTL_LIST_YAML = ${UTIL_TASK_DIR}/${BENCHMARK_SUITE_NAME}_rtl_list.yaml

# Format executables
PYTHON_FORMAT_EXEC ?= black
BENCHMARK_SUITE_LIST = "simple_gates" "simple_registers" "fsm" "dsp" "interface" "processors" "ram"

NUM_JOBS=4
IVERILOG_TEMP_DIR = _iverilog_temp

# VexRiscV
TMP_VEXRISC5 = _tmp_vexrisc5
VEXRISC5_GIT_URL = https://github.com/SpinalHDL/VexRiscv.git
VEXRISC5_RTL = VexRiscv.v
VEXRISC5_LDIR_PREFIX = ${PWD}/processors/VexRiscv
VEXRISC5S_LDIR= ${VEXRISC5_LDIR_PREFIX}_small/rtl/
VEXRISC5F_LDIR= ${VEXRISC5_LDIR_PREFIX}_full/rtl/
VEXRISC5_MURAX_RTL = Murax.v
VEXRISC5_MURAX_LDIR= ${VEXRISC5_LDIR_PREFIX}_murax/rtl/

# Verilog-SPI
TMP_VSPI = _tmp_vspi
VSPI_GIT_URL = https://github.com/janschiefer/verilog_spi.git
VSPI_LDIR_PREFIX = ${PWD}/interface/verilog_spi
VSPI_RTL_FLIST = "clock_divider.v" "neg_edge_det.v" "pos_edge_det.v" "spi2.v" "spi_module.v"
VSPI_TB_FLIST = "testbench.v"
VSPI_MISC_FLIST = "README.md" "LICENSE"
VSPI_LDIR_RTL = ${VSPI_LDIR_PREFIX}/rtl/
VSPI_LDIR_TB = ${VSPI_LDIR_PREFIX}/testbench/

# DSP filters
TMP_DSPFLT = _tmp_dspfilter
DSPFLT_GIT_URL = https://github.com/ZipCPU/dspfilters.git
DSPFLT_LDIR_PREFIX = ${PWD}/dsp/dspfilters
DSPFLT_RTL_FLIST = "boxcar.v" "delayw.v" "fastfir.v" "genericfir.v" "iiravg.v" "lfsr_gal.v" "ratfil.v" "slowfil_srl.v" "slowsymf.v" "subfildown.v" "cheapspectral.v" "dspswitch.v" "firtap.v" "histogram.v" "lfsr_fib.v" "lfsr.v" "shalfband.v" "slowfil.v" "smplfir.v"
DSPFLT_MISC_FLIST = "README.md"
DSPFLT_LDIR_RTL = ${DSPFLT_LDIR_PREFIX}/rtl/

# CORDIC
TMP_CORDIC = _tmp_cordic
CORDIC_GIT_URL = https://github.com/ZipCPU/cordic.git
CORDIC_LDIR_PREFIX = ${PWD}/dsp/cordic
CORDIC_RTL_FLIST = "cordic.v" "quadtbl_ltbl.hex" "quadtbl.v" "quarterwav.v" "seqpolar.v" "sintable.v" "quadtbl_ctbl.hex" "quadtbl_qtbl.hex" "quarterwav.hex" "seqcordic.v" "sintable.hex" "topolar.v"
CORDIC_MISC_FLIST = "README.md"
CORDIC_LDIR_RTL = ${CORDIC_LDIR_PREFIX}/rtl/

# wbi2c
TMP_WBI2C = _tmp_wbi2c
WBI2C_GIT_URL = https://github.com/ZipCPU/wbi2c.git
WBI2C_LDIR_PREFIX = ${PWD}/interface/wbi2c
WBI2C_RTL_FLIST = "axili2ccpu.v" "axisi2c.v" "lli2cm.v" "wbi2ccpu.v" "wbi2cmaster.v" "wbi2cslave.v"
WBI2C_MISC_FLIST = "README.md"
WBI2C_LDIR_RTL = ${WBI2C_LDIR_PREFIX}/rtl/

# wbuart32
TMP_WBURT32 = _tmp_wbuart32
WBURT32_GIT_URL = https://github.com/ZipCPU/wbuart32.git
WBURT32_LDIR_PREFIX = ${PWD}/interface/wbuart32
WBURT32_RTL_FLIST = "axiluart.v" "rxuart.v" "rxuartlite.v" "skidbuffer.v" "txuart.v" "txuartlite.v" "ufifo.v" "wbuart-insert.v" "wbuart.v"
WBURT32_MISC_FLIST = "README.md" "LICENSE"
WBURT32_LDIR_RTL = ${WBURT32_LDIR_PREFIX}/rtl/

# wbspi-master
TMP_WBSPIM = _tmp_wbspim
WBSPIM_GIT_URL = https://github.com/daringpatil3134/SPI_Serial_Peripheral_Interface_Verilog_Modules.git
WBSPIM_LDIR_PREFIX = ${PWD}/interface/wbspi_master
WBSPIM_RTL_FLIST = "spi_clgen.v" "spi_defines.v" "spi_shift_reg.v" "spi_slave.v" "spi_top.v" "wishbone_master.v"
WBSPIM_MISC_FLIST = "README.md" "LICENSE"
WBSPIM_LDIR_RTL = ${WBSPIM_LDIR_PREFIX}/rtl/

# uberddr3
TMP_UBERDDR3 = _tmp_uberddr
UBERDDR3_GIT_URL = https://github.com/AngeloJacobo/UberDDR3.git
UBERDDR3_LDIR_PREFIX = ${PWD}/interface/uberddr3
UBERDDR3_RTL_FLIST = "ddr3_controller.v" "ddr3_phy.v" "ddr3_top.v"
UBERDDR3_MISC_FLIST = "README.md" "LICENSE"
UBERDDR3_LDIR_RTL = ${UBERDDR3_LDIR_PREFIX}/rtl/

# rs-485
TMP_RS485 = _tmp_rs485
RS485_GIT_URL = https://github.com/baseli/RS-485.git
RS485_LDIR_PREFIX = ${PWD}/interface/rs485
RS485_RTL_FLIST = "clkdiv.v" "clkdiv_9600.v" "crccheck.v" "deletezero.v" "hdlc_recivedata.v" "hdlc_senddata.v" "insertzero.v" "rs_top.v" "rsrx.v" "rstx.v" "rx.v" "tx.v"
RS485_TB_FLIST = "deletezero_tb.v" "hdlc_recivedata_tb.v" "hdlc_senddata_tb.v" "insertzero_tb.v" "rs_top_tb.v"
RS485_MISC_FLIST = "README.md"
RS485_LDIR_RTL = ${RS485_LDIR_PREFIX}/rtl/
RS485_LDIR_TB = ${RS485_LDIR_PREFIX}/testbench/

.SILENT:

# Put it first so that "make" without argument is like "make help".
export COMMENT_EXTRACT

# Put it first so that "make" without argument is like "make help".
help:
	@${PYTHON_EXEC} -c "$$COMMENT_EXTRACT"

compile:
# This command compiles the RTL designss under a given specific benchmark suite name
# This command uses the RTL list generated by the ``rtl_list`` target
	echo "======== Test RTL compilation for ${BENCHMARK_SUITE_NAME} ========"; \
	${PYTHON_EXEC} ${UTIL_SCRIPT_DIR}/run_compile_test.py --file ${RTL_LIST_YAML} --temp_dir ${IVERILOG_TEMP_DIR}

cocotb_test:
# This command run HDL simulations for the RTL designss with cocotb testbenches under a given specific benchmark suite name
# This command uses the RTL list generated by the ``rtl_list`` target
	echo "======== Run Cocotb tests for ${BENCHMARK_SUITE_NAME} ========"; \
	${PYTHON_EXEC} ${UTIL_SCRIPT_DIR}/run_cocotb_test.py --file ${RTL_LIST_YAML} --new_thread_wait_time 0.1 --j ${NUM_JOBS}

clean:
# This command removes all the intermediate files during rtl compilation and cocotb verification 
	echo "======== Remove all the iverilog outputs ========"; \
	find . -name '*.o' -delete
	rm -rf ${IVERILOG_TEMP_DIR}
	echo "======== Remove all the cocotb tests ========"; \
	find . -type f -name '__pycache__' -delete
	find . -name 'results.xml' -delete
	find . -name 'cocotb_sim.log' -delete
	find . -type f -name 'sim_build' -delete

vexriscv:
# This command will checkout the latest VexRiscV, then update RTL and testbenches
	echo "==== Clone latest VexRiscV from github repo: ${VEXRISC5_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_VEXRISC5} && \
	git clone ${VEXRISC5_GIT_URL} ${TMP_VEXRISC5} && \
    cd ${TMP_VEXRISC5} && \
	echo "==== Generate VexRiscV small version and update local copy ====" && \
	sbt "runMain vexriscv.demo.GenSmallest" && mkdir -p ${VEXRISC5S_LDIR} && cp ${VEXRISC5_RTL} ${VEXRISC5S_LDIR} && \
	echo "==== Generate VexRiscV full version and update local copy ====" && \
	sbt "runMain vexriscv.demo.GenFull" && mkdir -p ${VEXRISC5F_LDIR} && cp ${VEXRISC5_RTL} ${VEXRISC5F_LDIR} && \
	echo "==== Generate VexRiscV Murax and update local copy ====" && \
	sbt "runMain vexriscv.demo.Murax" && mkdir -p ${VEXRISC5_MURAX_LDIR} && cp ${VEXRISC5_MURAX_RTL} ${VEXRISC5_MURAX_LDIR} && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${VEXRISC5_LDIR_PREFIX}* && \
	echo "==== Done ====" || exit 1;

verilog-spi:
# This command will checkout the latest SPI, then update RTL and testbenches
	echo "==== Clone latest verilog-spi from github repo: ${VSPI_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_VSPI} && \
	git clone ${VSPI_GIT_URL} ${TMP_VSPI} && \
    cd ${TMP_VSPI} && \
	echo "==== Update RTL ====" && \
	mkdir -p ${VSPI_LDIR_RTL} && \
	for f in ${VSPI_RTL_FLIST} ; \
	do cp $${f} ${VSPI_LDIR_RTL} || exit 1; \
	done && \
	echo "==== Update Testbench ====" && \
	mkdir -p ${VSPI_LDIR_TB} && \
	for f in ${VSPI_TB_FLIST} ; \
	do cp $${f} ${VSPI_LDIR_TB} || exit 1; \
	done && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${VSPI_LDIR_PREFIX} && \
	for f in ${VSPI_MISC_FLIST} ; \
	do cp $${f} ${VSPI_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${VSPI_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${VSPI_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

dspfilters:
# This command will checkout the latest DSP filters, then update RTL and testbenches
	echo "==== Clone latest dspfilters from github repo: ${DSPFLT_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_DSPFLT} && \
	git clone ${DSPFLT_GIT_URL} ${TMP_DSPFLT} && \
    cd ${TMP_DSPFLT}/rtl && \
	echo "==== Update RTL ====" && \
	mkdir -p ${DSPFLT_LDIR_RTL} && \
	for f in ${DSPFLT_RTL_FLIST}; \
	do cp $${f} ${DSPFLT_LDIR_RTL} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Documentation ====" && \
    cd ${TMP_DSPFLT} && \
	mkdir -p ${DSPFLT_LDIR_PREFIX} && \
	for f in ${DSPFLT_MISC_FLIST} ; \
	do cp $${f} ${DSPFLT_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${DSPFLT_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${DSPFLT_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

cordic:
# This command will checkout the latest cordic designs, then update RTL and testbenches
	echo "==== Clone latest cordic from github repo: ${CORDIC_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_CORDIC} && \
	git clone ${CORDIC_GIT_URL} ${TMP_CORDIC} && \
    cd ${TMP_CORDIC}/rtl && \
	echo "==== Update RTL ====" && \
	mkdir -p ${CORDIC_LDIR_RTL} && \
	for f in ${CORDIC_RTL_FLIST}; \
	do cp $${f} ${CORDIC_LDIR_RTL} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${CORDIC_LDIR_PREFIX} && \
	for f in ${CORDIC_MISC_FLIST} ; \
	do cp $${f} ${CORDIC_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${CORDIC_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${CORDIC_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

wbi2c:
# This command will checkout the latest Wishbone-I2C, then update RTL and testbenches
	echo "==== Clone latest wbi2c from github repo: ${WBI2C_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_WBI2C} && \
	git clone ${WBI2C_GIT_URL} ${TMP_WBI2C} && \
    cd ${TMP_WBI2C}/rtl && \
	echo "==== Update RTL ====" && \
	mkdir -p ${WBI2C_LDIR_RTL} && \
	for f in ${WBI2C_RTL_FLIST} ; \
	do cp $${f} ${WBI2C_LDIR_RTL} || exit 1; \
	done && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${WBI2C_LDIR_PREFIX} && \
	for f in ${WBI2C_MISC_FLIST} ; \
	do cp $${f} ${WBI2C_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${WBI2C_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${WBI2C_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

wbuart32:
# This command will checkout the latest Wishbone-uart, then update RTL and testbenches
	echo "==== Clone latest wbuart32 from github repo: ${WBURT32_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_WBURT32} && \
	git clone ${WBURT32_GIT_URL} ${TMP_WBURT32} && \
    cd ${TMP_WBURT32}/rtl && \
	echo "==== Update RTL ====" && \
	mkdir -p ${WBURT32_LDIR_RTL} && \
	for f in ${WBURT32_RTL_FLIST} ; \
	do cp $${f} ${WBURT32_LDIR_RTL} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${WBURT32_LDIR_PREFIX} && \
	for f in ${WBURT32_MISC_FLIST} ; \
	do cp $${f} ${WBURT32_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${WBURT32_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${WBURT32_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

wbspi_master:
# This command will checkout the latest Wishbone-spi-master, then update RTL and testbenches
	echo "==== Clone latest wbspi_master from github repo: ${WBSPIM_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_WBSPIM} && \
	git clone ${WBSPIM_GIT_URL} ${TMP_WBSPIM} && \
    cd ${TMP_WBSPIM} && \
	echo "==== Update RTL ====" && \
	mkdir -p ${WBSPIM_LDIR_RTL} && \
	for f in ${WBSPIM_RTL_FLIST} ; \
	do cp $${f} ${WBSPIM_LDIR_RTL} || exit 1; \
	done && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${WBSPIM_LDIR_PREFIX} && \
	for f in ${WBSPIM_MISC_FLIST} ; \
	do cp $${f} ${WBSPIM_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${WBSPIM_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${WBSPIM_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

uberddr3:
# This command will checkout the latest UberDDR3, then update RTL and testbenches
	echo "==== Clone latest UberDDR3 from github repo: ${UBERDDR3_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_UBERDDR3} && \
	git clone ${UBERDDR3_GIT_URL} ${TMP_UBERDDR3} && \
    cd ${TMP_UBERDDR3}/rtl && \
	echo "==== Update RTL ====" && \
	mkdir -p ${UBERDDR3_LDIR_RTL} && \
	for f in ${UBERDDR3_RTL_FLIST} ; \
	do cp $${f} ${UBERDDR3_LDIR_RTL} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${UBERDDR3_LDIR_PREFIX} && \
	for f in ${UBERDDR3_MISC_FLIST} ; \
	do cp $${f} ${UBERDDR3_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${UBERDDR3_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${UBERDDR3_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;

rs485:
# This command will checkout the latest RS485, then update RTL and testbenches
	echo "==== Clone latest rs485 from github repo: ${RS485_GIT_URL} ====" && \
	currDir=$${PWD} && rm -rf ${TMP_RS485} && \
	git clone ${RS485_GIT_URL} ${TMP_RS485} && \
    cd ${TMP_RS485}/code && \
	echo "==== Update RTL ====" && \
	mkdir -p ${RS485_LDIR_RTL} && \
	for f in ${RS485_RTL_FLIST} ; \
	do cp $${f} ${RS485_LDIR_RTL} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Testbench ====" && \
    cd ${TMP_RS485}/simulate && \
	mkdir -p ${RS485_LDIR_TB} && \
	for f in ${RS485_TB_FLIST} ; \
	do cp $${f} ${RS485_LDIR_TB} || exit 1; \
	done && cd $${currDir} && \
	echo "==== Update Documentation ====" && \
	mkdir -p ${RS485_LDIR_PREFIX} && \
	for f in ${RS485_MISC_FLIST} ; \
	do cp $${f} ${RS485_LDIR_PREFIX} || exit 1; \
	done && \
	echo `git rev-parse HEAD` > ${RS485_LDIR_PREFIX}/VERSION.md && \
	cd $${currDir} && \
	echo "==== Update git track list ====" && \
	git add ${RS485_LDIR_PREFIX} && \
	echo "==== Done ====" || exit 1;


update_version:
# Update the patch count in the version number
	echo "======== Bump up patch count in the version number ========"; \
	${PYTHON_EXEC} ${INFRA_ROOT}/scripts/version_updater.py --version_file ${VERSION_FILE} --tagged_commit ${TAGGED_COMMIT_FILE} --force_commit ${FORCE_COMMIT_VERSION_UPDATE}	

release_version:
# Update the patch count in the version number
	echo "======== Bump up release in the version number ========"; \
	${PYTHON_EXEC} ${INFRA_ROOT}/scripts/version_updater.py --version_file ${VERSION_FILE} --tagged_commit ${TAGGED_COMMIT_FILE} --release --bump_type ${VERSION_BUMP_TYPE}	

generate_initial_tagged_commit:
# Create the first version of tagged commit file, used for version update
	git rev-list --max-parents=0 --abbrev-commit HEAD > ${TAGGED_COMMIT_FILE}

format-py:
# Format all the python scripts under this project, excluding submodule and symbolic links
	for f in `find ${BENCHMARK_SUITE_LIST} -type f -iname *.py`; \
	do \
	${PYTHON_FORMAT_EXEC} $${f} --line-length 100 || exit 1; \
	done

check-format-py:
# Check if all the python files are in the expected format
	${INFRA_ROOT}/scripts/check-format.sh -py

# Functions to extract comments from Makefiles
define COMMENT_EXTRACT
import re
with open ('Makefile', 'r' ) as f:
    matches = re.finditer('^([a-zA-Z-_0-9]*):.*\n#(.*)', f.read(), flags=re.M)
    for _, match in enumerate(matches, start=1):
        header, content = match[1], match[2]
        print(f"  {header:10} {content}")
endef
