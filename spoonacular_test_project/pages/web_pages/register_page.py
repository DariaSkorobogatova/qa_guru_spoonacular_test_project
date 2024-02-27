import random
from selene import browser, be, have
import time
from selenium.webdriver.common.by import By


class RegisterPage:
    def fill_register_form(self, user):
        browser.element('#firstname').should(be.visible).type(user.login)
        browser.element('#email').should(be.visible).type(user.email)
        browser.element('#username').should(be.visible).type(user.login)
        browser.element('#password').should(be.visible).type(user.password)
        return self

    def click_agree_policy_checkbox(self):
        browser.element('[for="agreeTermsBox"]').should(be.visible).click()
        browser.element('#firstnameStatus').should(have.text('Great'))
        browser.element('#emailStatus').should(have.text('Great'))
        browser.element('#usernameStatus').should(have.text('free'))
        browser.element('#passwordStatus').should(have.text('Great'))
        return self

    def delay(self):
        time.sleep(random.randint(2, 3))

    def click_captcha(self):
        frames = browser.driver.find_elements(By.TAG_NAME, 'iframe')
        browser.driver.switch_to.frame(frames[0])
        self.delay()
        browser.element('.recaptcha-checkbox-border').click()
        return self

    def assert_image_select_block(self):
        browser.driver.switch_to.default_content()
        frames = browser.driver.find_element(By.XPATH, '/html/body/div[8]/div[4]').find_elements(By.TAG_NAME, 'iframe')
        browser.driver.switch_to.frame(frames[0])
        self.delay()
        browser.element('#recaptcha-verify-button').should(be.visible)
        return self

    def click_sign_up_button(self):
        browser.element('#doneButton').should(be.visible).click()
        return self

    def assert_alert_message(self):
        browser.element('.alert-box').should(be.visible)
        return self


register = RegisterPage()
