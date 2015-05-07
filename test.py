# -*- coding: utf-8 -*-
"""
Unit tests.
"""
# pylint: disable=maybe-no-member, too-many-public-methods, invalid-name

import unittest

from main import app


class LunchBackendViewsTestCase(unittest.TestCase):
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


class LunchCameraTestCase(unittest.TestCase):
    """
    Views tests.
    """

    def setUp(self):
        """
        Before each test, set up a environment.
        """
        pass

    def camera_library_test(self):
        self.assertEquals("ala", "ALA".lower())


def suite():
    """
    Default test suite.
    """
    base_suite = unittest.TestSuite()
    base_suite.addTest(unittest.makeSuite(LunchBackendViewsTestCase))
    base_suite.addTest(unittest.makeSuite(LunchCameraTestCase))
    return base_suite


if __name__ == '__main__':
    unittest.main()