from __future__ import absolute_import

import unittest

from calc import calculator


class TestSubtract(unittest.TestCase):

    def test_subtract_one(self):
        self.assertEqual(4, calculator.subtract([2]))

    def test_subtract_three(self):
        "Why is this test not great?"
        self.assertEqual(4, calculator.add([1,2,1]))

    def test_subtract_four(self):
        self.assertEqual(4, calculator.subtract([6,1,1]))

    def test_subtract_two(self):
        self.assertEqual(4, calculator.subtract([6,2]))
