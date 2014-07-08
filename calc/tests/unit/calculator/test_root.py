from __future__ import absolute_import

import unittest

from calc import calculator


class TestRoot(unittest.TestCase):

    def test_two_root_of_four(self):
        self.assertEqual(2, calculator.root([4,2]))
