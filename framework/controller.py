#!/usr/bin/env python
##
## TODO: update project's name
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

"""Implements the controller's logic"""

import os
import docker
from framework import tests_set
from framework import parser
from framework import logger
from framework import testing

class Controller:

    """Controller class that implements the logic"""

    def __init__(self, sets_dirs, tests, global_config):
        self.sets_dirs = sets_dirs
        self.tests = tests
        config_parser = parser.Parser()
        self.global_config = config_parser.parse_yaml(global_config)
        logger.initLogger(self.global_config["logging"]["controller"])
        self.docker = docker.from_env()
        self.tlogger = testing.Testing("Running Testing framework")

    def run(self):
        """Runs all test sets"""
        for test_set in self.sets_dirs:
            test_set_obj = tests_set.TestSet(test_set, self, self.tests)
            self.tlogger.test_set(f"Running test set: {test_set_obj.name}")
            test_set_obj.run()
        self.tlogger.end()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
