import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class test_rectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_object = 0
        print("hello set up")

    def tearDown(self):
        pass

    def test_rectangle(self):
        r0 = Rectangle(10, 2)
        self.assertTrue(r0.id)
        r1 = Rectangle(3, 2)
        self.assertTrue(r1.id, 2)
        r9 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r9.id, 12)
        r10 = Rectangle(10, 2, 3)
        self.assertTrue(r10.id)
        r11 = Rectangle(10, 2, 3, 3)
        self.assertTrue(r11.id)

    def test_rec_TypeException(self):
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle("1", 2)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r2 = Rectangle(1, "2")
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r3 = Rectangle(1, 2, "3")
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r4 = Rectangle(1, 2, 3, "2")
        self.assertEqual("y must be an integer", str(x.exception))

    def test_rec_ValueError(self):
        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(-1, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r2 = Rectangle(1, -2)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r4 = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r5 = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r6 = Rectangle(1, 2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r7 = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r4 = Rectangle(2, 3, 3, 4, 9)
        self.assertEqual(r4.area(), 6)

class test_stdout(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
        print("second set up alew")

    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_display_with_position(self):
        r = Rectangle(3, 5, 0, 1, 0)
        capture = test_stdout.capture_stdout(r, "display")
        display = "\n###\n###\n###\n###\n###\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_without_y(self):
        r = Rectangle(3, 5, 1)
        capture = test_stdout.capture_stdout(r, "display")
        display = " ###\n ###\n ###\n ###\n ###\n"
        self.assertEqual(display, capture.getvalue())
    def test_disp_without_xy(self):
        r = Rectangle(3, 5)
        capture = test_stdout.capture_stdout(r, "display")
        display = "###\n###\n###\n###\n###\n"
        self.assertEqual(display, capture.getvalue())

class test_update(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))
        
    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual("[Rectangle] (89) 10/10 - 1/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))
    
    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())


