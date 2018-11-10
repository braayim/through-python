"""
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
"""
import unittest


def is_unique(string):
    """
    Determines if the string only contains unique characters
    """
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


class Test(unittest.TestCase):
    dataT = ['abcdef', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            print(test_string)
            print(actual)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
