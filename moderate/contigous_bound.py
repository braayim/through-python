"""
You are given an array of integers (both positive and negative). Find the continuous
sequence with the largest sum. Return the sum.
"""
import unittest


def contiguous_sequence(array):
    largest_bound = (0, 0)
    big_sum = 0
    bound_sum = 0
    start = 0

    for i, number in enumerate(array):
        bound_sum += number
        if bound_sum < 0:
            bound_sum = 0
            start = i + 1
        if bound_sum > big_sum:
            largest_bound = (start, i+1)
            big_sum = bound_sum
    return [array[i] for i in range(*largest_bound)]


class Test(unittest.TestCase):
    def test_contiguous_sequence(self):
        seq = [-1, 4, 4, -7, 8, 2, -4, 3]
        self.assertEqual(contiguous_sequence(seq), [4, 4, -7, 8, 2])
        seq = [-1, 4, 4, -7, 8, 2, -4, -3, 9]
        self.assertEqual(contiguous_sequence(seq), [4, 4, -7, 8, 2, -4, -3, 9])
        seq = [-1, -4, -54, -7, -8, 2, -4, -3, 9]
        self.assertEqual(contiguous_sequence(seq), [9])
        seq = [-1, -4, -54, -7, -8, -2, -4, -3, -9]
        self.assertEqual(contiguous_sequence(seq), [])
        seq = [2, -8, 3, -2, 4, -10]
        self.assertEqual(contiguous_sequence(seq), [3, -2, 4])

if __name__ == "__main__":
    unittest.main()
