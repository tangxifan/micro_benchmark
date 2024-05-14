import os
import sys
from os.path import dirname, abspath
import argparse
import logging
import subprocess
import yaml
import re
import time
from datetime import timedelta
import datetime
import threading
import version_manager

#####################################################################
# Error codes
#####################################################################
error_codes = {"SUCCESS": 0, "ERROR": 1, "FILE_ERROR": 2}

SPACE_LIMIT = 80  # Maximum space tuned for the screen width

#####################################################################
# Read tagged commit from a file
#####################################################################
def read_tagged_commit_from_file(tagged_commit_file):
    with open(tagged_commit_file, "r") as tag_f:
        return tag_f.readline().rstrip()


#####################################################################
# Extract version from installed binary
#####################################################################
def count_patch(tagged_commit):
    commit_log_str = subprocess.check_output(
        ["git", "log", tagged_commit + "..", "--oneline"]
    ).decode(sys.stdout.encoding)
    logging.debug(f"Git log:\n{commit_log_str}")
    if commit_log_str.rstrip():
        return len(commit_log_str.rstrip().split("\n"))
    else:
        return 0


#####################################################################
# Run version update
#####################################################################
def update_patch_count(version_file, tagged_commit_file, force_commit):
    num_err = 0

    # Count patch based on tag
    tagged_commit = read_tagged_commit_from_file(tagged_commit_file)
    new_patch = count_patch(tagged_commit)
    logging.debug(f"Counted {new_patch} patchs since last version update")

    # Parse version number
    ver_mgr = version_manager.VersionManager()
    with open(version_file, "r") as ver_f:
        ver_mgr.parse(ver_f.readline().rstrip())
    old_ver_str = ver_mgr.to_string()
    old_patch = ver_mgr.patch()
    logging.debug(f"Current version number: {old_ver_str}")
    ver_mgr.set_patch(new_patch)
    new_ver_str = ver_mgr.to_string()

    if int(new_patch) > int(old_patch):
        with open(version_file, "w") as ver_f:
            ver_f.write(new_ver_str)
        logging.info(f"Version bump: {old_ver_str} -> {new_ver_str}")
        if force_commit:
            add_git_commit(version_file, old_ver_str, new_ver_str)
    else:
        logging.info(f"Version remains at {old_ver_str} due to no new commits")
        num_err += 1

    return num_err


#####################################################################
# Update the tagged commit id
# This function will push a commit on the latest version first and record the new commit id
#####################################################################
def add_git_commit(version_file, from_ver, to_ver):
    num_err = 0
    subprocess.check_output(
        ["git", "commit", version_file, "-m", "Bump up version " + from_ver + " -> " + to_ver]
    )
    logging.info("Add 1 commit to git tree")
    return num_err


#####################################################################
# Update the tagged commit id
# This function will push a commit on the latest version first and record the new commit id
#####################################################################
def update_tagged_commit(version_file, from_ver, to_ver, tagged_commit_file):
    num_err = 0
    num_err += add_git_commit(version_file, from_ver, to_ver)
    last_commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode(
        sys.stdout.encoding
    )

    with open(tagged_commit_file, "w") as tag_f:
        tag_f.write(last_commit)

    # Commit the tagged commit info as well
    num_err += add_git_commit(tagged_commit_file, from_ver, to_ver)

    return num_err


#####################################################################
# Create a new release version
#####################################################################
def create_release_version_number(version_file, tagged_commit_file, bump_type):
    num_err = 0

    # Parse version number
    ver_mgr = version_manager.VersionManager()
    with open(version_file, "r") as ver_f:
        ver_mgr.parse(ver_f.readline())
    old_ver_str = ver_mgr.to_string()
    logging.debug(f"Current version number: {old_ver_str}")
    if bump_type == "major":
        ver_mgr.major_release()
    elif bump_type == "minor":
        ver_mgr.minor_release()
    elif bump_type == "reset":
        ver_mgr.clear()
    else:
        raise Exception(f"Invalid type of version bump: {bump_type}! Expect [major|minor|reset]")
    new_ver_str = ver_mgr.to_string()

    with open(version_file, "w") as ver_f:
        ver_f.write(new_ver_str)
    logging.info(f"Version bump: {old_ver_str} -> {new_ver_str}")

    # Update tagged commit
    num_err += update_tagged_commit(version_file, old_ver_str, new_ver_str, tagged_commit_file)

    return num_err


##################################################################
# Main function
##################################################################
if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement

    # Parse the options and apply sanity checks
    parser = argparse.ArgumentParser(description="Update version numbers")
    parser.add_argument(
        "--version_file",
        default="../VERSION.md",
        help="The file contains version number. Must be in the format of [major].[minor].[patch]",
    )
    parser.add_argument(
        "--tagged_commit",
        default=".TAGGED_COMMIT",
        help="The tagged commit of last release. Used as the base commit id when counting the patch number",
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="Create a new release on the version number (reset patch number to zero). The tagged_commit file will be updated on the current version",
    )
    parser.add_argument(
        "--bump_type",
        default="minor",
        choices=["major", "minor", "reset"],
        help="Bump up the specific digit on the version. If the type is major, only the major number will be increased. If the type is minor, only the minor number will be increased. If the type is reset, both major, minor and patch will be reset to zeros. By default, it is minor",
    )
    parser.add_argument(
        "--force_commit",
        default="off",
        choices=["on", "off"],
        help="Force to create a dedicated git commit after version update. Not applicable to release mode!",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    #####################################################################
    # Initialize logger
    #####################################################################
    logging_level = logging.INFO
    if args.verbose:
        logging_level = logging.DEBUG
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging_level)

    num_err = 0
    num_err += update_patch_count(args.version_file, args.tagged_commit, args.force_commit == "on")
    if args.release:
        num_err += create_release_version_number(
            args.version_file, args.tagged_commit, args.bump_type
        )

    if num_err == 0:
        exit(error_codes["SUCCESS"])
    else:
        exit(error_codes["ERROR"])
