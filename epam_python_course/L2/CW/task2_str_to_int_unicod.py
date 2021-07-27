"""
Написать функцию перевода строки в число не используя функцию
привода к числу и строк (int(), str())
Пример: вход - 'abcd', выход -979899100,
тип выхода - int
"""
import math


def str_to_int(input_str: str):
    int_from_string = 0
    ten_power = 0
    count_chr_in_str = len(input_str) - 1

    for index in range(count_chr_in_str, -1, -1):
        if index == count_chr_in_str:
            int_from_string = ord(input_str[index])
        else:
            previous = ord(input_str[index + 1])
            current = ord(input_str[index])

            ten_power += 2 if previous < 100 else 3
            int_from_string += current * 10 ** ten_power

    return int_from_string


def main():
    string_to_convert = input('Please, input string to convert ')
    int_from_string = str_to_int(string_to_convert)
    print(f'Converted string in int is {int_from_string}')


if __name__ == '__main__':
    main()
