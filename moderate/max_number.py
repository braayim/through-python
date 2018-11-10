"""
Returns the larger number with out using an operator
"""
import unittest


def max_number(a, b):
    diff = b - a
    sign = (diff & (1 << 63)) >> 63

    return a * sign + b * (sign ^ 1)


class Test(unittest.TestCase):
    data = [
        (10000, 10, 10000),
        (3, 5, 5),
        (0x10000, 0xFFFF, 0x10000),
        (1212121, 1234567, 1234567)
    ]

    def test_number_max(self):
        for a, b, expected in self.data:
            self.assertEqual(max_number(a, b), expected)


if __name__ == "__main__":
    unittest.main()
