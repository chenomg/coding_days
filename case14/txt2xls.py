#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: txt2xls.py
#          Desc: 转换student.txt内容到xls文件
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-14 23:50:45
#       History:
# =============================================================================
'''
import json
import xlwt

def json2xls():
    filename = 'student.txt'
    txt = ''
    row_index = 0
    col_index = 0
    with open(filename, 'r') as f:
        _txt = f.readlines()
        for line in _txt:
            txt = txt + line
    _data = json.loads(txt)
    xls_data = xlwt.Workbook()
    table = xls_data.add_sheet('student')
    for item in _data:
        table.write(row_index, col_index, item)
        for item_ in _data[item]:
            col_index += 1
            table.write(row_index, col_index, item_)
        col_index = 0
        row_index += 1
    xls_data.save('student.xls')

def main():
    json2xls()

if __name__ == "__main__":
    main()
