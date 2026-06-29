import requests
from utils.config import BASE_URL

def test_update_user_details(headers, update_user, random_users):
    response = requests.put(f"{BASE_URL}/api/users/{random_users['id']}",headers=headers, json = update_user)
    assert response.status_code == 200
    data = response.json()
    assert "updatedAt" in data
    assert data["first_name"] == update_user["first_name"]
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 2000
