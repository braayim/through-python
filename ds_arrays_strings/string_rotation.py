import unittest


def string_rotation(s1, s2):
    """
    Determines whether or not a given string is a rotation of another string
    :param s1:
    :param s2:
    :return:
    """
    if len(s1) == len(s2) != 0:
        string = s1+s1
        return string.find(s2) != -1
    return False


class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('abrahamskits', 'kitsabrahams', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
