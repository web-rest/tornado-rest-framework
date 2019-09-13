# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-11 11:02:07
'''
BEGIN
function:
    register
return:
    code:0 success
END
'''

import importlib
import os
import re
from atm.settings import ROUTERS_PATH, TRAILING_SLASH, API_PREFIX


def load_modules_from_spec_path(path):
    modules = []
    for filename in os.listdir(path):
        if not re.match(r"^[a-zA-Z].*\.py", filename):
            continue
        root, _ = os.path.splitext(filename)
        package = os.path.relpath(path).replace(os.sep, ".")
        module = importlib.import_module(package + "." + root)
        modules.append(module)
    return modules


def get_routes(path=ROUTERS_PATH,
               api_prefix=API_PREFIX,
               trailing_slash=TRAILING_SLASH):
    routers = []
    for module in load_modules_from_spec_path(path):
        router = getattr(module, "router")
        router.api_prefix = api_prefix
        router.trailing_slash = trailing_slash
        routers += router.rules
    return routers
