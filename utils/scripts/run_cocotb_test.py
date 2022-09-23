#####################################################################
# A script to run cocotb tests with a given list of tasks
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
import datetime
import threading

#####################################################################
# Error codes
#####################################################################
error_codes = {
  "SUCCESS": 0,
  "ERROR": 1, 
  "FILE_ERROR": 2 
}

space_limit = 80 # Maximum space tuned for the screen width

#####################################################################
# Initialize logger 
#####################################################################
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO);

#####################################################################
# Run cocotb Makefile for a given RTL
#####################################################################
def run_cocotb_for_rtl_file(rtl_file, simulator):
  status = error_codes["SUCCESS"]

  # Use custom simulator if specified
  sim_args = ""
  if (simulator):
    sim_args = " SIM=" + simulator

  # Go to the localrun directory and call cocotb
  curr_dir = os.getcwd()
  include_dir = rtl_file
  logging.debug("Changed to " + include_dir)
  os.chdir(include_dir)
  # Start a new run
  cmd = "make" + sim_args
  log_fname = "cocotb_sim.log"
  with open(log_fname, "w") as log_f:
    make_process = subprocess.Popen(cmd, shell=True, stdout=log_f, stderr=log_f)

    if (make_process.wait()) != 0:
      status = error_codes["ERROR"]

  logging.debug("Changed to " + curr_dir)
  os.chdir(curr_dir)

  return status

#####################################################################
# Run cocotb Makefile for a given RTL
#####################################################################
def thread_run_cocotb_for_rtl_file(thread_sema, rtl_file, rtl_abspath, simulator, job_status, job_time):
  with thread_sema:
    thread_name = threading.currentThread().getName()

    # Log runtime
    start_time = time.time()
    logging.debug("rtl_file: " + rtl_file)

    start_time_str = datetime.datetime.fromtimestamp(start_time).isoformat()
    time_logging_space = "." * (space_limit - len(rtl_file) -  len(" start at") - len(start_time_str) - 2) + " "
    logging.info(rtl_file + " start at" + time_logging_space + start_time_str)

    job_status[rtl_abspath] = run_cocotb_for_rtl_file(rtl_abspath, simulator)
    end_time = time.time()
    job_time[rtl_abspath] = timedelta(seconds=(end_time - start_time))

    end_time_str = datetime.datetime.fromtimestamp(end_time).isoformat()
    logging.info(rtl_file + " ends  at" + time_logging_space + end_time_str)

    return job_status

#####################################################################
# Check cocotb results file and report any failures captured
#####################################################################
def check_cocotb_results(result_file):
  status = 0
  # If the file does not exist, fail this test directly
  if not os.path.isfile(result_file):
    return 1
  result_f = open(result_file, "r")
  for line in result_f:
    if re.search("failure", line):
      status += 1
  return status

#####################################################################
# For each RTL file in the list,
# - Run cocotb tests
#####################################################################
def test_cocotb_rtl_list(file_db, simulator, max_num_jobs, new_thread_wait_time):
  num_failures = 0

  # Create thread pool
  thread_sema = threading.BoundedSemaphore(value=max_num_jobs)
  thread_list = []

  # Job status dashboard
  job_status = {}
  job_time = {}

  curr_dir = os.getcwd()

  for rtl in file_db.keys():
    # Skip those without a cocotb directory
    if not "cocotb_dir" in file_db[rtl]:
      continue
    rtl_abspath = os.path.abspath(curr_dir + "/" + file_db[rtl]["cocotb_dir"]);
    logging.debug("test name: " + rtl)
    logging.debug("testbench abspath: " + rtl_abspath)
    cur_thread = threading.Thread(target=thread_run_cocotb_for_rtl_file, args=(thread_sema, rtl, rtl_abspath, simulator, job_status, job_time))
    cur_thread.start()
    thread_list.append(cur_thread)
    time.sleep(new_thread_wait_time) # Give a wait time before starting the next thread. Avoid any conflicts in switching directories

  for cur_thread in thread_list:
    cur_thread.join()

  for rtl in file_db.keys():
    # Skip those without a cocotb directory
    if not "cocotb_dir" in file_db[rtl]:
      continue
    rtl_abspath = os.path.abspath(curr_dir + "/" + file_db[rtl]["cocotb_dir"]);
    include_dir = rtl_abspath
    curr_job_status = check_cocotb_results(include_dir + "/" + "results.xml")
    # Create a space when logging
    logging_space = " " + "." * (space_limit - len(rtl) - 2) + " "
    num_failures = num_failures + curr_job_status; 
    if (curr_job_status == 0):
      logging.info(rtl + logging_space + "[Pass]")
    else:
      logging.info(rtl + logging_space + "[Fail]")
    # Show runtime
    time_diff = job_time[rtl_abspath]
    time_str = "took " + str(time_diff)
    time_logging_space = "." * (space_limit - len(rtl) - len(time_str) - 2) + " "
    logging.info(rtl + time_logging_space + time_str)

  return num_failures

#####################################################################
# Read file database to a yaml file
#####################################################################
def read_yaml_to_file_db(yaml_filename):
  file_db = {}
  with open(yaml_filename, 'r') as stream:
    try:
      file_db = yaml.load(stream, Loader=yaml.FullLoader)
      if file_db :
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
  parser = argparse.ArgumentParser(description='Run cocotb tests with a given task list ')
  parser.add_argument('--file_list',
                      required=True,
                      help='A file contains a list of RTL files to test')
  parser.add_argument('--simulator',
                      default="",
                      help='Specify the HDL simulator to be used in cocotb. By default, we consider the simulator written in Cocotb Makefile')
  parser.add_argument('--new_thread_wait_time',
                      type=float,
                      default="10",
                      help='Specify the waiting time before starting a new thread (unit: second)')
  parser.add_argument('--j', type=int, default=2,
                      help='Specify maximum number of jobs to be run in parallel')
  args = parser.parse_args()

  # Create an empty database
  file_db = {}

  # Test all the files
  file_db = read_yaml_to_file_db(args.file_list)

  # Early exit condition: when no test case is listed
  if not file_db :
    logging.info("No test case found. Exiting...")
    exit(error_codes["SUCCESS"])

  num_errors = 0
  num_errors += test_cocotb_rtl_list(file_db, args.simulator, args.j, args.new_thread_wait_time)

  logging.info("Tested " + str(len(file_db)) + " benchmarks")
  logging.info("\tPassed " + str(len(file_db) - num_errors))
  logging.info("\tFailed " + str(num_errors))
  if (num_errors == 0):
    exit(error_codes["SUCCESS"])
  else:
    exit(error_codes["ERROR"])
