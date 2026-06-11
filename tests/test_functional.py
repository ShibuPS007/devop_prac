from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.json() == {"status": "healthy"}


def test_add_endpoint():
    response = client.get("/add?a=10&b=5")
    assert response.json()["result"] == 15


def test_division_by_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.json()["error"] == "Division by zero not allowed"