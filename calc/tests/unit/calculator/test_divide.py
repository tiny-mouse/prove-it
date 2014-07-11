from __future__ import absolute_import

import unittest

from calc import calculator


class TestDivide(unittest.TestCase):

    def test_divide_two(self):
        self.assertEqual(1, calculator.divide([1,1]))

    def test_divide_two_floats_bad(self):
        """Why is this test different than the next one?"""
        self.assertEqual(0.75, calculator.divide([3,4]))

    def test_divide_two_floats_good(self):
        self.assertEqual(0.75, calculator.divide([3.0,4.0]))

    def test_divide_three(self):
        self.assertEqual(1, calculator.divide([6,3,2]))

    def test_divide_by_zero(self):
        """What does the error on this test imply about our input validation?"""
        self.assertEqual(1, calculator.divide([1,0]))

    def test_divide_by_zero_error(self):
        """Check out this other type of assertion!"""
        self.assertRaises(ZeroDivisionError, calculator.divide, [1,0])
