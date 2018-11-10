"""
Computes a power set of a set
Power set P(S) of a set S is the set of all subsets of S.
For example S = {a, b, c} then
P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
"""
import unittest


def power_set(s):
    ps = {frozenset()}
    for element in s:
        additions = set()
        for subset in ps:
            additions.add(subset.union(element))
        ps = ps.union(additions)
    return ps


class Test(unittest.TestCase):
    def test_power_set(self):
        s = {'a', 'b', 'c', 'd'}
        ps = power_set(s)
        print(ps)
        self.assertEqual(len(ps), 16)
        subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
                   {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'},
                   {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]
        self.assertEqual(ps, set([frozenset(s) for s in subsets]))


if __name__ == "__main__":
    unittest.main()