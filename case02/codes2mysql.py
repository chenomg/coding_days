#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from functools import wraps
import sys
sys.path.append('..')
from case01.gene_activation_code import Gene_activation_codes


class MySQL_Process(object):
    def __init__(self, addr, user, password, db_name):
        # 地址
        self.addr = addr
        # 用户名
        self.user = user
        # 密码
        self.password = password
        # 数据库名
        self.db_name = db_name

    def connect_mysql(self):
        # 打开数据库连接
        self.db = pymysql.connect(self.addr, self.user, self.password,
                                  self.db_name)
        # 使用cursor()方法创建一个游标对象cursor
        self.cursor = self.db.cursor()

    def close_mysql(self):
        self.db.close()

    def create_table(self, table, keys_values):
        # 使用execute()方法执行SQL, 如果表存在则删除
        # self.cursor.execute('DROP TABLE IF EXISTS %s' % table)
        # 使用预处理语句创建表
        sql = "CREATE TABLE %s (%s)" % (table, keys_values)
        self.cursor.execute(sql)

    def insert_mysql(self, insert_mysql):
        try:
            # 执行sql语句
            self.cursor.execute(insert_mysql)
            self.db.commit()
        except:
            print("There's something wrong here...")
            # 发生错误时回滚
            self.db.rollback()


if __name__ == "__main__":
    addr = 'localhost'
    user = 'chenomg'
    password = '7777'
    db_name = 'test'
    table = 'ACTIVATION_CODES'
    keys_values = 'ID INT(10) NOT NULL, CODES CHAR(20) NOT NULL, \
        STATUS CHAR(10) NOT NULL, PRIMARY KEY(ID)'

    mysql_process = MySQL_Process(addr, user, password, db_name)
    mysql_process.connect_mysql()
    mysql_process.create_table(table, keys_values)
    gene = Gene_activation_codes()
    for i in range(1, 201):
        code = gene.gene_a_code(length=12)
        print(code)
        insert_mysql_line = "INSERT INTO ACTIVATION_CODES(ID, CODES, STATUS) \
            VALUES(%d, '%s', '%s')" % (i, code, 'OK')
        mysql_process.insert_mysql(insert_mysql_line)
    mysql_process.close_mysql()
