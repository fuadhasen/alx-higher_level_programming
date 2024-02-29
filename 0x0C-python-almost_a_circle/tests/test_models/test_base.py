import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class test_base(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0
    
    def tearDown(self):
        pass

    def test_base_creation(self):
        b1 = Base()
        self.assertTrue(b1.id)
    def test_base_creation__autoId(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b3.id - 1)

    def test_Base_None(self):
        b4 = Base(None)
        b0 = Base(5)
        self.assertNotEqual(b4.id, b0.id)

    def test_base_withid(self):
        b5 = Base(-4)
        b6 = Base(4)
        self.assertNotEqual(b5.id, b6.id)

    def test_type(self):
        b6 = Base()
        self.assertEqual(type(b6), Base)
        b7 = Base(2)
        self.assertEqual(type(b7), Base)

class test_to_json_string(unittest.TestCase):
    def test_to_json_string_None(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), '[]')

    def test_to_json_string_Empty(self):
        b = Base()
        self.assertEqual(b.to_json_string([]), '[]')

    def test_to_json_string_object(self):
        b = Base()
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')


class test_from_json_string(unittest.TestCase):
    def test_to_json_string_None(self):
        b = Base()
        self.assertEqual(b.from_json_string(None), [])
    
    def test_to_json_string_Empty(self):
        b = Base()
        self.assertEqual(b.from_json_string("[]"), [])
    
    def test_to_json_string_object(self):
        b = Base()
        self.assertEqual(b.from_json_string('[{ "id": 89 }]'), [{ 'id': 89 }])

class test_create(unittest.TestCase):
    def test_creat_withId(self):
        r = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_creat_width(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2, 'x': 0, 'y': 0})
    
    def test_creat_height(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_creat_x(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 0})

    def test_creat_y(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

class test_save_to_file(unittest.TestCase):
    def test_None(self):
        Rectangle.save_to_file(None)
        os.path.isfile("Rectangle.json")
    
    def test_Empty(self):
        Rectangle.save_to_file([])
        os.path.isfile("Rectangle.json")
    
    def test_(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        os.path.isfile("Rectangle.json")