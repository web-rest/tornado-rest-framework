# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-09-13 08:55:42
'''
BEGIN
function:
    Handler
return:
    code:0 success
END
'''

import json
import tornado.web


class RequestHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        mapping = kwargs.get("mapping")
        if not mapping:
            return
        for method, action in mapping.items():
            handler = getattr(self, action)
            setattr(self, method, handler)

    def prepare(self):
        self.parse_request()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods",
                        "GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS")

    def write(self, chunk):
        if isinstance(chunk, dict):
            chunk = json.dumps(chunk, ensure_ascii=False, indent=2)
            chunk = chunk.replace("</", "<\\/") + "\n"
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        super().write(chunk)

    def parse_request(self):
        pass
