import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):

    def test_rectangle(self):
        r1 = Rectangle(10, 2, id=3)
        self.assertEqual(r1.id, 3)

    def test_exception_rec(self):
        with self.assertRaises(TypeError):
             r = Rectangle(10)
        
