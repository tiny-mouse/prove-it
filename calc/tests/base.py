from __future__ import absolute_import

import unittest
from calc import views


class CalcTestBase(unittest.TestCase):

    def setUp(self):
        self.app = views.app.test_client()
