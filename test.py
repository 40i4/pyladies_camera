# -*- coding: utf-8 -*-
"""
Unit tests.
"""
# pylint: disable=maybe-no-member, too-many-public-methods, invalid-name

import unittest

from main import app


class LunchCameraAppViewsTestCase(unittest.TestCase):
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

    def test_browse_photos_view(self):
        """
        Test main page view.
        """
        resp = self.client.get('/photos')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Next photo', str(resp.data))
        self.assertIn('Previous photo', str(resp.data))
        self.assertIn('Download', str(resp.data))

    def test_make_photos_view(self):
        """
        Test main page view.
        """
        resp = self.client.get('/camera')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Capture a photo', str(resp.data))
        self.assertIn('Change aperture', str(resp.data))
        self.assertIn('Change time', str(resp.data))
        self.assertIn('Change ISO', str(resp.data))

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

    def test_brawse_photos_view(self):
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

    def test_make_photos_view(self):
        """
        Test main page view.
        """
        resp = self.client.get('/cpu_choice')
        self.assertEqual(resp.status_code, 200)
        resp_2 = self.client.get('/cpu_choice')
        self.assertEqual(resp.status_code, 200)
        resp_3 = self.client.get('/cpu_choice')
        self.assertEqual(resp.status_code, 200)
        assert resp != resp_2 or resp_2 != resp_3 or resp_3 != resp




def suite():
    """
    Default test suite.
    """
    base_suite = unittest.TestSuite()
    base_suite.addTest(unittest.makeSuite(LunchCameraAppViewsTestCase))
    base_suite.addTest(unittest.makeSuite(LunchGameAppViewsTestCase))
    return base_suite


if __name__ == '__main__':
    unittest.main()