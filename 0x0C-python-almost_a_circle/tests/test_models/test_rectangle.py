import unittest
from models.rectangle import Rectangle
from models.base import Base


class test_rectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_object = 0
        print("hello set up")

    def tearDown(self):
        pass

    def test_rectangle(self):
        r0 = Rectangle(10, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.id, 2)
        r3 = Rectangle(3, 2, id=None)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(3, 2, id=-4)
        self.assertEqual(r4.id, -4)
        r = Rectangle(10, 2, id=8)
        self.assertEqual(r.id, 8)
        r9 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r9.id, 12)
        r10 = Rectangle(10, 2, 3)
        self.assertEqual(r10.id, 4)
        r11 = Rectangle(10, 2, 3, 3)
        self.assertEqual(r11.id, 5)
        

        

    def test_area(self):
        r4 = Rectangle(2, 3, 3, 4, 9)
        self.assertEqual(r4.area(), 6)
