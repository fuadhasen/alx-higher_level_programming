import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


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

class test_create_Rectangle(unittest.TestCase):
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

class test_create_Square(unittest.TestCase):
    def test_creat_withId(self):
        r = Square.create(**{ 'id': 89 })
        self.assertEqual(r.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

    def test_creat_size(self):
        r = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(r.to_dictionary(),  {'id': 89, 'size': 1, 'x': 0, 'y': 0})
   
    def test_creat_x(self):
        r = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(r.to_dictionary(),  {'id': 89, 'size': 1, 'x': 2, 'y': 0})

    def test_creat_y(self):
        r = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(r.to_dictionary(),  {'id': 89, 'size': 1, 'x': 2, 'y': 3})

class test_save_to_file_Rectangle(unittest.TestCase):
    def test_None(self):
        Square.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
    
    def test_Empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            correct = f.read()
        obj = json.loads(correct)
        self.assertEqual([], obj)
    
    def test_instance(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 6)])
        with open("Rectangle.json", "r") as f:
            correct = f.read()
        obj = json.loads(correct)
        self.assertEqual([{'id': 6, 'width': 1, 'height': 2, 'x': 3, 'y': 4}], obj)
    
class load_from_file_Rectangle(unittest.TestCase):
    def test_if_file_no_exist(self):
        filename = "Rectangle.json"
        if os.path.isfile(filename):
            os.remove(filename)
        correct = Rectangle.load_from_file()
        self.assertEqual([], correct)
    
    def test_if_file_exist(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        correct = Rectangle.load_from_file()

        self.assertEqual(len(correct), len(list_rectangles_input))

class test_save_to_file_Square(unittest.TestCase):
    def test_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
    
    def test_Empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            correct = f.read()
        obj = json.loads(correct)
        self.assertEqual([], obj)
    
    def test_instance(self):
        Square.save_to_file([Square(1, 2, 3, 4)])
        with open("Square.json", "r") as f:
            correct = f.read()
        obj = json.loads(correct)
        self.assertEqual([{'id': 4, 'size': 1, 'x': 2, 'y': 3}], obj)

class load_from_file_square(unittest.TestCase):
    def test_if_file_no_exist(self):
        filename = "Square.json"
        if os.path.isfile(filename):
            os.remove(filename)
        correct = Square.load_from_file()
        self.assertEqual([], correct)
    
    def test_if_file_exist(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        correct = Square.load_from_file()

        self.assertEqual(len(correct), len(list_squares_input))