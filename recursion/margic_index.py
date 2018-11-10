"""
Find a magic index in a sorted array. An array value that is equal to the position
This can be implemented either through linear search or binary search
Time of linear search will be O(N)
while for binary search it will take O(log N)
"""

import unittest


def binary_search(array, left, right):
    """
    Binary search using a recursion
    :param array:
    :param left:
    :param right:
    :param x:
    :return:
    """
    if left < right:
        mid = (left + right)//2

        # if x is  the middle value then x is found
        if array[mid] == mid:
            return array[mid]

        # if x is greater than the middle value the x is on the right side
        elif array[mid] < mid:
            return binary_search(array, mid+1, right)

        # if x is less than the middle value then x is on the left side
        else:
            return binary_search(array, left, mid)
    else:
        return None


def magic_index_binary(array):
    if len(array) == 0 or array[0] > 0 or array[-1] < len(array) - 1:
        return None
    return binary_search(array, 0, len(array))


def magic_index_linear(array):
    for i in range(len(array)):
        if array[i] == i:
            return i
    return None


class Test(unittest.TestCase):
    data = [
        ([3,4,5], None),
        ([-2,-1,0,2], None),
        ([-20,0,1,2,3,4,5,6,20], None),
        ([-20,0,1,2,3,4,5,7,20], 7),
        ]

    def test_magic_index_binary(self):
        for [arr, expected] in self.data:
            result = magic_index_binary(arr)
            self.assertEqual(result, expected)

    def test_magic_index_linear(self):
        for [arr, expected] in self.data:
            result = magic_index_linear(arr)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()