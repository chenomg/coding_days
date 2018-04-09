import re

file_name = 'Why People Leave the Church and Never Come Back.txt'


class Words_Calculate(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def words_calculate(self):
        """TODO: Calculate the number of words in the file.

        :file_name: type: string, the name of the file in the same direction
        :returns: type: string, the number of words in the file

        """
        with open(file_name, 'r') as f:
            f_read = f.read()
            words_count_list = re.split(r'\W+', f_read)
        return len(words_count_list)


def main():
    """main function
    :returns: None

    """
    test = Words_Calculate(file_name)
    words_count = test.words_calculate()
    print(words_count)


if __name__ == "__main__":
    main()
