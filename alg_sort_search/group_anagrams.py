"""
Write a method to sort an array of strings so that all the anagrams are next to each
other.
"""
import unittest


def sort_anagrams(array):
    pairs = [(s, sorted(s)) for s in array]
    pairs.sort(key=lambda k: k[1])
    return [p[0] for p in pairs]


class Test(unittest.TestCase):
    def test_group_anagrams(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
        self.assertEqual(sort_anagrams(strings),
                         ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])


if __name__ == "__main__":
    unittest.main()
