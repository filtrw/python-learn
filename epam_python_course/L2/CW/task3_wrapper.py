"""
Написать функцию, которая обертывает любую, передаваемую в нее
функцию и выводит имя передаваемой функции перед ее вызовом

wr = wrapper(print)
wr("Hello")

Function name: 'print'
Hello

Скорректировано по примеру в классе
"""


def wrapper(func):
    def inner(*args, **kwargs):
        print(f'Function name: {func.__name__}')
        return func(*args, **kwargs)

    return inner


wr = wrapper(print)
wr("Hello")

wr = wrapper(pow)
print(wr(2, 5))
