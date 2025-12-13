from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def auth_header():
    client.post("/api/auth/register", json={
        "email": "inventory@test.com",
        "password": "password"
    })
    token = client.post("/api/auth/login", json={
        "email": "inventory@test.com",
        "password": "password"
    }).json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def create_sweet(quantity: int):
    response = client.post(
        "/api/sweets",
        headers=auth_header(),
        json={
            "name": "Ladoo",
            "category": "Indian",
            "price": 5.0,
            "quantity": quantity
        }
    )
    return response.json()["id"]


def test_purchase_sweet_decreases_quantity():
    sweet_id = create_sweet(2)

    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        headers=auth_header()
    )

    assert response.status_code == 200
    assert response.json()["quantity"] == 1


def test_purchase_fails_when_out_of_stock():
    sweet_id = create_sweet(0)

    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        headers=auth_header()
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Out of stock"
