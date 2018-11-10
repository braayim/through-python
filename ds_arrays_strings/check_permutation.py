from collections import Counter
import unittest


def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    counter = Counter()
    for letter in string1:
        counter[letter] += 1

    for letter in string2:
        if counter[letter] == 0:
            return False
        counter[letter] -= 1
    return True


class Counter(dict):
    def __missing__(self, key):
        return 0


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34')
    )

    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f')
    )

    def test_permutation(self):
        for test_strings in self.dataT:
            result = is_permutation(*test_strings)
            self.assertTrue(result)

        for test_strings in self.dataF:
            result = is_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
