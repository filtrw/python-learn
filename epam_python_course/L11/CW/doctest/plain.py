"""
Square root functions

>>> [sqrt(9), sqrt(4)]
[3.0, 2.0]

"""


def sqrt(value):
    """
    Calculate square root of value
    >>> sqrt(-1)
    Traceback (most recent call last):
    ...
    ValueError: Positive value required

    :param value: source value
    :type value: int
    :return: float -- result of calculation
    """
    if value <= 0:
        raise ValueError('Positive value required')
    return value ** 0.5


# assert <>, ''


if __name__ == '__main__':
    import doctest

    doctest.testmod()
