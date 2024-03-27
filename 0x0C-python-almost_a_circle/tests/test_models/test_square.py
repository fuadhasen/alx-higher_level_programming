import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class test_creat(unittest.TestCase):
    def test_square_instantiation_no_xy(self):
        s = Square(1)
        s1 = Square(2)
        self.assertEqual(s.id, s1.id - 1)
    
    def test_with_x(self):
        s1 = Square(1, 2)
        s2 = Square(2, 1)
        self.assertEqual(s1.id, s2.id - 1)
    
    def test_with_xy(self):
        s2 = Square(1, 2, 3)
        s1 = Square(1, 2, 4)
        self.assertEqual(s2.id, s1.id - 1)

    def test_with_xy_id(self):
        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.id, 4)
        
class test_Exception(unittest.TestCase):
    def test_square_TypeException(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("1")
        
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "1")
        
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2, "1")
    
    def test_square_ValueException(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -3)
        
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(2, 4, -1)
        
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

class test_stdout(unittest.TestCase):
    def test_str(self):
        s = Square(4, 2, 3)
        correct = "[Square] ({}) 2/3 - 4".format(s.id)
        self.assertEqual(correct, str(s))
    
    def test_to_dictionary(self):
        s = Square(2, 2, 3, 4)
        correct = {'id': 4, 'size': 2, 'x': 2, 'y': 3}
        self.assertEqual(correct, s.to_dictionary())

class test_update(unittest.TestCase):
    def test_update_no_arg(self):
        s = Square(3, 2, 3)
        correct = "[Square] ({}) 2/3 - 3".format(s.id)
        s.update()
        self.assertEqual(correct, str(s))
    
    def test_update_args_one(self):
        s = Square(3, 2, 3)
        correct = "[Square] (89) 2/3 - 3"
        s.update(89)
        self.assertEqual(correct, str(s))

        
    def test_update_args_two(self):
        s = Square(3, 2, 3)
        correct = "[Square] (89) 2/3 - 1"
        s.update(89, 1)
        self.assertEqual(correct, str(s))

    def test_update_args_three(self):
        s = Square(3, 2, 3)
        correct = "[Square] (89) 2/3 - 1"
        s.update(89, 1, 2)
        self.assertEqual(correct, str(s))

    def test_update_args_four(self):
        s = Square(3, 2, 3)
        correct = "[Square] (89) 2/3 - 1"
        s.update(89, 1, 2, 3)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_one(self):
        s = Square(3, 2, 3)
        correct = "[Square] (1) 2/3 - 3"
        s.update(id=1)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_two(self):
        s = Square(3, 2, 3)
        correct = "[Square] (1) 2/3 - 7"
        s.update(id=1, size=7)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_three(self):
        s = Square(3, 2, 3)
        correct = "[Square] (1) 8/3 - 7"
        s.update(id=1, size=7, x=8)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_four(self):
        s = Square(3, 2, 3)
        correct = "[Square] (1) 8/4 - 7"
        s.update(id=1, size=7, x=8, y=4)
        self.assertEqual(correct, str(s))

