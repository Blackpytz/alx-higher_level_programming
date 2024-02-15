#!/usr/bin/python3
"""
Defines unittest for models/square.py

Unittest classes:
    TestSquare_instantiation - line 23
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 3)
        s2 = Square(22, 9, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(Square(5, 2, 3, 9).size, 5)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_width_getter(self):
        s = Square(4, 1, 9, 3)
        s.size = 8

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 99
        self.assertEqual(s.height, 99)

    def test_x_getter(self):
        self.assertEqual(Square(10).x, 0)

    def test_y_getter(self):
        self.assertEqual(Square(50).y, 0)


if __name__ == "__main__":
    unittest.main()
