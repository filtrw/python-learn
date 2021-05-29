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


import unittest


class TestSqrt(unittest.TestCase):
    def test_square_root_positive(self):
        self.assertEqual(3.0, sqrt(9), 'Wrong answer')

    def test_square_root_non_positive_value(self):
        with self.assertRaises(ValueError) as raised_exception:
            sqrt(0)

        self.assertEqual(raised_exception.exception.args[0], 'Positive value required!')


if __name__ == '__main__':
    unittest.main()
