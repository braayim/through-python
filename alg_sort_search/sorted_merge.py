"""
You are given two sorted arrays, A and B, and A has a large enough buffer at the end
to hold B. Write a method to merge B into A in sorted order
"""
import unittest


def sorted_merge(a, b):
    b_index = len(b) - 1
    # actual length of array b with no free spaces
    a_index = len(a) - len(b) - 1

    while a_index >= 0 and b_index >= 0:
        if a[a_index] > b[b_index]:
            a[a_index+b_index+1] = a[a_index]
            a_index -= 1
        else:
            a[a_index+b_index+1] = b[b_index]
            b_index -= 1

    while b_index >= 0:
        a[b_index] = b[b_index]
        b_index -= 1


class Test(unittest.TestCase):
    # Test case
    data = [
        ([33, 44, 55, 66, 88, 99, None, None, None, None],
         [-10, 20, 31, 82], [-10, 20, 31, 33, 44, 55, 66, 82, 88, 99]),

        ([11, 22, 55, 66, 88, None, None, None], [2, 12, 99], [2, 11, 12, 22, 55, 66, 88, 99])
    ]

    def test_merge_sort(self):
        for [a, b, expected] in self.data:
            sorted_merge(a, b)
            self.assertEqual(a, expected)


if __name__ == '__main__':
    unittest.main()
