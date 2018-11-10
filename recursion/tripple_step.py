
import unittest


def triple_step(n):
    """
    USING RECURSION
    A child is running up a staircase with n steps and can jump either 1 step, 2 steps, or 3 steps
    at a time. Implement a method to count how many possible ways the child can run up the stairs.
    :param n: steps
    :return: possible ways
    """
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return triple_step(n-3) + triple_step(n-2) + triple_step(n-1)


def triple_step_dynamic(n):
    """
    DYNAMIC METHOD
    :param n:
    :return:
    """
    # initials
    res = [0] * (n+1)
    res[0], res[1], res[2] = 1, 1, 2

    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2] + res[i-3]
    return res[n]


class Test(unittest.TestCase):
    data = [
        (3, 4),
        (4, 7),
        (5, 13),
        (7, 44)
    ]

    def test_triple_step(self):
        for (n, expected) in self.data:
            res1 = triple_step(n)
            res2 = triple_step_dynamic(n)
            self.assertEqual(res1, expected)
            self.assertEqual(res2, expected)


if __name__ == "__main__":
    unittest.main()
