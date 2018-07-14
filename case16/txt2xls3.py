#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: txt2xls3.py
#          Desc: 转换numbers.txt内容到xls文件
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-15 00:18:39
#       History:
# =============================================================================
'''
import json
import xlwt

def json2xls():
    filename = 'numbers.txt'
    txt = ''
    row_index = 0
    col_index = 0
    with open(filename, 'r') as f:
        _txt = f.readlines()
        for line in _txt:
            txt = txt + line
    _data = json.loads(txt)
    print('type:{}, value:{}'.format(type(_data), _data))
    xls_data = xlwt.Workbook()
    table = xls_data.add_sheet('city')
    for item in _data:
        for item_ in item:
            table.write(row_index, col_index, item_)
            col_index += 1
        col_index = 0
        row_index += 1
    xls_data.save('numbers.xls')

def main():
    json2xls()

if __name__ == "__main__":
    main()
