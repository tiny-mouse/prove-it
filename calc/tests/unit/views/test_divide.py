from __future__ import absolute_import

from calc.tests.base import CalcTestBase


class TestDivide(CalcTestBase):

    def test_divide_two_numbers(self):
        resp = self.app.get('/divide?numbers=3&numbers=4')
        self.assertEqual('0.75', resp.data)

    def test_divide_three_numbers(self):
        resp = self.app.get('/divide?numbers=6&numbers=3&numbers=2')
        self.assertEqual('1', resp.data)

