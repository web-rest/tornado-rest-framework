# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-13 08:45:37
'''
BEGIN
function:
    Open ID
return:
    code:0 success
END
'''

from atm.routers import GenericRouter
from handlers.open_id import OpenIDHandler

router = GenericRouter()
router.register(r"test/open_id", OpenIDHandler)
