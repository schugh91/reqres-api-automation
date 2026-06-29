import requests
from utils.config import BASE_URL

def test_get_single_user_data(headers, random_users):
    user_id = random_users["id"]
    response = requests.get(f"{BASE_URL}/api/users/{user_id}", headers=headers)

    data = response.json()
    assert response.status_code == 200
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 2000
    assert data["data"]["first_name"] == random_users["first_name"]
    assert data["data"]["id"] == user_id
