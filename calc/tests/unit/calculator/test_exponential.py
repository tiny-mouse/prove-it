from __future__ import absolute_import

import unittest

from calc import calculator


class TestExponential(unittest.TestCase):

    def test_two_squared(self):
        """What does this imply about adding many types of tests and not just
           assuming the one test case is ok?"""
        self.assertEqual(4, calculator.exponent([2,2]))

    def test_three_squared(self):
        self.assertEqual(9, calculator.exponent([3,2]))
