import unittest
from django.test import Client

# Create your tests here.

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client
        self.client = Client()

    def test_first_time_request(self):
        # issue a GET request
        response = self.client.get('/')

        # check that pid is in session and within range
        session = self.client.session.get('pid')
        self.assertIn(session, '0,1,2,3,4')

        # check that response is 200 OK
        self.assertEqual(response.status_code, 200)

        # check that rendered context has at least two articles
        self.assertGreaterEqual(len(response.context['articles']), 2)
