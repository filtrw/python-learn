"""
Написать программу, принимающую на вход две дроби (вида a/b) и выводящую результат сложения дробей вида:
"Result is XX/XX"
"""

import fractions


def sum_fractions():
    first_fraction = fractions.Fraction(input('Please, input first fraction '))
    second_fraction = fractions.Fraction(input('Please, input second fraction '))
    print(f"Result is {first_fraction + second_fraction}")


"""
Написать программу, ожидающую ввод числа, возводящую его в степень 13 и выводящую на консоль
"""


def power_13():
    number = int(input())
    print(number ** 13)


def math_execute(x_var, b_var):
    result = (12 * x_var + 25 * b_var) / (1 + x_var ** (2 ** b_var))
    print(result)


math_execute(5, 2)
