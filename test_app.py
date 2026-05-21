import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_calculate_empty_json(self):
        # Перевірка поведінки при порожньому запиті
        response = self.app.post('/calculate', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()