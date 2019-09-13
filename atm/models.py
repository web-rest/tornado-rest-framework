# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-08-01 11:51:50
'''
BEGIN
function:
    DB Module
return:
    code:0 success
END
'''

import crystaldb


class BaseDatabase(object):
    def __init__(self,
                 host,
                 port,
                 user,
                 passwd,
                 dbname,
                 debug=False,
                 get_debug_queries=False,
                 db_instance=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.debug = debug
        self.get_debug_queries = get_debug_queries
        self.db_instance = db_instance

    def new_db_handle(self):
        return crystaldb.database(dbn='mysql',
                                  host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  db=self.dbname,
                                  debug=self.debug,
                                  get_debug_queries=self.get_debug_queries)

    def db_handle(self):
        if not self.is_db_connected():
            try_cnt = 3
            while try_cnt > 0:
                self.db_instance = self.new_db_handle()
                if self.db_instance:
                    return self.db_instance
                try_cnt = try_cnt - 1
        else:
            return self.db_instance

    def is_db_connected(self):
        if not self.db_instance:
            return False
        try:
            self.db_instance.ctx.db.ping()
            return True
        except Exception:
            self.disconnect_db()
        return False

    def disconnect_db(self):
        try:
            self.db_instance.close()
        except Exception:
            pass
        return
