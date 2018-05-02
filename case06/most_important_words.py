#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: most_important_words.py
#          Desc: print the 5 most_important_words in articles
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: http://jase.im/
#       Version: 0.0.1
#    LastChange: 2018-05-02 22:31:44
#       History:
# =============================================================================
'''
from file_list import get_filename_list_and_text_path_list
import sys
sys.path.append('..')
from case04.words_calculate import Words_Calculate


def main():
    """
    TODO:
    1. 获取文章列表
    2. 计算每个文章中的单词及数量字典
    3. 获取每个文章中使用量前五名的单词
    """
    # 1st step
    file_list_dic = get_filename_list_and_text_path_list()
    My_Words_Calculate = Words_Calculate()
    # 每篇文章用量前五的单词
    article_5words_dic = {}
    ignore_words = [
        'in', 'on', 'at', 'the', 'of', 'a', 'that', 'is', 'was', 'that', 'and',
        'to', 'with', 'about', 'for', 'as', 'be', 'at', 'or', 'this',
        'are'
    ]
    # 计算每篇文章的单词
    for txt in file_list_dic.keys():
        # 文章路径
        txt_path = file_list_dic[txt]
        # 获取文章字符串
        words_string = My_Words_Calculate.get_string_from_txt_file(txt_path)
        # 获取文章单词及数量字典
        words_dic = My_Words_Calculate.word_and_number(words_string)
        # 统计数量的时候去除无意义的单词
        for word in ignore_words:
            if word in words_dic.keys():
                del words_dic[word]
        # 获取前五的单词
        words5_list = sorted(
            words_dic.items(), key=lambda item: item[1])[:-9:-1]
        article_5words_dic[txt] = words5_list
    return article_5words_dic


if __name__ == "__main__":
    most_important_words = main()
    print(most_important_words)
