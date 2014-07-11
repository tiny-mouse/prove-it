from __future__ import absolute_import

import mock
from calc.tests.base import CalcTestBase


class TestAdd(CalcTestBase):

    def test_add_input_validation(self):
        """You want to test the negative and positive. What happens when people
           give you bad input?
        """

        resp = self.app.get('/add')
        self.assertEqual(resp.data, 'You need to give numbers to add')
        self.assertEqual(resp.code, 400)

    def test_add_three_numbers(self):
        resp = self.app.get('/add?numbers=1&numbers=2&numbers=1')
        self.assertEqual(resp.data, '4')

    def test_add_mock(self):
        """Why is this test passing?"""
        with mock.patch('calc.views.calculator.add') as mock_calculator:
            mock_calculator.return_value = 1
            resp = self.app.get('/add?numbers=1&numbers=2')
            self.assertEqual(resp.data, '1')
            mock_calculator.assert_called_once_with([1,2])
