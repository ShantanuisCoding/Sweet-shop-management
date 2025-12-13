from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def auth_header():
    client.post("/api/auth/register", json={
        "email": "search@test.com",
        "password": "password"
    })
    token = client.post("/api/auth/login", json={
        "email": "search@test.com",
        "password": "password"
    }).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def seed_sweets(headers):
    sweets = [
        {"name": "Ladoo", "category": "Indian", "price": 5, "quantity": 10},
        {"name": "Barfi", "category": "Indian", "price": 15, "quantity": 5},
        {"name": "Donut", "category": "Western", "price": 20, "quantity": 8},
    ]

    for sweet in sweets:
        client.post("/api/sweets", headers=headers, json=sweet)


def test_search_by_category():
    headers = auth_header()
    seed_sweets(headers)

    response = client.get(
        "/api/sweets/search?category=Indian",
        headers=headers
    )

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_search_by_price_range():
    headers = auth_header()
    seed_sweets(headers)

    response = client.get(
        "/api/sweets/search?min_price=10&max_price=20",
        headers=headers
    )

    assert response.status_code == 200
    assert len(response.json()) == 2
