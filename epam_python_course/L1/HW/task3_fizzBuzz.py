"""
Напишите программу, которая выводит числа от 1 до 100
При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел кратных пяти - Buzz.
Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz
"""


def define_multiple(number):
    is_three_multiple = number % 3
    is_five_multiple = number % 5

    if is_three_multiple == 0 and is_five_multiple == 0:
        print("FizzBuzz", end=" ")
    elif is_three_multiple == 0:
        print("Fizz", end=" ")
    elif is_five_multiple == 0:
        print("Buzz", end=" ")
    else:
        print(number, end=" ")


def main():
    for number in range(1, 100):
        define_multiple(number)


if __name__ == '__main__':
    main()
