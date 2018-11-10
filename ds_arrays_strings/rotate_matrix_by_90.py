"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
import unittest


def rotate_matrix_by_90(matrix):
    """
    Rotate a square matrix by 90 degrees clockwise
    :param matrix:
    :return:
    """
    n = len(matrix)
    for i in range(n//2):
        first, last = i, n-i-1
        for j in range(first, last):
            # save top
            top = matrix[i][j]
            # left to top
            matrix[i][j] = matrix[-j-1][i]
            # bottom to left
            matrix[-j-1][i] = matrix[-i-1][-j-1]
            # right to bottom
            matrix[-i-1][-j-1] = matrix[j][-i - 1]
            # top to right
            matrix[j][-i-1] = top

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
             [1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [21, 16, 11, 6, 1],
             [22, 17, 12, 7, 2],
             [23, 18, 13, 8, 3],
             [24, 19, 14, 9, 4],
             [25, 20, 15, 10, 5]
         ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix_by_90(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
