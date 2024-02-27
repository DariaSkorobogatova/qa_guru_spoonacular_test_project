import allure
from spoonacular_test_project.pages.web_pages.main_page import main
import pytest

titles_and_urls = [
        ['Save and organize recipes from any site', 'articles/how-to-use-the-spoonacular-recipe-saver-and-recipe-bookmarklet'],
        ['Free meal planner and food tracker', 'meal-planner'],
        ['Collect your favorite products', 'high-protein-organic-granola-bar']
]


@allure.epic('main page header')
@allure.label("owner", "daria_skorobogatova")
@allure.feature("Checking the titles and urls")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_check_main_title():
    with allure.step("Open the main page"):
        main.open()

    with allure.step("Check title"):
        main.assert_main_title_text('All Your Food. One Place.')


@pytest.mark.parametrize('title, url', titles_and_urls)
def test_recipe_circle(title, url):
    with allure.step("Open the main page"):
        main.open()

    with allure.step("Check urls"):
        main.click_circle(title)
        main.assert_link(url)
