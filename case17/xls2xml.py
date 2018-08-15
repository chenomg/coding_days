#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: xls2xml.py
#          Desc: 将第0014题中的student.xls文件中的内容写到student.xml文件中
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-08-15 23:09:21
#       History:
# =============================================================================
'''

from lxml import etree
import xlrd
import json


def xls2dic(file):
    out_dic = {}
    xls = xlrd.open_workbook(file)
    sheet = xls.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    for row in range(rows):
        key = sheet.cell(row, 0).value
        out_dic[key] = sheet.row_values(row)[1:]
    out_dic_str = json.dumps(out_dic, ensure_ascii=False, indent=4)
    print(out_dic_str)
    return out_dic_str


students_info = xls2dic('student.xls')

root = etree.Element('root')
students = etree.SubElement(root, 'students')
# students.tail = '\n'
# 添加学生信息
students.text = students_info
# 添加注释信息
comment = '学生信息表\n"id":[名字, 数学, 语文, 英文]'
comment_etree = etree.Comment(comment)
# comment_etree.tail = '\n'
students.append(comment_etree)

# save
tree = etree.ElementTree(root)
tree.write(
    'student.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
