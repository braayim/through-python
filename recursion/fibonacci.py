"""
Write a method to generate the nth Fibonacci number.
"""
import unittest


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return None


class Test(unittest.TestCase):
    data = [(0, 0), (1, 1), (2, 1), (3, 2)]

    def test_fibonacci(self):
        for n, expected in self.data:
            self.assertEqual(fibonacci(n), expected)


if __name__ == '__main__':
    unittest.main()
