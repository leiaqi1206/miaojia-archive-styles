import unittest

from fastapi.testclient import TestClient

from app.main import app


class ApiEndpointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_health_endpoint_returns_ok(self) -> None:
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_message_endpoint_returns_message(self) -> None:
        response = self.client.get("/api/message")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "喵家档案后端连接成功"})


if __name__ == "__main__":
    unittest.main()
