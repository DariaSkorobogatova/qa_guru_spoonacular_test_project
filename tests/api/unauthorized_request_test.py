import allure
import jsonschema
from spoonacular_test_project.helper.load_schema import load_schema
from spoonacular_test_project.helper.api_requests import api_get


@allure.epic('API. Unauthorized request')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Unauthorized request restricted')
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unauthorized_request():
    schema = load_schema('unauthorized_request.json')
    url = 'food/ingredients/search'
    response = api_get(url)
    assert response.status_code == 401
    jsonschema.validate(response.json(), schema)
    assert response.json()[
               'message'] == 'You are not authorized. Please read https://spoonacular.com/food-api/docs#Authentication'


@allure.epic('API. Unauthorized request')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Sending non-existing key')
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_request_with_non_existing_key():
    schema = load_schema('unauthorized_request.json')
    api_key = '101239sdhwo3923hd328h382f'
    url = f'food/ingredients/search'
    params = {
        'apiKey': api_key,
        'query': 'ice cream',
        'number': 1
    }
    response = api_get(url, params=params)
    assert response.status_code == 401
    jsonschema.validate(response.json(), schema)
    assert response.json()[
               'message'] == 'You are not authorized. Please read https://spoonacular.com/food-api/docs#Authentication'
