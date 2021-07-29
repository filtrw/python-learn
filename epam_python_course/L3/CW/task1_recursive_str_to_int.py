"""
Написать функцию перевода строки в число, не используя стандартные функции приведения (str, int). Рекурсивно.
Пример: вход - 'abcd', выход -979899100,
тип выхода - int
"""

import math


def str_to_int(input_str: str) -> int:
    """
    Recursive function to convert string to int without using int(), str().
    This function work in direct order:starts to convert from first char of string and recursive call itself
    for other chars in string

    :param input_str: string to convert
    :type input_str: str

    :return: converted number
    :rtype: int
    """
    if len(input_str) == 1:
        return ord(input_str[0])

    previous_int = str_to_int(input_str[1:])
    # In case 10, 100, 1000 and so on, need to increment ten_power on 1 for correct computation multiplier and
    # take account "1" in "100"/"1000"/...
    # In other case math.ceil will rounds up.
    if previous_int % math.log10(previous_int) == 0:
        ten_power = math.ceil(math.log10(previous_int) + 1)
    else:
        ten_power = math.ceil(math.log10(previous_int))

    return ord(input_str[0]) * pow(10, ten_power) + previous_int


def str_to_int2(input_str: str, previous_int: int = 0) -> int:
    """
    Recursive function to convert string to int without using int(), str().
    This function work in reverse order:starts to convert from last char of string and recursive call itself
    for other chars in string

    :param input_str: string to convert
    :type input_str: str

    :param previous_int: int number which computed on previous step of conversion. By default it equals 0.
    :type previous_int: int

    :return: converted number
    :rtype: int
    """
    if len(input_str) == 0:
        return previous_int

    if previous_int == 0:
        ten_power = 0
    # In case 10, 100, 1000 and so on, need to increment ten_power on 1 for correct computation multiplier and
    # take account "1" in "100"/"1000"/...
    # In other case math.ceil will rounds up.
    elif previous_int % math.log10(previous_int) == 0:
        ten_power = math.ceil(math.log10(previous_int) + 1)
    else:
        ten_power = math.ceil(math.log10(previous_int))

    int_from_string = ord(input_str[-1]) * pow(10, ten_power) + previous_int
    return str_to_int2(input_str[:-1], int_from_string)


def main():
    string_to_convert = input('Please, input string to convert ')
    int_from_string = str_to_int(string_to_convert)
    print(f'First function (direct). Converted string in int is {int_from_string}')

    int_from_string2 = str_to_int2(string_to_convert, 0)
    print(f'Second function (reverse). Converted string in int is {int_from_string2}')


if __name__ == '__main__':
    main()
