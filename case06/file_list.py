#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: file_list.py
#          Desc: get file_list in the folder(articles)
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: http://jase.im/
#       Version: 0.0.1
#    LastChange: 2018-05-02 21:57:17
#       History:
# =============================================================================
'''

import os
import re


def get_filename_and_path_dic(
        path=os.path.join(os.getcwd(), 'articles')):
    """
    生成需要进行统计的文件名清单和文件完整目录(带文件名)清单的字典
    返回：
    {file_name:file_path}
    """
    text_dic = {}
    file_list = os.listdir(path)
    for f in file_list:
        if not os.path.isdir(f):
            if re.findall(r'\.txt$', f, re.IGNORECASE):
                # 字典中添加文件名以及路径
                text_dic[f] = os.path.join(path, f)
        else:
            pass
    return text_dic


if __name__ == "__main__":
    dic = get_filename_and_path_dic()
    print(dic)
