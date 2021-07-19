"""
Написать функцию перевода строки в число не используя функцию
привода к числу и строк (int(), str())
Пример: вход - 'abcd', выход -979899100,
тип выхода - int
"""
import math


def main():
    string_to_convert = input()
    int_from_string = 0
    count_chr_in_str = len(string_to_convert)
    for index in range(count_chr_in_str - 1, -1, -1):
        print(ord(string_to_convert[index]))
        # print(math.floor(math.log10(ord(string_to_convert[index]))))
    return int_from_string


if __name__ == '__main__':
    main()
