import unittest
from models.rectangle import Rectangle
from models.base import Base


class test_rectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_object = 0

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
        self.assertEqual(r1.id, 2)
        r = Rectangle(10, 2, id=8)
        self.assertEqual(r.id, 8)

    def test_exception(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10)

        with self.assertRaises(TypeError):
            r = Rectangle()        
