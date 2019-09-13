# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-11 10:25:23
'''
BEGIN
function:
    API
return:
    code:0 success
END
'''

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from atm import settings
from atm.shortcuts import get_routes

define("host", default="0.0.0.0", type=str)
define("port", default=8100, type=int)


def runserver():
    parse_command_line()
    app = tornado.web.Application(handlers=get_routes(), debug=settings.DEBUG)
    app.listen(address=options.host, port=options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    runserver()
