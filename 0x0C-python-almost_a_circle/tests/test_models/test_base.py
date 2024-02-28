import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_base_creation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(4)
        self.assertEqual(b3.id, 4)
        b4 = Base(None)
        self.assertEqual(b4.id, 3)
        b5 = Base(-4)
        self.assertEqual(b5.id, -4)
