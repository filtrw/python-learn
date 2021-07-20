"""
Написать функцию перевода строки в число не используя функцию
привода к числу и строк (int(), str())
Пример: вход - 'abcd', выход -979899100,
тип выхода - int
"""
import math


def main():
    string_to_convert = input('Please, input string to convert ')
    int_from_string = 0
    ten_power = 0
    count_chr_in_str = len(string_to_convert) - 1
    for index in range(count_chr_in_str, -1, -1):
        if index == count_chr_in_str:
            int_from_string = ord(string_to_convert[index])
        else:
            previous = ord(string_to_convert[index + 1])
            current = ord(string_to_convert[index])
            if previous < 100:
                ten_power += 2
            elif previous >= 100:
                ten_power += 3

            int_from_string += current * 10 ** ten_power
    print(f'Converted string in int is {int_from_string}')
    return int_from_string


if __name__ == '__main__':
    main()
