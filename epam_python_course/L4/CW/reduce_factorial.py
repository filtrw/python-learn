"""
посчитать факториал с помощью функции reduce

"""
import functools

result = functools.reduce(lambda accum, n: accum * n if n != 0 else accum, range(6), 1)
print(result)
