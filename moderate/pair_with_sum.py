"""
Design an algorithm to find all pairs of integers within an array which sum to a
specified value.
"""
import unittest


def pair_sums(arr, s):
    pairs = set()
    values = set()
    for v in arr:
        values.add(v)

    for elem in arr:
        if s - elem in values:
            values.remove(elem)
            pairs.add((elem, s-elem))
    return pairs


class Test(unittest.TestCase):
    def test_pairs_with_sum(self):
        arr = [2, 3, 4, 11, -4]
        self.assertEqual(pair_sums(arr, 7), {(3,4),(11,-4)})
        arr = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 20, 30, -11]
        self.assertEqual(pair_sums(arr, 55), {(0,55),(22,33),(66,-11),(11,44)})


if __name__ == "__main__":
    unittest.main()