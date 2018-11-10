"""
Given a sorted array of strings which is interspersed with empty strings, write a meth-
od to find the location of a given string.
Example:
    find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
    find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return None
"""
import unittest


def sparse_search(array, item, left=0, right=None):
    if right is None:
        right = len(array)
    if left == right:
        return None

    middle = (left + right) // 2

    next_ix = middle
    next = array[next_ix]

    while not next:
        next_ix += 1
        if next_ix == len(array):
            return sparse_search(array, item, left, middle)
        next = array[next_ix]
    if next == item:
        return next_ix
    if item < next:
        return sparse_search(array, item, left, middle)
    else:
        return sparse_search(array, item, next_ix+1, right)


class Test(unittest.TestCase):
    def test_sparse_search(self):
        array = [0, 0, 7, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 37, 40, 0, 0, 0]
        self.assertEqual(sparse_search(array, 0), None)
        self.assertEqual(sparse_search(array, 7), 2)
        self.assertEqual(sparse_search(array, 19), 8)
        self.assertEqual(sparse_search(array, 37), 13)
        self.assertEqual(sparse_search(array, 40), 14)
        array = [0, 12, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(sparse_search(array, 12), 1)
        self.assertEqual(sparse_search(array, 18), 3)
        array = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
        self.assertEqual(sparse_search(array, 'ball'), 4)
        self.assertEqual(sparse_search(array, 'dad'), 10)


if __name__ == "__main__":
    unittest.main()
