from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_history():
    response = client.get("/history")

    assert response.status_code == 200

def test_clear_history():
    response = client.delete("/history")

    assert response.status_code == 200


def test_calculate_then_history():

    client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": 2,
            "b": 3
        }
    )

    response = client.get("/history")

    assert response.status_code == 200
    assert len(response.json()) > 0
