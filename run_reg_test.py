#####################################################################
# A script to run regression tests for all the benchmarks
#####################################################################
import os
from os.path import dirname, abspath
import argparse
import logging
import subprocess
import tarfile
import yaml
import re

#####################################################################
# Error codes
#####################################################################
error_codes = {
  "SUCCESS": 0,
  "ERROR": 1, 
  "FILE_ERROR": 2 
}

#####################################################################
# Initialize logger 
#####################################################################
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO);

#####################################################################
# Compile a RTL with iVerilog
#####################################################################
def run_iverilog_for_rtl_file(rtl_file):
  status = 0
  include_dir = os.path.dirname(rtl_file)
  cmd = "iverilog " + rtl_file + " -o " + rtl_file + ".o" + " -y " + include_dir
  process = subprocess.run(cmd, shell=True, check=True)
  status = process.returncode
  return status

#####################################################################
# Run cocotb Makefile for a given RTL
#####################################################################
def run_cocotb_for_rtl_file(rtl_file):
  status = 0
  curr_dir = os.getcwd()
  include_dir = os.path.dirname(rtl_file)
  os.chdir(include_dir)
  cmd = "make"
  make_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  status = error_codes["SUCCESS"]
  if (make_process.wait()) != 0:
    status = error_codes["ERROR"]
  os.chdir(curr_dir)
  return status

#####################################################################
# Check cocotb results file and report any failures captured
#####################################################################
def check_cocotb_results(rtl_file):
  status = 0
  include_dir = os.path.dirname(rtl_file)
  result_f = open(include_dir + "/results.xml", "r")
  for line in result_f:
    if re.search("failure", line):
      status += 1
  return status

#####################################################################
# For each RTL file in the list,
# - compile with iVerilog
#####################################################################
def test_rtl_list(file_db):
  num_failures = 0
  space_limit = 80 # Maximum space tuned for the screen width
  for rtl in file_db.keys():
    # Find bitfile dirpath
    # Create a space when logging
    logging_space = " " + "." * (space_limit - len(rtl) - 2) + " "
    status = run_iverilog_for_rtl_file(rtl)
    num_failures = num_failures + status; 
    if (status == 0):
      logging.info(rtl + logging_space + "[Pass]")
    else:
      logging.info(rtl + logging_space + "[Fail]")
  return num_failures

#####################################################################
# For each RTL file in the list,
# - Run cocotb tests
#####################################################################
def test_cocotb_rtl_list(file_db):
  num_failures = 0
  space_limit = 80 # Maximum space tuned for the screen width
  for rtl in file_db.keys():
    # Find bitfile dirpath
    # Create a space when logging
    logging_space = " " + "." * (space_limit - len(rtl) - 2) + " "
    status = run_cocotb_for_rtl_file(rtl)
    status = check_cocotb_results(rtl)
    num_failures = num_failures + status; 
    if (status == 0):
      logging.info(rtl + logging_space + "[Pass]")
    else:
      logging.info(rtl + logging_space + "[Fail]")
  return num_failures

#####################################################################
# Read file database to a yaml file
#####################################################################
def read_yaml_to_file_db(yaml_filename):
  file_db = {}
  with open(yaml_filename, 'r') as stream:
    try:
      file_db = yaml.load(stream, Loader=yaml.FullLoader)
      logging.info("Found " + str(len(file_db)) + " files to test")
    except yaml.YAMLError as exc:
      logging.error(exc)
      exit(error_codes["FILE_ERROR"]);

  return file_db

#####################################################################
# Write file database to a yaml file
#####################################################################
def write_file_db_to_yaml(file_db, yaml_filename):
  with open(yaml_filename, 'w') as yaml_file:
    yaml.dump(file_db, yaml_file, default_flow_style=False)

#####################################################################
# Main function
#####################################################################
if __name__ == '__main__':
  # Execute when the module is not initialized from an import statement

  # Parse the options and apply sanity checks
  parser = argparse.ArgumentParser(description='Run regression tests for RTL benchmarks')
  parser.add_argument('--type',
                      required=True,
                      help='Describe the type of test to run [compile|cocotb_test]')
  parser.add_argument('--file_list',
                      required=True,
                      help='A file contains a list of RTL files to test')
  args = parser.parse_args()

  # Create an empty database
  file_db = {}

  # Test all the files
  file_db = read_yaml_to_file_db(args.file_list)

  num_errors = 0
  if (args.type == "compile"):
    num_errors = test_rtl_list(file_db)
  elif (args.type == "cocotb_test"):
    num_errors += test_cocotb_rtl_list(file_db)
  else:
    logging.error("Unknown type of test")
    exit(error_codes["ERROR"])

  logging.info("Tested " + str(len(file_db)) + " benchmarks")
  logging.info("\tPassed " + str(len(file_db) - num_errors))
  logging.info("\tFailed " + str(num_errors))
  if (num_errors == 0):
    exit(error_codes["SUCCESS"])
  else:
    exit(error_codes["ERROR"])

