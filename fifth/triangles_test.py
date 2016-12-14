import unittest
from triangles import *


class TestTriangle(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Triangle(1, 2, 3, 4, 5, 6)), "[(1, 2), (3, 4), (5, 6)]")
        self.assertEqual(str(Triangle(3, 5, 1, 4, 2, 9)), "[(3, 5), (1, 4), (2, 9)]")

    def test_repr(self):
        self.assertEqual(repr(Triangle(1, 2, 3, 4, 5, 6)), "Triangle(1, 2, 3, 4, 5, 6)")
        self.assertEqual(repr(Triangle(3, 5, 1, 4, 2, 9)), "Triangle(3, 5, 1, 4, 2, 9)")

    def test_eq(self):
        self.assertTrue(Triangle(1, 2, 3, 4, 5, 6) == Triangle(1, 2, 3, 4, 5, 6))
        self.assertFalse(Triangle(1, 2, 3, 4, 5, 6) == Triangle(3, 5, 1, 4, 2, 9))

    def test_ne(self):
        self.assertFalse(Triangle(1, 2, 3, 4, 5, 6) != Triangle(1, 2, 3, 4, 5, 6))
        self.assertTrue(Triangle(1, 2, 3, 4, 5, 6) != Triangle(3, 5, 1, 4, 2, 9))

    def test_center(self):
        self.assertEqual(Triangle(1, 2, 3, 4, 5, 6).center(), Point(3, 4))
        self.assertEqual(Triangle(3, 5, 1, 4, 2, 9).center(), Point(2, 6))

    def test_area(self):
        self.assertAlmostEqual(Triangle(1, 1, 5, 1, 3, 5).area(), 8)
        self.assertAlmostEqual(Triangle(1, 2, 0, 4, -3, -3).area(), 6.5)

    def test_move(self):
        self.assertEqual(Triangle(1, 1, 5, 1, 3, 5).move(1, 3), Triangle(2, 4, 6, 4, 4, 8))
        self.assertEqual(Triangle(1, 1, 5, 1, 3, 5).move(4, 2), Triangle(5, 3, 9, 3, 7, 7))

if __name__ == '__main__':
    unittest.main()
