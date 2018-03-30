#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Gene_activation_codes(object):
    '''''
    @number:生成激活码的个数
    @length:生成激活码的长度
    '''

    def __init__(self, number, length):
        self.number = number
        self.length = length
        self.__activation_code = {}

    def gene_a_code(self, length):
        code = ''
        letter_list = [chr(i) for i in range(65, 91)]
        num_list = [i for i in range(0, 10)]
        char_list = letter_list + num_list
        for i in range(length):
            code += str(random.choice(char_list))
        return code

    def get_codes(self):
        while len(self.__activation_code) < self.number:
            code = self.gene_a_code(self.length)
            self.__activation_code[code] = None
        return self.__activation_code.keys()


if __name__ == "__main__":
    num = input('Please enter a number of codes.')
    leng = input('Please enter the length of codes.')
    codes = Gene_activation_codes(int(num), int(leng))
    codes_list = codes.get_codes()
    print(u'优惠码如下:')
    for i in codes_list:
        print(i)
