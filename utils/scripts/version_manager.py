import time
import logging
import yaml
import os
import re
import subprocess
from datetime import timedelta
from datetime import datetime

# Constants

# Class of a PTPX sdc generator
class VersionManager:
    def __init__(self):
        # Internal data
        self.__major_ = 0
        self.__minor_ = 0
        self.__patch_ = 0

    # Parse a given version number
    def parse(self, ver_str):
        ver_nums = ver_str.split(".")
        self.__major_ = int(ver_nums[0])
        self.__minor_ = int(ver_nums[1])
        self.__patch_ = int(ver_nums[2])
        if len(ver_nums) > 3:
            raise Exception(f"Invalid version number {ver_str}. Expect [major].[minor].[patch]")

    # Convert the version number to string
    def to_string(self):
        return ".".join((str(self.__major_), str(self.__minor_), str(self.__patch_)))

    def set_patch(self, new_patch):
        self.__patch_ = new_patch

    def patch(self):
        return self.__patch_

    # Bump-up major and reset minor as well as patch to zero
    def major_release(self):
        self.__major_ += 1
        self.__minor_ = 0
        self.__patch_ = 0

    # Bump-up minor while reset patch to zero
    def minor_release(self):
        self.__minor_ += 1
        self.__patch_ = 0

    # Clear all the data
    def clear(self):
        self.__init__()
