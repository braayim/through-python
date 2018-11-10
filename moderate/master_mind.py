"""
The computer has four slots containing balls that are red (R), yellow (Y), green (G) or
blue (B). For example, the computer might have RGGB (e.g., Slot #1 is red, Slots #2 and
#3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a “hit”. If you guess
a color that exists but is in the wrong slot, you get a “pseudo-hit”. For example, the
guess YRGB has 2 hits and one pseudo hit.
For each guess, you are told the number of hits and pseudo-hits.
Write a method that, given a guess and a solution, returns the number of hits and
pseudo hits.
"""
import unittest


def mastermind_hits(code, guess):
    this_code = list(code)
    hits, pseudo_hit = 0, 0

    for i, color in enumerate(guess):
        if this_code[i] == color:
            hits += 1
        elif color in this_code:
            pseudo_hit += 1

    return hits, pseudo_hit


class Test(unittest.TestCase):
    def test_mastermind_hits(self):
        self.assertEqual(mastermind_hits("RGGB", "YRGB"), (2, 1))


if __name__ == "__main__":
    unittest.main()