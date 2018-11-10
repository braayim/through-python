"""
Suppose you have a 3 liter jug and a 5 liter jug (this could also be in gallons).
The jugs have no measurement lines on them either. How could you measure exactly 4
liter using only those jugs and as much extra water as you need?
"""
import unittest


class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.water = 0

    def fill(self):
        self.water = self.capacity

    def empty(self):
        self.water = 0

    def pour(self, jug):
        total = self.water + jug.water
        jug.water = min(jug.capacity, total)
        self.water = total - jug.water


def measure_four():
    jug3 = Jug(3)
    jug5 = Jug(5)

    # fill jug5
    jug5.fill()

    # pour jug5 to jug3 and jug5 will remain with 2 litres
    jug5.pour(jug3)

    # empty jug3 and pour the 2 litres in jug5
    jug3.empty()
    jug5.pour(jug3)

    # fill jug5 and pour to jug3 remember jug3 contains 2 litres
    jug5.fill()
    jug5.pour(jug3)

    return jug5.water


class Test(unittest.TestCase):
    def test_measure_four(self):
        self.assertEqual(measure_four(), 4)


if __name__ == "__main__":
    unittest.main()