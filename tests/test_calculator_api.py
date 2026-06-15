from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add():
    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15

def test_subtract():
    response = client.post(
        "/calculate",
        json={
            "operation": "subtract",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_multiply():
    response = client.post(
        "/calculate",
        json={
            "operation": "multiply",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 50

def test_divide():
    response = client.post(
        "/calculate",
        json={
            "operation": "divide",
            "a": 20,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 4

def test_divide_by_zero():
    response = client.post(
        "/calculate",
        json={
            "operation": "divide",
            "a": 20,
            "b": 0
        }
    )

    assert response.status_code == 400

def test_missing_field():
    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": 10
        }
    )

    assert response.status_code == 422

def test_invalid_datatype():
    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": "hello",
            "b": 5
        }
    )

    assert response.status_code == 422

def test_negative_numbers():
    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": -10,
            "b": -5
        }
    )

    assert response.json()["result"] == -15