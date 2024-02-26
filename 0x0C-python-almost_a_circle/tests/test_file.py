import unittest
"""this module provide class to test string. """


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        """test is equal. """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """test is upper. """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
