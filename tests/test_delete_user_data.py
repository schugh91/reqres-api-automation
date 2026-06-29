import requests
from utils.config import BASE_URL

def test_delete_user_data(headers, random_users):
    response = requests.delete(f"{BASE_URL}/api/users/{random_users['id']}", headers=headers)
    assert response.status_code == 204
    assert response.text == ""
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 2000