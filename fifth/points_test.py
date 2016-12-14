import unittest
from points import *


class TestPoints(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Point(12, 44)), "(12, 44)")
        self.assertEqual(str(Point(31, 23)), "(31, 23)")

    def test_repr(self):
        self.assertEqual(repr(Point(12, 44)), "Point(12, 44)")
        self.assertEqual(repr(Point(31, 23)), "Point(31, 23)")

    def test_eq(self):
        self.assertTrue(Point(12, 44) == Point(12, 44))
        self.assertFalse(Point(12, 44) == Point(31, 23))

    def test_ne(self):
        self.assertFalse(Point(12, 44) != Point(12, 44))
        self.assertTrue(Point(12, 44) != Point(31, 23))

    def test_add(self):
        self.assertEqual(Point(12, 44) + Point(12, 44), Point(24, 88))
        self.assertEqual(Point(31, 23) + Point(12, 44), Point(43, 67))
        self.assertEqual(Point(12, 44) + Point(31, 23), Point(43, 67))
        self.assertEqual(Point(31, 44) + Point(12, 23), Point(43, 67))

    def test_sub(self):
        self.assertEqual(Point(12, 44) - Point(12, 44), Point(0, 0))
        self.assertEqual(Point(31, 23) - Point(12, 44), Point(19, -21))
        self.assertEqual(Point(12, 44) - Point(31, 23), Point(-19, 21))
        self.assertEqual(Point(31, 44) - Point(12, 23), Point(19, 21))

    def test_mul(self):
        self.assertEqual(Point(12, 44) * Point(12, 44), 2080)
        self.assertEqual(Point(31, 23) * Point(12, 44), 1384)
        self.assertEqual(Point(12, 44) * Point(31, 23), 1384)
        self.assertEqual(Point(31, 44) * Point(12, 23), 1384)

    def test_cross(self):
        self.assertEqual(Point(31, 44).cross(Point(12, 23)), 185)
        self.assertEqual(Point(23, 44).cross(Point(12, 23)), 1)
        self.assertEqual(Point(44, 12).cross(Point(12, 23)), 868)

    def test_length(self):
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(8, 6).length(), 10)
        self.assertEqual(Point(4, 3).length(), 5)
        self.assertEqual(Point(15, 0).length(), 15)

if __name__ == '__main__':
    unittest.main()
