import allure
import os
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_get


@allure.epic('API. Meal planner')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Generating meal plan")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_generate_meal_plan_day():
    schema = load_schema('meal_plan_day.json')
    api_key = os.getenv('API_key')
    url = 'mealplanner/generate'
    params = {
        'apiKey': api_key,
        'timeFrame': 'day'
    }
    response = api_get(url, params=params)
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
    assert len(response.json().get('meals')) == 3


@allure.epic('API. Meal planner')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Generating meal plan")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_generate_meal_plan_with_calories_limit(calories=2000):
    schema = load_schema('meal_plan_day.json')
    api_key = os.getenv('API_key')
    url = 'mealplanner/generate'
    params = {
        'apiKey': api_key,
        'timeFrame': 'day',
        'targetCalories': calories
    }
    response = api_get(url, params=params)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert len(body.get('meals')) == 3
    assert round(body['nutrients']['calories']) in [1999, 2000, 2001]


@allure.epic('API. Meal planner')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Generating meal plan")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_generate_meal_plan_week():
    schema = load_schema('meal_plan_week.json')
    api_key = os.getenv('API_key')
    url = 'mealplanner/generate'
    params = {
        'apiKey': api_key,
        'timeFrame': 'week'
    }
    response = api_get(url, params=params)
    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert len(body['week']['monday']['meals']) == 3
    assert len(body['week']['tuesday']['meals']) == 3
    assert len(body['week']['wednesday']['meals']) == 3
    assert len(body['week']['thursday']['meals']) == 3
    assert len(body['week']['friday']['meals']) == 3
    assert len(body['week']['saturday']['meals']) == 3
    assert len(body['week']['sunday']['meals']) == 3
