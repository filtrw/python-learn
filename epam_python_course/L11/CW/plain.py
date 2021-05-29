"""
Square root functions
"""


def sqrt(value):
    """
    Calculate square root of value

    :param value: source value
    :type value: int
    :return: float -- result of calculation
    """
    if value <= 0:
        raise ValueError('Positive value required')
    return value ** 0.5


# assert <>, ''

def test_square_root_positive():
    assert sqrt(9) == 3.0


def test_square_root_non_positive_value():
    try:
        sqrt(-1)
    except ValueError as raised_exception:
        assert raised_exception.args[0] == 'Positive value required', 'Wrong exception text'
        return

    assert False, 'Exception did not raise '


if __name__ == '__main__':
    test_square_root_positive()
    test_square_root_non_positive_value()
