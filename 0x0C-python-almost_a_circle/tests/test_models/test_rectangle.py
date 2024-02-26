import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):

    def test_without_id(self):
        r1 = Rectangle(10, 2, id=3)
        self.assertEqual(r1.id, 3)
