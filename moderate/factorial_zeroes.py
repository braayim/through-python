"""
Returns the number of leading zeros on the the factorial of an integer n
"""
import unittest


def factorial_zeros(n):
    leading_zeros = 0
    while n > 4:
        n //= 5
        leading_zeros += n
    return leading_zeros


class Test(unittest.TestCase):
    data = [(4, 0), (9, 1), (10, 2), (25, 6), (55, 13)]

    def test_leading_zeros(self):
        for n, expected in self.data:
            self.assertEqual(factorial_zeros(n), expected)


if __name__ == '__main__':
    unittest.main()
