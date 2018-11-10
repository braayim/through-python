import unittest


def compress_string(string):
    """
    It compresses a string where by repeating character are reduced to that
    character plus their count e.g aaaabbc -> a3b2c
    :param string:
    :return:
    """
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            compressed.append(string[i-1]+str(counter))
            counter = 0
        counter += 1

    compressed.append(string[-1]+str(counter))
    new_string = ''.join(compressed)
    return new_string.replace('1', '')


class Test(unittest.TestCase):
    """
    Test Case
    """
    data = [
        ('aabcccccaaa', 'a2bc5a3'),
        ('aabcccccd', 'a2bc5d'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = compress_string(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
