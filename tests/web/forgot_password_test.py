import os
import allure
from spoonacular_test_project.pages.web_pages.main_page import main
from spoonacular_test_project.pages.web_pages.forgot_password_page import forgot_password


@allure.epic('reset password')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Sending reset link')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_reset_link_sent_success_alert_message():
    email = os.getenv('USER_EMAIL')

    with allure.step("Open the forgot password page"):
        main.go_to_reset_password_page()

    with allure.step("Enter registered user email"):
        forgot_password.enter_email(email)
        forgot_password.click_send_button()

    with allure.step("Assert success alert message appeared"):
        forgot_password.assert_success_alert_message('The password reset request has been sent.')


@allure.epic('reset password')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Entering unregisted email')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_unregisted_email_alert_message():
    email = os.getenv('UNREGISTERED_USER_EMAIL')

    with allure.step("Open the forgot password page"):
        main.go_to_reset_password_page()

    with allure.step("Enter unregistered user email"):
        forgot_password.enter_email(email)

    with allure.step("Assert failure alert message appeared"):
        forgot_password.assert_failure_alert_message('This email is not connected to a spoonacular account.')


@allure.epic('reset password')
@allure.label('owner', 'daria_skorobogatova')
@allure.feature('Entering invalid email')
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_invalid_email_alert_message():
    email = 'testGJR273gmail.com'

    with allure.step("Open the forgot password page"):
        main.go_to_reset_password_page()

    with allure.step("Enter invalid email"):
        forgot_password.enter_email(email)

    with allure.step("Assert failure alert message appeared"):
        forgot_password.assert_failure_alert_message('Invalid email')
