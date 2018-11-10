import unittest


def urlify(string):
    string1 = list(string.strip())
    length = len(string.strip())

    for i in range(length):
        if string1[i] == ' ':
            # Replace spaces
            string1[i] = '%20'
    return ''.join(string1)


class Test(unittest.TestCase):
    dataT = [
        ('much ado about nothing      ', 'much%20ado%20about%20nothing'),
        ('  Mr John Smith    ', 'Mr%20John%20Smith'),
        ('Mr John', 'Mr%20John')
    ]

    def test_urlify(self):
        for [test_string, expected] in self.dataT:
            result = urlify(test_string)
            print(result)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()




