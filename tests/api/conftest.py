import pytest
from dotenv import load_dotenv
import os
from spoonacular_test_project.helper.api_requests import api_post


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=False)
def get_user_info():
    username = os.getenv('dasha_skorobogatova')
    api_key = os.getenv('API_key')
    url = f'users/connect'
    params = {
        'apiKey': api_key
    }
    data = {
        'username': username
    }
    response = api_post(url, json=data, params=params)
    body = response.json()
    return body.get('username'), body.get('hash')
