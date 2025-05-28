import unittest
import requests

class EndpointsTest(unittest.TestCase):
    BASE_URL = "https://your-app-url.com/api"  # Change to your app's API base URL

    def test_health_endpoint(self):
        """Test the health check endpoint."""
        response = requests.get(f"{self.BASE_URL}/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json())
        self.assertEqual(response.json()["status"], "ok")

    def test_login_endpoint(self):
        """Test the login endpoint with valid credentials."""
        payload = {"username": "user1", "password": "pass1"}
        response = requests.post(f"{self.BASE_URL}/login", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_login_endpoint_invalid(self):
        """Test the login endpoint with invalid credentials."""
        payload = {"username": "user1", "password": "wrong"}
        response = requests.post(f"{self.BASE_URL}/login", json=payload)
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json())

    def test_put_order_endpoint(self):
        """Test the put order endpoint."""
        # First, login to get a token
        login_payload = {"username": "user1", "password": "pass1"}
        login_response = requests.post(f"{self.BASE_URL}/login", json=login_payload)
        token = login_response.json().get("token")
        self.assertIsNotNone(token)

        headers = {"Authorization": f"Bearer {token}"}
        order_payload = {
            "order_type": "Put",
            "stock_symbol": "AAPL",
            "quantity": 10,
            "price": 150
        }
        response = requests.post(f"{self.BASE_URL}/orders", json=order_payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("order_id", response.json())

if __name__ == "__main__":
    unittest.main()
