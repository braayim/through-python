"""
Given a matrix in which each row and each column is sorted, write a method to find
an element in it
"""
import unittest


def sorted_matrix_search(mat, item, x1=0, y1=0, x2=None, y2=None):
    if y2 is None:
        y2 = len(mat)
    if x2 is None:
        x2 = len(mat[0])

    if x1 == x2 or y1 == y2:
        return None
    row, col = (y1 + y2)//2, (x1 + x2)//2
    middle = mat[row][col]
    if middle == item:
        return row, col
    if middle > item:
        found = sorted_matrix_search(mat, item, x1, y1, col, row) or \
                sorted_matrix_search(mat, item, col, y1, col+1, row) or \
                sorted_matrix_search(mat, item, x1, row, col, row+1)
        if found:
            return found
    else:
        found = sorted_matrix_search(mat, item, col+1, row+1, x2, y2) or \
                sorted_matrix_search(mat, item, col, row+1, col+1, y2) or \
                sorted_matrix_search(mat, item, col+1, row, x2, row+1)
        if found:
            return found
    return sorted_matrix_search(mat, item, x1, row+1, col, y2) or\
           sorted_matrix_search(mat, item, col+1, y1, x2, row)


class Test(unittest.TestCase):
    def test_sorted_matrix_search(self):
        mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
               [5,  10, 15, 20, 25, 30, 35, 40, 45],
               [10, 20, 30, 40, 50, 60, 70, 80, 90],
               [13, 23, 33, 43, 53, 63, 73, 83, 93],
               [14, 24, 34, 44, 54, 64, 74, 84, 94],
               [15, 25, 35, 45, 55, 65, 75, 85, 95],
               [16, 26, 36, 46, 56, 66, 77, 88, 99]]
        self.assertEqual(sorted_matrix_search(mat, 10), (1,1))
        self.assertEqual(sorted_matrix_search(mat, 13), (3,0))
        self.assertEqual(sorted_matrix_search(mat, 14), (4,0))
        self.assertEqual(sorted_matrix_search(mat, 16), (6,0))
        self.assertEqual(sorted_matrix_search(mat, 56), (6,4))
        self.assertEqual(sorted_matrix_search(mat, 65), (5,5))
        self.assertEqual(sorted_matrix_search(mat, 74), (4,6))
        self.assertEqual(sorted_matrix_search(mat, 99), (6,8))


if __name__ == "__main__":
    unittest.main()