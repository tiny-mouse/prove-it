from __future__ import absolute_import

import mock
from calc.tests.base import CalcTestBase


class TestMultiply(CalcTestBase):
    "This is a a real and proper unit test for what that view is doing"

    @mock.patch('calc.views.calculator')
    def test_multiply_two_numbers(self, mock_calculator):
        mock_calculator.multiply.return_value = 2
        resp = self.app.get('/multiply?numbers=1&numbers=2')
        self.assertEqual(2, int(resp.data))
        mock_calculator.add.assert_not_called()
        mock_calculator.multiply.assert_called_once_with([1,2])


