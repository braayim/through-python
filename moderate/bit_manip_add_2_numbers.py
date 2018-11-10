"""
Write a function that adds two numbers. You should not use + or any arithmetic operators.
"""
import unittest


def add(x, y):

    # Iterate till there is no carry
    while y != 0:

        # carry now contains common
        # set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1

    return x


class Test(unittest.TestCase):
    data = [
        ((10, 2), 12),
        ((5, 2), 7),
        ((10, 8), 18),
        ((1000, 9), 1009),
    ]

    def test_bit_add(self):
        for arg, expected in self.data:
            self.assertEqual(add(*arg), expected)


if __name__ == "__main__":
    unittest.main()