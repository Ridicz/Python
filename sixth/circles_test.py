import unittest
from circles import *


class TestCircle(unittest.TestCase):

    def setUp(self): pass

    def test_init(self):
        self.assertRaises(ValueError, Circle, 2, 2, -1)
        self.assertRaises(ValueError, Circle, "String")

    def test_repr(self):
        self.assertEqual(repr(Circle(1, 2, 3)), "Circle(1, 2, 3)")
        self.assertEqual(repr(Circle(5, 6, 1)), "Circle(5, 6, 1)")

    def test_eq(self):
        self.assertTrue(Circle(1, 1) == Circle(1, 1, 1))
        self.assertTrue(Circle(2, 3, 1) == Circle(2, 3))
        self.assertTrue(Circle(3, 3, 4) == Circle(3, 3, 4))
        self.assertFalse(Circle(3, 2) == Circle(3, 2, 2))
        self.assertFalse(Circle(3.1, 2) == Circle(3, 2))
        self.assertTrue(Circle(3.5, 2.2, 2) == Circle(3.5, 2.2, 2))
        with self.assertRaises(ValueError):
            Circle.__eq__(Circle(1, 1, 1), 0)

    def test_ne(self):
        self.assertFalse(Circle(1, 1) != Circle(1, 1, 1))
        self.assertFalse(Circle(2, 3, 1) != Circle(2, 3))
        self.assertFalse(Circle(3, 3, 4) != Circle(3, 3, 4))
        self.assertTrue(Circle(3, 2) != Circle(3, 2, 2))
        self.assertTrue(Circle(3.1, 2) != Circle(3, 2))
        self.assertFalse(Circle(3.5, 2.2, 2) != Circle(3.5, 2.2, 2))
        with self.assertRaises(ValueError):
            Circle.__eq__(Circle(1, 1, 1), 0)

    def test_area(self):
        self.assertEqual(Circle(0.5, 0.7, 1).area(), pi)
        self.assertEqual(Circle(0.5, 0.7, 3.7).area(), Circle(1212, 1232, 3.7).area())
        self.assertEqual(Circle(0.5, 0.7, 5).area(), pi * 25)
        self.assertNotEqual(Circle(1, 2, 2).area(), Circle(1, 2, 3).area())
        self.assertNotEqual(Circle(0, 0).area(), Circle(5, 5, 3).area())

    def test_move(self):
        self.assertEqual(Circle(5, 6, 7).move(1, 1), Circle(6, 7, 7))
        self.assertEqual(Circle(5, 6, 7).move(0, 0), Circle(5, 6, 7))
        self.assertEqual(Circle(5, 6, 7).move(-1, -1), Circle(4, 5, 7))
        self.assertEqual(Circle().move(7, 3), Circle(7, 3))
        with self.assertRaises(ValueError):
            Circle(5, 5).move("string", 5)

    def test_cover(self):
        self.assertEqual(Circle(1, 1, 1).cover(Circle(3, 1, 1)), Circle(2, 1, 2))
        self.assertEqual(Circle(1, 1, 1).cover(Circle(1, 5, 2)), Circle(1, 3.5, 3.5))
        self.assertEqual(Circle(1, 1, 1).cover(Circle(2, 1, 5)), Circle(2, 1, 5))
        self.assertEqual(Circle(4, 6, 10).cover(Circle(4, 1, 5)), Circle(4, 6, 10))
        self.assertEqual(Circle(0, 0, 10).cover(Circle(10, 0, 10)), Circle(5, 0, 15))
        with self.assertRaises(ValueError):
            Circle(4, 4, 4).cover(10)

if __name__ == '__main__':
    unittest.main()
