import allure
import os
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_post, api_delete


@allure.epic('API. Connecting user')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Generate username, hash, password")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_add_and_delete_item_from_shopping_list(get_user_info):
    schema = load_schema('add_to_shopping.json')
    api_key = os.getenv('API_key')
    username = get_user_info[0]
    user_hash = get_user_info[1]
    url_add = f'mealplanner/{username}/shopping-list/items'
    item = {
        "item": "1 package baking powder",
        "aisle": "Baking",
        "parse": True
    }
    params = {
        'apiKey': api_key,
        'hash': user_hash
    }
    response_add = api_post(url_add, json=item, params=params)
    jsonschema.validate(response_add.json(), schema)
    assert response_add.status_code == 200
    assert response_add.json().get('name') == 'baking powder'
    item_id = response_add.json().get('id')
    url_delete = f'mealplanner/{username}/shopping-list/items/{item_id}'
    params = {
        'apiKey': api_key,
        'hash': user_hash
    }
    response_delete = api_delete(url_delete, params=params)
    assert response_delete.status_code == 200
    assert response_delete.json().get('status') == 'success'
