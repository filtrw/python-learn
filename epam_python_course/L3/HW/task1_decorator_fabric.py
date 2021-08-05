"""
Необходимо написать фабрику декораторов(также декоратор). Фабрика (функция) принимает аргумент - функцию(lambda)
и декоратор. Возвращает декоратор, который должен вызывать функцию(lambda) с аргументом - результатом
декорируемого декоратора.

Пример:

def fabric():
    \"""Фабрика декоратор\"""
    pass


@fabric(lambda x: x ** 2)
def repeat(times):
    \"""Повторить вызов times раз, и вернуть среднее значение\"""
    pass


@repeat(4)
def foo(*args, **kwargs):
    \"""Функция которая работает... и все
    print("Foo called!")
    return 3

>> foo([1, 3, 5])
Foo called!
Foo called!
Foo called!
Foo called!
9

>> fabric.off()
>> foo([1, 3, 5])
9

Дополнительно
1.Красивый, читаемый код ("Всегда пишите код так, будто сопровождать его будет склонный к насилию психопат,
который знает, где вы живете. — Martin Golding")
2. Документирование функций обязательно. Используем стиль документации Sphinx
3. Реализуемый декоратор(фабрика) должен иметь функции для включения/отключения декоратора.
При выключении - декорируемый декоратор не отрабатывает (в примере выше, функция не будет вызываться times раз),
но сам декоратор(фабрика) работает - т.е. вызывается lambda на результат работы функции.
4. Иметь ввиду что функции и декораторы могут быть различными.
5. Ориентироваться на пользователя который может использовать декоратор как угодно, с различными параметрами
"""
import functools


def fabric(handler):
    """Fabric of decorators, which wraps decorators functions and use additional function arguments, which work with
    results  of decorators execution. Have option on and off decorator.

    :param handler: lambda function, which used as argument results of function.
    :type handler: function
    :return:
    """
    """Фабрика декораторов"""
    print("Fabric called! ")

    def create_decorator(dec_func):
        print("Create decorator called", dec_func.__name__)

        def decorator(*dargs, **dkwargs):
            print("Decorator called", *dargs, **dkwargs)

            def worker(work_func):
                print("Inner func", work_func.__name__)

                deco = dec_func(*dargs, **dkwargs)(work_func)

                def inner(*args, **kwargs):
                    print("Args of inner func", work_func.__name__, *args, **kwargs)

                    if fabric.enabled:
                        return handler(deco(*args, **kwargs))
                    else:
                        return handler(work_func(*args, **kwargs))

                return inner

            return worker

        return decorator

    return create_decorator


def off():
    """Turn off work of decorator in fabric of decorators

    :return:
    """
    fabric.enabled = False


def on():
    """turn on work of decorator in fabric of decorators

    :return:
    """
    fabric.enabled = True


fabric.enabled = True
fabric.off = off
fabric.on = on


@fabric(lambda x: x ** 2)
def repeat(times: int):
    """Decorator for repeat functions required times and compute average of result function call

    :param times: amount of times to repeat function calls
    :type times: int
    :return: average of result function call
    :rtype: float
    """
    """Повторить вызов times раз, и вернуть среднее значение"""

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            sum_of_results = 0
            for time in range(times):
                sum_of_results += func(*args, **kwargs)

            result = sum_of_results / times
            return result

        return inner

    return decorator


@repeat(4)
def foo(*args, **kwargs) -> int:
    """Simple function which return constant value and print constant message.

    :param args: any args, not used in function
    :param kwargs: any kwargs, not used in function
    :return: constant value
    :rtype: int
    """
    """Функция которая работает... и все"""
    print("Foo called!")
    return 3


print("FOR TRUE called foo", foo([1, 3, 5]))

# Foo called!
# Foo called!
# Foo called!
# 9
fabric.off()
print("FOR FALSE called foo", foo([1, 3, 5]))
# 9
