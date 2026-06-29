import requests
from utils.config import BASE_URL
import random

def test_get_users(headers):

    response = requests.get(f"{BASE_URL}/api/users?page=2", headers=headers)
    data = response.json()
    assert response.status_code == 200
    assert data["per_page"] == 6
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 2000
