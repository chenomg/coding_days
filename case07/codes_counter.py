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
        comments_flag = False
        i = 0
        with open(file_path) as f:
            for line in iter(f.readline, ''):
                lines += 1
                if re.findall(r'^\s*$', line):
                    # 若全部为空格则空格行数+1
                    blanklines += 1
                if re.findall(r'^\s*\#', line):
                    # 若以#开头
                    commentlines += 1
                if re.findall(r"^\s*(\'\'\'|\"\"\")", line):
                    # 若以'''或"""开头或结束
                    if not comments_flag:
                        comments_flag = True
                    else:
                        comments_flag = False
                        commentlines += 1
                if comments_flag:
                    commentlines += 1
                    i += 1
                    # print('""content"" found {}'.format(i))
                    # print(line)
                if comments_flag and re.findall(r'^\s*\#', line):
                    commentlines -= 1
        return lines, blanklines, commentlines


if __name__ == "__main__":
    totle_lines = 0
    total_blanklines = 0
    total_commentlines = 0
    My_Codes = Codes_Counter()
    # 获取当前目录的父目录
    parent_path = os.path.abspath(
        os.path.join(os.path.dirname('__file__'), os.path.pardir))
    my_codes_path = os.path.abspath(
        os.path.join(parent_path, os.path.pardir)
    )
    # 执行获取父目录下的所有py文件
    My_Codes.get_filename_and_path_dic(my_codes_path)
    # 仅测试当前目录
    # My_Codes.get_filename_and_path_dic(os.getcwd())
    for i in My_Codes.file_dic:
        counters = My_Codes.file_codes_counter(My_Codes.file_dic[i])
        # print(i + '\tpath: ' + My_Codes.file_dic[i] + '\n' +
        # str(My_Codes.lines) + '\t' + str(My_Codes.blanklines) + '\t' +
        # str(My_Codes.commentlines))
        print("{} \t path: {}\nlines: {}\tblanklines: {}\tcommentlines: {}\n".
              format(i, My_Codes.file_dic[i], counters[0], counters[1],
                     counters[2]))
        totle_lines += counters[0]
        total_blanklines += counters[1]
        total_commentlines += counters[2]
    print("Total: \nLines: {}\tBlanklines: {}\tCommentlines: {}\n".format(
        totle_lines, total_blanklines, total_commentlines))
