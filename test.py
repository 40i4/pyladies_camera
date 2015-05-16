# -*- coding: utf-8 -*-
"""
Unit tests.
"""
# pylint: disable=maybe-no-member, too-many-public-methods, invalid-name

import unittest

from main import app, cpu_choice


class LunchGameAppViewsTestCase(unittest.TestCase):
    """
    Views tests.
    """

    def setUp(self):
        """
        Before each test, set up a environment.
        """
        self.client = app.test_client()

    def test_mainpage_view(self):
        """
        Test main page view.
        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_play(self):
        """
        Test main page view.
        """
        resp = self.client.get('/play')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('rock', str(resp.data))
        self.assertIn('paper', str(resp.data))
        self.assertIn('scissors', str(resp.data))
        self.assertIn('spock', str(resp.data))
        self.assertIn('python', str(resp.data))

    def test_cpu(self):
        """
        Test main page view.
        """
        resp = cpu_choice()
        resp_2 = cpu_choice()
        resp_3 = cpu_choice()
        assert resp != resp_2 or resp_2 != resp_3 or resp_3 != resp




def suite():
    """
    Default test suite.
    """
    base_suite = unittest.TestSuite()
    base_suite.addTest(unittest.makeSuite(LunchGameAppViewsTestCase))
    return base_suite


if __name__ == '__main__':
    unittest.main()