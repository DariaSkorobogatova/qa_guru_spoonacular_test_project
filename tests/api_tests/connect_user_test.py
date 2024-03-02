import allure
import os
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_get, api_post


@allure.epic('API. Connecting user')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Generate username, hash, password")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_connect_user(username='dasha'):
    schema = load_schema('connect_user.json')
    api_key = os.getenv('API_key')
    url = f'users/connect?apiKey={api_key}'
    data = {
        'username': username
    }
    response = api_post(url, json=data)
    body = response.json()
    print(body)
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body.get('username') is not None
    assert body.get('spoonacularPassword') is not None
    assert body.get('hash') is not None
