"""
Return the frequency of a word in a given text
"""
import unittest


def word_frequency(text, x):
    lines = text.strip().split("\n")
    total_words = 0
    word_count = 0

    for line in lines:
        words = line.strip().split(" ")
        for word in words:
            if word == x:
                word_count += 1
            total_words += 1
    return float(word_count)/total_words


class Test(unittest.TestCase):
    def test_word_frequency(self):
        text = """
        When the sun shines, we'll shine together
        Told you I'd be here forever
        Said I'll always be a friend
        Took an oath I'ma stick it out 'til the end
        Now that it's raining more than ever
        Know that we'll still have each other
        You can stand under my umbrella
        You can stand under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh eh eh eh)"""
        stats = word_frequency(text, "umbrella")
        self.assertEqual(stats, 5 / 87.0)


if __name__ == "__main__":
    unittest.main()