import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.zero = [0, 7]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 6], [5, 4]), [7, 4])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([9, 10], [3, 5]), [3, 10])
        self.assertEqual(sub_frac([6, 7], [5, 3]), [-17, 21])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [1, 2]), [1, 3])
        self.assertEqual(mul_frac([6, 7], [5, 3]), [10, 7])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [1, 2]), [4, 3])
        self.assertEqual(div_frac([6, 7], [5, 3]), [18, 35])

    def test_is_positive(self):
        self.assertTrue(is_positive([6, 7]))
        self.assertFalse(is_positive([-6, 7]))
        self.assertFalse(is_positive([6, -7]))
        self.assertTrue(is_positive([-6, -7]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([2, 0]))
        self.assertTrue(is_zero([0, -2]))
        self.assertTrue(is_zero([0, 18]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)
        self.assertEqual(cmp_frac([4, 20], [2, 5]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([3, 4], [4, 7]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 1/2.)
        self.assertEqual(frac2float([0, 1]), 0.)
        self.assertEqual(frac2float([0, 2]), 0.)
        self.assertEqual(frac2float([1, 3]), 1/3.)
        self.assertEqual(frac2float([2, 6]), 1/3.)
        self.assertEqual(frac2float([5, 1]), 5.)

if __name__ == '__main__':
    unittest.main()
