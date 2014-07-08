from __future__ import absolute_import

from calc.tests.base import CalcTestBase


class TestExponential(CalcTestBase):

    def test_two_to_the_oneth_power(self):
        resp = self.app.get('/exponential?numbers=2&numbers=1')
        self.assertEqual(2, int(resp.data))

    def test_two_squared(self):
        resp = self.app.get('/exponential?numbers=2&numbers=2')
        self.assertEqual(4, int(resp.data))

    def test_two_squared_squared(self):
        resp = self.app.get('/exponential?numbers=2&numbers=2&numbers=2')
        self.assertEqual(8, int(resp.data))

    def test_three_squared(self):
        resp = self.app.get('/exponential?numbers=3&numbers=2')
        self.assertEqual(9, int(resp.data))
