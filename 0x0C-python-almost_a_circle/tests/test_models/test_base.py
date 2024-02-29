import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0
    
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

    def test_type(self):
        b6 = Base()
        self.assertEqual(type(b6), Base)
        b7 = Base(2)
        self.assertEqual(type(b7), Base)

class test_to_json_string(unittest.TestCase):
    def test_to_json_string_None(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), '[]')

    def test_to_json_string_None(self):
        b = Base()
        self.assertEqual(b.to_json_string([]), '[]')

    def test_to_json_string_None(self):
        b = Base()
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
