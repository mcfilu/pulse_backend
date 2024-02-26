from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_user_correct():
    response = client.get("/users/1")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['id'] == 1
    assert user_data['email'] == 'george.bluth@reqres.in'

def test_get_user_minus():
    response = client.get("/users/-1")
    assert response.status_code == 404
    

def test_get_user_zero():
    response = client.get("/users/0")
    assert response.status_code == 404

def test_get_user_big():
    response = client.get("/users/999999999999999999")
    assert response.status_code == 404

def test_get_user_int():
    response = client.get("/users/adsasdga")
    assert response.status_code == 422

def test_get_user_invalid_url():
    response = client.get("/nonexistent")
    assert response.status_code == 404


