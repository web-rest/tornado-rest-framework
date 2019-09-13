# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-13 08:48:39
'''
BEGIN
function:
    OpenID Handler
return:
    code:0 success
END
'''

from atm.handlers import RequestHandler


class OpenIDHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.finish()
