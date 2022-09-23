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
import time
from datetime import timedelta

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
def run_iverilog_for_rtl_file(rtl_files, top_module, output_dir):
  # Check if all the rtl sources exist
  rtl_file_list = []
  for rtl_f in rtl_files:
    rtl_f_abspath = os.path.abspath(rtl_f)
    if not os.path.exists(rtl_f_abspath):
      raise IOError("RTL source not found: " + rtl_f_abspath)
 
    rtl_file_list.append(rtl_f_abspath)

  # Create temp output directory
  if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

  # Run iverilog compilation
  status = 0
  cmd = "iverilog "
  for rtl_f in rtl_file_list:
    cmd += rtl_f + " "
  cmd += " -o " + output_dir + "/" + top_module + ".o"
  process = subprocess.run(cmd, shell=True, check=True)
  status = process.returncode
  return status

#####################################################################
# For each RTL file in the list,
# - compile with iVerilog
#####################################################################
def test_rtl_list(file_db, temp_dir):
  num_failures = 0
  space_limit = 80 # Maximum space tuned for the screen width
  for rtl in file_db.keys():
    # Log runtime
    start_time = time.time()
    # Create a space when logging
    logging_space = " " + "." * (space_limit - len(rtl) - 2) + " "
    status = run_iverilog_for_rtl_file(file_db[rtl]["source"], file_db[rtl]["top_module"], temp_dir)
    num_failures = num_failures + status; 
    end_time = time.time()
    if (status == 0):
      logging.info(rtl + logging_space + "[Pass]")
    else:
      logging.info(rtl + logging_space + "[Fail]")
    # Show runtime
    time_diff = timedelta(seconds=(end_time - start_time))
    time_str = "took " + str(time_diff)
    time_logging_space = "." * (space_limit - len(time_str) - 2) + " "
    logging.info(time_logging_space + time_str)

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
  parser = argparse.ArgumentParser(description='Run regression tests for compiling RTL benchmarks')
  parser.add_argument('--file_list',
                      required=True,
                      help='A file contains a list of RTL files to test')
  parser.add_argument('--temp_dir',
                      default="_iverilog_temp",
                      help='A directory contains intermediate files during test')
  args = parser.parse_args()

  # Create an empty database
  file_db = {}

  # Test all the files
  file_db = read_yaml_to_file_db(args.file_list)

  num_errors = 0
  num_errors = test_rtl_list(file_db, args.temp_dir)

  logging.info("Tested " + str(len(file_db)) + " benchmarks")
  logging.info("\tPassed " + str(len(file_db) - num_errors))
  logging.info("\tFailed " + str(num_errors))
  if (num_errors == 0):
    exit(error_codes["SUCCESS"])
  else:
    exit(error_codes["ERROR"])

