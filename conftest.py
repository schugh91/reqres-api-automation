import pytest
from utils.config import API_KEY, BASE_URL
import requests
import random

@pytest.fixture
def headers():
    return{
        "x-api-key": API_KEY,
    }


@pytest.fixture
def random_users(headers):
    response = requests.get(f"{BASE_URL}/api/users?page=2", headers=headers)
    data = response.json()
    assert response.status_code == 200
    users = data["data"]

    # getting user id and first name for random user
    selected_user = random.choice(users)

    return{
        "id": selected_user["id"],
        "first_name": selected_user["first_name"],
        "last_name": selected_user["last_name"],
    }


@pytest.fixture
def user_details():
    return{
        "id": "13",
        "email": "Surabhi.Chugh@reqres.in",
        "first_name": "Surabhi",
        "last_name": "Chugh"
    }

@pytest.fixture
def update_user():
    return{
        "first_name" : "Rishu",
        "last_name" : "Singh"
    }