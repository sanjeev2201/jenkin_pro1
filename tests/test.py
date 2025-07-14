import unittest
from app import app

class TestBasic(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello", response.data)

if __name__ == '__main__':
    unittest.main()