import allure
import os
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_get


@allure.epic('API. Recipes')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Search Recipes")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_search_recipe(recipe='pasta', fat=25):
    schema = load_schema('search_recipe.json')
    api_key = os.getenv('API_key')
    url = 'recipes/complexSearch'
    params = {
        'apiKey': api_key,
        'query': recipe,
        'maxFat': fat,
        'number': 2
    }
    response = api_get(url, params=params)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert len(body.get('results')) == 2
    assert recipe in body.get('results')[0].get('title').lower()
    assert recipe in body.get('results')[1].get('title').lower()
    recipe_1_fat = body.get('results')[0].get('nutrition').get('nutrients')[0].get('amount')
    recipe_2_fat = body.get('results')[1].get('nutrition').get('nutrients')[0].get('amount')
    assert recipe_1_fat, recipe_2_fat < 25


@allure.epic('API. Recipes')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Search Recipes")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_search_similar_recipe():
    schema = load_schema('search_similar_recipe.json')
    api_key = os.getenv('API_key')
    url = 'recipes/complexSearch'
    params = {
        'apiKey': api_key,
        'query': 'pasta',
        'maxFat': 25,
        'number': 1
    }
    response = api_get(url, params=params).json().get('results')[0].get('id')
    print(response)
    recipe_id = api_get(url, params=params).json().get('results')[0].get('id')
    url = f'recipes/{recipe_id}/similar'
    params = {
        'apiKey': api_key,
        'number': 1
    }
    response = api_get(url, params=params)
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
    assert len(response.json()) == 1
