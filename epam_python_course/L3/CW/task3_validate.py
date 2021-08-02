"""
Написать декоратор validate, который будет валидировать входящий аргумент функции на предмет выхода
за заданные границы и нужный размер

>> @validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    print("Pixel created!")

set_pixel((0, 127, 300))
Function call is no valid!

set_pixel((0, 127, 250))
Pixel created!

"""
import functools


def with_arguments(deco):
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result

        return decorator

    return wrapper


@with_arguments
def validate(func, low_bound, upper_bound):
    def inner(*args, **kwargs):

        if all((element >= low_bound) and (element <= upper_bound) for element in args[0]):
            return func(*args, **kwargs)
        else:
            print("Function call is no valid!")

    return inner


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    print("Pixel created!")


def main():
    set_pixel((0, 127, 300))
    set_pixel((0, 127, 250))


if __name__ == '__main__':
    main()


def test_set_pixel_correct(capsys):
    set_pixel((0, 127, 250))
    captured = capsys.readouterr()
    assert captured.out == "Pixel created!\n"


def test_set_pixel_incorrect_upper_bond(capsys):
    set_pixel((0, 127, 300))
    captured = capsys.readouterr()
    assert captured.out == "Function call is no valid!\n"


def test_set_pixel_incorrect_low_bond(capsys):
    set_pixel((0, -1127, 300))
    captured = capsys.readouterr()
    assert captured.out == "Function call is no valid!\n"
