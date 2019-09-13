# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-11 11:04:26
'''
BEGIN
function:
    setting
return:
    code:0 success
END
'''

import os


__debug = os.environ.get("ATM_DEBUG", "false")
__trailing_slash = os.environ.get("ATM_TRAILING_SLASH", "false")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True if __debug == "true" else False
TRAILING_SLASH = True if __trailing_slash == "true" else False

API_PREFIX = os.environ.get("ATM_API_PREFIX", "/v1/")
ROUTERS_PATH = os.path.join(BASE_DIR, "routers")
