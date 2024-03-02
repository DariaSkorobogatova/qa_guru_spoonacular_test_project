import pytest
import allure
import os
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_get, api_post


@allure.epic('API. Ingredients')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Search ingredients")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
@pytest.mark.parametrize('ingredient', ['ice cream', 'butter', 'egg'])
def test_search_ingredients(ingredient):
    schema = load_schema('search_ingredients.json')
    api_key = os.getenv('API_key')
    url = f'food/ingredients/search?apiKey={api_key}&query={ingredient}&number=3'
    response = api_get(url)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert len(body.get('results')) == 3
    assert ingredient in body.get('results')[0].get('name')
    assert ingredient in body.get('results')[1].get('name')
    assert ingredient in body.get('results')[2].get('name')


@allure.epic('API. Ingredients')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Search non-existing ingredient")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_search_non_existing_ingredient(ingredient='ksjhfkjds'):
    schema = load_schema('search_ingredients.json')
    api_key = os.getenv('API_key')
    url = f'food/ingredients/search?apiKey={api_key}&query={ingredient}&number=3'
    response = api_get(url)
    body = response.json()
    assert response.status_code == 200
    assert body.get('results') == []
    jsonschema.validate(body, schema)


@allure.epic('API. Ingredients')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Get Ingredient Information")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_get_ingredient_info():
    schema = load_schema('ingredient_info.json')
    api_key = os.getenv('API_key')
    ingredient_id = api_get(f'food/ingredients/search?apiKey={api_key}&query=ice cream').json().get('results')[0].get(
        'id')
    url = f'food/ingredients/{ingredient_id}/information?apiKey={api_key}&amount=1'
    response = api_get(url)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert 'icecream sandwiches' in body.get('name')
    assert body.get('amount') == 1
    assert body.get('possibleUnits') == ['package', 'piece', 'g', 'box', 'oz']
    assert body.get('estimatedCost') == {'value': 25.0, 'unit': 'US Cents'}
    assert body.get('aisle') == 'Frozen'
    assert len(body.get('nutrition').get('nutrients')) == 37


@allure.epic('API. Ingredients')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Get Ingredient Information")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_get_ingredient_info_with_invalid_id(ingredient_id=0):
    schema = load_schema('invalid_ingredient_id.json')
    api_key = os.getenv('API_key')
    url = f'food/ingredients/{ingredient_id}/information?apiKey={api_key}&amount=1'
    response = api_get(url)
    assert response.status_code == 404
    jsonschema.validate(response.json(), schema)
    assert response.json()['message'] == 'An ingredient with the id 0 does not exist.'


@allure.epic('API. Ingredients')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Compute Glycemic Load")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_compute_glycemic_load():
    schema = load_schema('compute_glycemic_load.json')
    api_key = os.getenv('API_key')
    url = f'food/ingredients/glycemicLoad?apiKey={api_key}'
    data = {
        "ingredients": [
            "1 kiwi",
            "2 cups rice",
            "2 glasses of water"
        ]
    }
    response = api_post(url, json=data)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body.get('totalGlycemicLoad') == 183.32
    assert len(body.get('ingredients')) == 3
