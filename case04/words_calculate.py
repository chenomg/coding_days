import re


class Words_Calculate(object):
    def __init__(self, file_name=None, count_string=None):
        self.file_name = file_name
        self.count_string = count_string

    def get_string_from_txt_file(self):
        """TODO: get string from a txt file

        :file_name: in the same folder. type: string
        :returns: string in the file. type: string

        """
        with open(self.file_name, 'r') as f:
            f_read = f.read()
        return f_read

    def words_calculate(self, string):
        """TODO: Calculate the number of words in the file.

        :file_name: type: string, the name of the file in the same direction
        :returns: type: string, the number of words in the file

        """
        words_count_list_provious = re.split(r"[\s\n\t\.]+", string)
        words_count_list = [
            word for word in words_count_list_provious
            if re.match(r'^[a-zA-Z]+', word)
        ]
        return len(words_count_list)


def main():
    """main function
    :returns: None

    """
    file_name_test = 'Why People Leave the Church and Never Come Back.txt'
    test = Words_Calculate(file_name=file_name_test)
    str_from_file = test.get_string_from_txt_file()
    words_count = test.words_calculate(str_from_file)
    print(words_count)


if __name__ == "__main__":
    main()
