"""
Implement an algorithm to print all valid (e.g., properly opened and closed) combi-
nations of n-pairs of parentheses.
EXAMPLE:
input: 3 (e.g., 3 pairs of parentheses)
output: ()()(), ()(()), (())(), ((()))
"""
import unittest


def parens(n):
    parens_of_length = [[""]]
    if n == 0:
        return parens_of_length[0]
    for length in range(1, n + 1):
        parens_of_length.append([])
        for i in range(length):
            for inside in parens_of_length[i]:
                for outside in parens_of_length[length - i - 1]:
                    parens_of_length[length].append("(" + inside + ")" + outside)
    return parens_of_length[n]


class Test(unittest.TestCase):
    def test_parens(self):
        self.assertEqual(parens(1), ["()"])
        self.assertEqual(parens(2), ["()()", "(())"])
        self.assertEqual(parens(3), ["()()()", "()(())", "(())()", "(()())", "((()))"])


if __name__ == "__main__":
    unittest.main()