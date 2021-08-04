"""
Написать декоратор, который будет считать время работы функции и выводить на экран.
Для текущего времени можно использовать модуль time
"""
import functools
import time


def time_it(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()
        print(f"Time for execution func {func.__name__} is {t1 - t0} second")

    return inner


@time_it
def fib(n):
    fib_array = [0, 1]

    for element in range(2, n + 1):
        fib_array.insert(element, (fib_array[element - 1] + fib_array[element - 2]))
    print(f"Fib for number {n} is {fib_array[n]}")
    return fib_array[n]


def main():
    print("Let's start")
    fib(10)

    print("One more time")
    fib(100)

    print("Last one")
    fib(10000)


if __name__ == '__main__':
    main()
