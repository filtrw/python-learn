"""
Написать функцию перевода строки в число, не используя стандартные функции приведения (str, int). Рекурсивно.
Пример: вход - 'abcd', выход -979899100,
тип выхода - int
"""

import math


def str_to_int(input_str: str):
    if len(input_str) == 1:
        return ord(input_str[0])

    previous_int = str_to_int(input_str[1:])
    if previous_int % math.log10(previous_int) == 0:
        ten_power = math.ceil(math.log10(previous_int) + 1)
    else:
        ten_power = math.ceil(math.log10(previous_int))

    return ord(input_str[0]) * pow(10, ten_power) + previous_int


def str_to_int2(input_str: str, previous_int: int = 0):
    if len(input_str) == 0:
        return previous_int

    if previous_int == 0:
        ten_power = 0
    elif previous_int % math.log10(previous_int) == 0:
        ten_power = math.ceil(math.log10(previous_int) + 1)
    else:
        ten_power = math.ceil(math.log10(previous_int))

    int_from_string = ord(input_str[-1]) * pow(10, ten_power) + previous_int
    return str_to_int2(input_str[:-1], int_from_string)


def main():
    string_to_convert = input('Please, input string to convert ')
    int_from_string = str_to_int2(string_to_convert, 0)
    print(f'Converted string in int is {int_from_string}')


if __name__ == '__main__':
    main()
