"""
Measures the smallest distance between two arrays
"""
import unittest


def smallest_difference(arr1, arr2):
    # sort arrays
    sorted1 = sorted(arr1)
    sorted2 = sorted(arr2)

    smallest_diff = abs(sorted1[0]-sorted2[0])
    a_index, b_index = 0, 0

    while True:
        diff = sorted1[a_index] - sorted2[b_index]
        smallest_diff = min(smallest_diff, abs(diff))

        if diff == 0:
            break
        if diff < 0:
            a_index += 1
            if a_index == len(sorted1):
                break
        else:
            b_index += 1
            if b_index == len(sorted2):
                break
    return smallest_diff


class Test(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 66, 50]), 6)
        self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 34, 50]), 1)
        self.assertEqual(smallest_difference([11, 77, 33, 44], [77, 2, 34, 50]), 0)
        array1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        array2 = [33, 45, 58, 17]
        self.assertEqual(smallest_difference(array1, array2), 2)
        self.assertEqual(smallest_difference(array2, array1), 2)


if __name__ == "__main__":
    unittest.main()