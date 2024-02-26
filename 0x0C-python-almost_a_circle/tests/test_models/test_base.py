import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_equal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
