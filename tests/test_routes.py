import unittest
from service import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        resp = self.app.get('/health')
        self.assertEqual(resp.status_code, 200)

    def test_index(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
