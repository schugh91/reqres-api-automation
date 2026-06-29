import requests
from utils.config import BASE_URL

def test_create_new_user(headers , user_details):
    response = requests.post(f"{BASE_URL}/api/users", headers = headers, json = user_details)
    data = response.json()

    assert response.status_code == 201
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 2000
    assert data["first_name"] == user_details["first_name"]
    assert data["id"] == user_details["id"]
    assert data["email"] == user_details["email"]
    assert data["last_name"] == user_details["last_name"]
    assert "id" in data