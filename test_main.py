from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_request():
    response = client.post("/api/requests", json={
        "course": "OAIS",
        "name": "Иван Иванов",
        "email": "ivan@mail.ru",
        "phone": "+79991234567"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["course"] == "OAIS"
    assert data["name"] == "Иван Иванов"
    assert "id" in data

def test_get_requests():
    response = client.get("/api/requests")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_request():
    create_response = client.post("/api/requests", json={"course": "OAIS"})
    request_id = create_response.json()["id"]
    response = client.get(f"/api/requests/{request_id}")
    assert response.status_code == 200
    assert response.json()["id"] == request_id

def test_update_request():
    create_response = client.post("/api/requests", json={"course": "OAIS"})
    request_id = create_response.json()["id"]
    # Для PUT нужно отправлять все обязательные поля
    response = client.put(f"/api/requests/{request_id}", json={"course": "OAIS", "name": "Петр Петров"})
    assert response.status_code == 200
    assert response.json()["name"] == "Петр Петров"

def test_delete_request():
    create_response = client.post("/api/requests", json={"course": "OAIS"})
    request_id = create_response.json()["id"]
    response = client.delete(f"/api/requests/{request_id}")
    assert response.status_code == 200
    get_response = client.get(f"/api/requests/{request_id}")
    assert get_response.status_code == 404

def test_patch_request():
    create_response = client.post("/api/requests", json={"course": "OAIS"})
    request_id = create_response.json()["id"]
    response = client.patch(f"/api/requests/{request_id}", json={"name": "Петр Петров"})
    assert response.status_code == 200
    assert response.json()["name"] == "Петр Петров"
