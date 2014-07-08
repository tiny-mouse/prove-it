from __future__ import absolute_import

import cassette
import unittest

from calc import otherapp


class TestIntegrationExample(unittest.TestCase):

    def setUp(self):
        self.app = otherapp.app.test_client()


    def test_with_cassette(self):
        "This really turns it into a unit test, not an integration test."
        with cassette.play("calc/tests/integration/responses.yaml"):
            self.app.get('/execute/add?number=2&numbers=3')


    def test_without_cassette(self):
        self.app.get('/execute/add?number=2&numbers=3')
