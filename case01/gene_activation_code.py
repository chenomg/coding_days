#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Gene_activation_codes(object):
    '''''
    @number:生成激活码的个数
    @length:生成激活码的长度
    激活码包含数字和大写字母
    '''

    def __init__(self, number=1, length=12):
        """
        number: 激活码数量
        length: 激活码长度
        __activation_code: 激活码字典
        __activation_code_list: 激活码清单
        """
        self.number = number
        self.length = length
        self.__activation_code = {}
        self.__activation_code_list = []

    def gene_a_code(self, length):
        """
        生成激活码
        输入length：激活码长度
        输出一个激活码，type: string
        """
        code = ''
        letter_list = [chr(i) for i in range(65, 91)]
        num_list = [i for i in range(0, 10)]
        char_list = letter_list + num_list
        for i in range(length):
            code += str(random.choice(char_list))
        return code

    def get_codes(self):
        """
        获取激活码清单: __activation_code_list
        """
        while len(self.__activation_code) < self.number:
            code = self.gene_a_code(self.length)
            self.__activation_code[code] = None
        for item in self.__activation_code.keys():
            self.__activation_code_list.append(item)
        return self.__activation_code_list


if __name__ == "__main__":
    leng = '12'
    codes_list_char = ''
    num = input('Please enter a number of codes.')
    codes = Gene_activation_codes(int(num), int(leng))
    codes_list = codes.get_codes()
    file_name = 'Activation codes.txt'
    with open(file_name, 'a+') as f:
        f.write('-----Activation codes begain-----\n')
        for item in codes_list:
            f.write(item + '\n')
        f.write('-----Activation codes end-----\n')
    print(u'优惠码如下:')
    for i in codes_list:
        print(i)
