# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-08-21 22:41:24
'''
BEGIN
function:
    Concurrent Logging Module
return:
    code:0 success
END
'''

import os
import concurrent_log_handler
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING_CONF_FILE = os.path.join(BASE_DIR, "logging.ini")


class Logging(object):

    log_instance = None

    @staticmethod
    def initialize():
        Logging.log_instance = logging.config.fileConfig(LOGGING_CONF_FILE)

    @staticmethod
    def get_logger(name):
        if Logging.log_instance is None:
            Logging.initialize()
        Logging.log_instance = logging.getLogger(name)
        return Logging.log_instance


errorLogger = Logging.get_logger("error")
infoLogger = Logging.get_logger("info")
