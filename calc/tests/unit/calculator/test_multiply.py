from __future__ import absolute_import

import unittest

from calc import calculator


class TestMultiply(unittest.TestCase):

    def test_two_times_two(self):
        "Why does this work when the code is broken?"
        self.assertEqual(4, calculator.multiply([2,2]))

    def test_two_times_three_times_four(self):
        "Why does this work when the code is broken?"
        self.assertEqual(24, calculator.multiply([2,3,4]))
