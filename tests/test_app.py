import unittest

from app.app import app


class HelloEndpointTests(unittest.TestCase):
    def test_hello_endpoint_returns_greeting(self):
        with app.test_client() as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("hello", response.get_data(as_text=True).lower())
