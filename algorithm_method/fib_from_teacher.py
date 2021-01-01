"""
Несколько вариантов решения задачи по вычислению чисел Фибоначчи,
сравнение скорости работы алгоритмов, возможности посчитать достаточно большие числа
"""
# Импорт бибилиотеки, которая визуализирует вызовы внутри функций (граф)
from rcviz import viz


# Способ №1 - вычисление числа Фибонначи с помощью рекурсии
# Минусы - много раз вычисляет одни и те же значения (см. графики вызова)
# При сравнительно небольших числах >40 считает очень медленно, в течение нескольких секунд
# скорость вычислений зависит экспоненциально от величины числа
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# Проверка вычисления
# print(fib1(8))

# Но на больших числах - начинает считать очень долго
# print(fib1(40))


# Визуализация работы алгоритма с помощью библиотеки, viz  - декоратор
old_fib = fib1
fib1 = viz(fib1)
fib1(5)

# Отображение изображений графика, сгенерированного viz
from IPython.display import Image

# Image("./fib1.png")


# Способ №2  рекурсивное вычисление - но значение складывается в cache,
# Не нужно вычислять все предыдущие значения - нужно взять из cache уже посчитанное значение
# Недостаток - ограничение на глубину рекрсии, функция может вызываться рекурсивно не более 1000 раз
cache = {}


def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


# Визуализация алгоритма, посчитанного вторым способом
# fib2 = viz(fib2)
# fib2(5)

# декоратор, чтобы сделать переменную cache не доступной для других функций и значений, кроме тех, что работают с
# числами Фибоначчи
def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


fib1 = memo(old_fib)
print(fib1(80))

# То же самое что делает декоратор memo делает стандартная библиотека Питона - lru_cache
from functools import lru_cache

fib1 = lru_cache(maxsize=None)(old_fib)


# print(fib1(8000))


# Способ №3 - итераторы.
# Преимщества - работает линейно, работает быстро, нет ограничений на глубину рекурсии
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib3(8000))

# Вычисление времени, за которое отрабатывает функция
import time


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


print(timed(fib3, 800))

# Сравнение  скорости роста времени работы нескольких функций
from matplotlib import pyplot as plt


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


fib1 = old_fib
# compare([fib1, fib3], list(range(20)))
# compare([fib2, fib3], list(range(20)))
compare([fib3], list(range(200)))
