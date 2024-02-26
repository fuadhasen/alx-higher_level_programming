import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_equal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_nagative_input(self):
        b = Base(-12)
        self.assertEqual(b.id, -12)

    def test_maxid(self):
        with self.assertRaises(ValueError):
            b = Base(float('ínf'))

    def test_minid(self):
        with self.assertRaises(ValueError):
            b = Base(float('null')) 
