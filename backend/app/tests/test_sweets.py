from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def register_and_login():
    client.post("/api/auth/register", json={
        "email": "user@sweets.com",
        "password": "password"
    })
    response = client.post("/api/auth/login", json={
        "email": "user@sweets.com",
        "password": "password"
    })
    return response.json()["access_token"]


def test_create_sweet():
    token = register_and_login()

    response = client.post(
        "/api/sweets",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Gulab Jamun",
            "category": "Indian",
            "price": 10.5,
            "quantity": 100
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Gulab Jamun"


def test_get_all_sweets():
    token = register_and_login()

    response = client.get(
        "/api/sweets",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
