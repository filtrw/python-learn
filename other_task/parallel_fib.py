"""
Нужно посчитать число фибоначчи для трех введеных чисел
Числа должны вычисляться параллельно, в несколько потоков
Выводится на экран по мере вычисления
"""
import sys
import time
from threading import Thread


def fib(number: int):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)


def print_fib(number: int):
    fib_num = fib(number)
    print(f'Number is {number} Fib is {fib_num}')


def main():
    numbers = tuple(map(int, input().split()))
    print(numbers)
    all_th = []
    t0 = time.perf_counter()
    for number in numbers:
        th = Thread(target=print_fib, args=(number,))
        th.start()
        all_th.append(th)
    for th in all_th:
        th.join()
    print(time.perf_counter() - t0)
    numbers = tuple(map(int, input().split()))
    print(numbers)
    t0 = time.perf_counter()
    for number in numbers:
        print_fib(number)
        # th = Thread(target=print_fib, args=(number, ))
        # th.start()
    print(time.perf_counter() - t0)


if __name__ == "__main__":
    main()
