import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import config
from selene import browser
from spoonacular_test_project.helper import attach_web
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.base_url = 'https://www.chitai-gorod.ru'
    config.window_width = 1920
    config.window_height = 1080
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach_web.add_screenshot(browser)
    attach_web.add_logs(browser)
    attach_web.add_html(browser)
    attach_web.add_video(browser)

    browser.quit()
