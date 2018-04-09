import re

file_name = 'Why People Leave the Church and Never Come Back.txt'


def words_calculate(file_name):
    """TODO: Calculate the number of words in the file.

    :file_name: type: string, the name of the file in the same direction
    :returns: type: string, the number of words in the file

    """
    with open(file_name, 'r') as f:
        f.readline()
        # print(f.read())


def main():
    """main function
    :returns: None

    """
    words_calculate(file_name)


if __name__ == "__main__":
    main()
