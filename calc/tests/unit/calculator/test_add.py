from __future__ import absolute_import

import mock
import unittest

from calc import calculator


class TestAdd(unittest.TestCase):

    def test_add_two(self):
        self.assertEqual(4, calculator.add([2,2]))

    def test_add_three(self):
        self.assertEqual(4, calculator.add([1,2,1]))

    def test_add_mock(self):
        "Why is this a terrible test?"
        with mock.patch('calc.calculator.add') as mock_calculator:
            mock_calculator.return_value = 1
            self.assertEqual(1, calculator.add([4,3,1]))
