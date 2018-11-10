"""
On a given polygon with n corners there an ant on each one of the corners.
All ants randomly pick a direction and start moving along edge of the polygon.
What is the probability that any two ants collide?
"""
import unittest


def ants_on_a_polygon(n):
    # ants won't collide if they all pick to go clockwise or anti-clockwise. only 2 possibilities
    total_possibilities = 2**n
    return (total_possibilities-2)/total_possibilities


class Test(unittest.TestCase):
    def test_ants_on_a_polygon(self):
        self.assertEqual(ants_on_a_polygon(3), 0.75)
        self.assertEqual(ants_on_a_polygon(4), 0.875)


if __name__ == "__main__":
    unittest.main()