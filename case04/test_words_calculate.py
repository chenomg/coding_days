import pytest
from case04.words_calculate import Words_Calculate


class Test_Words_Calculate:
    TestCalculate = Words_Calculate()

    def test_string1(self):
        """
        test to count the number of words in the string
        """
        string1 = """When people treat you with pity and say things like, “I’m praying for you.”"""
        assert 14 == self.TestCalculate.words_calculate(string1)[0]

    def test_file(self):
        """
        test to count the number of words in the string
        """
        file_name = "file_4_test_14words.txt"
        string_from_file = self.TestCalculate.get_string_from_txt_file(
            file_name)
        assert 14 == self.TestCalculate.words_calculate(string_from_file)[0]
