#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: txt2xls2.py
#          Desc: 转换city.txt内容到xls文件
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-15 00:12:08
#       History:
# =============================================================================
'''
import json
import xlwt

def json2xls():
    filename = 'city.txt'
    txt = ''
    row_index = 0
    col_index = 0
    with open(filename, 'r') as f:
        _txt = f.readlines()
        for line in _txt:
            txt = txt + line
    _data = json.loads(txt)
    print(_data)
    xls_data = xlwt.Workbook()
    table = xls_data.add_sheet('city')
    for item in _data:
        table.write(row_index, col_index, item)
        col_index += 1
        table.write(row_index, col_index, _data[item])
        col_index = 0
        row_index += 1
    xls_data.save('city.xls')

def main():
    json2xls()

if __name__ == "__main__":
    main()
