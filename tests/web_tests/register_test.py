import os
import allure
from spoonacular_test_project.data.users import User
from spoonacular_test_project.pages.web_pages.main_page import main
from spoonacular_test_project.pages.web_pages.register_page import register


@allure.epic('registration')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Checking unsuccessful registration without captcha')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_unsuccessful_registration_without_captcha():

    user = User(
        login=os.getenv('UNREGISTERED_USER_LOGIN'),
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    with allure.step("Open the registration page"):
        main.go_to_register_page()

    with allure.step("Fill register form"):
        register.fill_register_form(user)

    with allure.step("Agree to site policy"):
        register.click_agree_policy_checkbox()

    with allure.step("Click sign up button"):
        register.click_sign_up_button()

    with allure.step("Check that alert message appeared"):
        register.assert_alert_message()


