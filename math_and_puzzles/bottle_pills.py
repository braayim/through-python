"""
Problem: Given 10 identical bottles of identical pills (each bottle contain hundred of pills).
Out of 10 bottles 9 have 1 gram of pills but 1 bottle has pills of weight of 1.1 gram.
Given a measurement scale, how would you find the heavy bottle? You can use the scale only once.

"""
import unittest


def pill_bottle(bottles):

    pills = []
    for i, bottle in enumerate(bottles):
        pills += [bottle.pill()]*i
    weight = weight_scale(pills)
    index = (weight - (len(pills)*1.0))*10
    return int(index+0.1)


def weight_scale(weight):
    return sum(weight)


class Bottle:
    def __init__(self, pill_weight=1.0):
        self.pill_weight = pill_weight

    def pill(self):
        return self.pill_weight


class Test(unittest.TestCase):
    def test_pill_bottle(self):
        bottles = [Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
                   Bottle(), Bottle(1.1), Bottle(), Bottle(), Bottle(),
                   Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
                   Bottle(), Bottle(), Bottle(), Bottle(), Bottle()]
        self.assertEqual(pill_bottle(bottles), 6)


if __name__ == "__main__":
    unittest.main()