#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: sensitive_words_1.py
#          Desc: 敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-05-31 21:22:11
#       History:
# =============================================================================
'''

import re

def get_sensi_words():
    sensi_file = 'filtered_words.txt'
    sensi_words_list = []
    with open(sensi_file, 'r') as f:
        for word in f.readlines():
            sensi_words_list.append(word.strip())
    return sensi_words_list

def output(input_word=None, sensi_words_list=None):
    if input_word in sensi_words_list:
        print('Freedom!')
    else:
        print('Human Rights!')

def main():
    sensi_words_list = get_sensi_words()
    while True:
        input_word = input('Enter a word: ')
        if not input_word:
            break
        output(input_word, sensi_words_list)

if __name__ == "__main__":
    main()
