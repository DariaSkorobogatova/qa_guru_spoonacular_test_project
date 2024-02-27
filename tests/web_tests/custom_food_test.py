import os
import allure
from spoonacular_test_project.data.users import User
from spoonacular_test_project.pages.web_pages.main_page import main
from spoonacular_test_project.pages.web_pages.user_profile_page import profile


@allure.epic('profile settings')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Adding custom food")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_custom_food(value='pasta'):
    user = User(
        login=os.getenv('USER_LOGIN'),
        email=os.getenv('USER_EMAIL'),
        password=os.getenv('USER_PASSWORD')
    )
    with allure.step("Log in"):
        main.log_in(user)

    with allure.step("Add custom food"):
        profile.click_custom_food_tab()
        profile.add_new_custom_food(value)

    with allure.step("Check that custom food was added"):
        profile.assert_custom_food_was_added(value)

    with allure.step("Delete custom food"):
        profile.delete_custom_food()



