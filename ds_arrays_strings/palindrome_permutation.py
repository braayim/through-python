from collections import Counter
import unittest


def is_palindrome_permutation(string):
    counter = Counter()
    for letter in string.replace(" ", ""):
        counter[letter] += 1
    # return sum([count % 2 for count in counter.values()]) < 2
    odd_counts = 0
    for count in counter.values():
        odd_counts += count % 2
        if odd_counts > 1:
            return False
    return True


class Test(unittest.TestCase):
    data = [("xxoo", True), ("joal", False), ("raacrce", True)]

    def test_palindrome(self):
        for s, expected in self.data:
            self.assertEqual(is_palindrome_permutation(s), expected)


if __name__ == "__main__":
    unittest.main()

