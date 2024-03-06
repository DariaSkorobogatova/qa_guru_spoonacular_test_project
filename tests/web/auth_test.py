import os
import allure
from spoonacular_test_project.data.users import User
from spoonacular_test_project.pages.web_pages.main_page import main


@allure.epic('authorisation')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Checking successful authorization')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_successful_authorisation():
    user = User(
        login=os.getenv('USER_LOGIN'),
        email=os.getenv('USER_EMAIL'),
        password=os.getenv('USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main.open()

    with allure.step("Click start now"):
        main.click_start_now()

    with allure.step("Fill the authorization form"):
        main.fill_authorization_form(user)

    with allure.step("Check that user has been authorized"):
        main.assert_successful_authorisation(user)


@allure.epic('authorisation')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Checking unsuccessful authorization')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_unsuccessful_authorisation():
    user = User(
        login=os.getenv('UNREGISTERED_USER_LOGIN'),
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main.open()

    with allure.step("Click start now"):
        main.click_start_now()

    with allure.step("Fill the authorization form"):
        main.fill_authorization_form(user)

    with allure.step("Check that user has not been authorized"):
        main.assert_unsuccessful_authorisation()
