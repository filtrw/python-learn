def plus_one(dec_function):
    def inner_function(number):
        return dec_function(number) + 1

    return inner_function


def foo(a):
    return a + 1


foo = plus_one(foo)
print(foo(8))
