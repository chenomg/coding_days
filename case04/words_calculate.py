#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs


class Words_Calculate(object):
    def __init__(self, file_name=None, string_2_count=None):
        self.file_name = file_name
        self.string_2_count = string_2_count
        self.words_count_list = []
        self.words_count_dic = {}

    def get_string_from_txt_file(self, file_name=None):
        """TODO: get string from a txt file

        :file_name: in the same folder. type: string
        :returns: string in the file. type: string

        """
        if file_name:
            self.file_name = file_name
        with open(self.file_name, 'r', encoding='utf-8') as f:
            f_read = f.read()
        return f_read

    def words_calculate(self, string):
        """TODO: Calculate the number of words in the file.

        :file_name: type: string, the name of the file in the same direction
        :returns: (count_number, word_list)
                count_number: type: string, the number of words in the file
                word_list: type: list, words appears in the string
        """
        words_count_list_provious = re.split(r"[\s\n\t\.\,\“\?\"\…\:\”]+", string)
        words_count_list = [
            word.lower() for word in words_count_list_provious
            if re.match(r'^[a-zA-Z]+', word)
        ]
        return len(words_count_list), words_count_list

    def word_and_number(self, string_2_count=None):
        """TODO: calculate all words and their appeared number

        :string: input
        :returns: type: dic--> [word1:count1,word2:count2]

        """
        if string_2_count:
            self.string_2_count = string_2_count
        words_total = self.words_calculate(self.string_2_count)[0]
        words = self.words_calculate(string_2_count)[1]
        for word in words:
            if not word in self.words_count_dic.keys():
                self.words_count_dic[word] = 1
            else:
                self.words_count_dic[word] += 1
        return self.words_count_dic


def main():
    """main function
    :returns: None

    """
    file_name_test = 'Why People Leave the Church and Never Come Back.txt'
    test = Words_Calculate(file_name=file_name_test)
    str_from_file = test.get_string_from_txt_file()
    words_count = test.words_calculate(str_from_file)[0]
    words_count_dic = test.word_and_number(str_from_file)
    print(words_count)
    print(words_count_dic)
    with open('words_count_dic.txt','w') as f:
        for key in words_count_dic.keys():
            f.write('{}: {}\n'.format(key, words_count_dic[key]))


if __name__ == "__main__":
    main()
