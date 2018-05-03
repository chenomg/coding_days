#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: file_list.py
#          Desc: get file_list in the folder(codes, ended with .py)
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: http://jase.im/
#       Version: 0.0.1
#    LastChange: 2018-05-03 21:57:51
#       History:
# =============================================================================
'''

import os
import re


class Codes_Counter(object):
    def __init__(self):
        self.file_dic = {}

    def get_filename_and_path_dic(self, path):
        """
        生成需要进行统计的文件名清单和文件完整目录(带文件名)清单的字典
        返回：
        {file_name:file_path}
        """
        file_list = os.listdir(path)
        # print(file_list)
        for f in file_list:
            if os.path.isdir(os.path.join(path, f)):
                self.get_filename_and_path_dic(os.path.join(path, f))
            else:
                if re.findall(r'\.py$', f, re.IGNORECASE):
                    # 字典中添加文件名以及路径
                    self.file_dic[f] = os.path.join(path, f)

    def file_codes_counter(self, file_path):
        lines = 0
        blanklines = 0
        commentlines = 0
        comments_flag = 0
        with open(file_path) as f:
            for line in iter(f.readline, ''):
                lines += 1
                if re.findall(r'^\s*$', line):
                    blanklines += 1
                elif re.findall(r'(\'\'\'|\"\"\")', line):
                    if not comments_flag:
                        comments_flag = 1
                    else:
                        comments_flag = 0
                        commentlines += 1
                    # print(line)
                    # print(re.findall(r'^\s*(\'\'\'|\"\"\")', line))
                elif comments_flag:
                    commentlines += 1
                    # print(line)
                elif not comments_flag:
                    if re.findall(r'^\s*#', line):
                        commentlines += 1
        return lines, blanklines, commentlines


if __name__ == "__main__":
    My_Codes = Codes_Counter()
    # 获取当前目录的父目录
    parent_path = os.path.abspath(
        os.path.join(os.path.dirname('__file__'), os.path.pardir))
    # 执行获取当前目录下的所有py文件
    My_Codes.get_filename_and_path_dic(parent_path)
    print(parent_path)
    print(My_Codes.file_dic)
    for i in My_Codes.file_dic:
        counters = My_Codes.file_codes_counter(My_Codes.file_dic[i])
        # print(i + '\tpath: ' + My_Codes.file_dic[i] + '\n' +
              # str(My_Codes.lines) + '\t' + str(My_Codes.blanklines) + '\t' +
              # str(My_Codes.commentlines))
        print("{} \t path: {}\nlines: {}\tblanklines: {}\tcommentlines: {}\n".format(i, My_Codes.file_dic[i], counters[0], counters[1], counters[2]))
