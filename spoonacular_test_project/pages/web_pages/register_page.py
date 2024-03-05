from selene import browser, be, have


class RegisterPage:
    def fill_register_form(self, user):
        browser.element('#firstname').should(be.visible).type(user.login)
        browser.element('#email').should(be.visible).type(user.email)
        browser.element('#username').should(be.visible).type(user.login[:5])
        browser.element('#username').should(be.visible).type(user.login[5:])
        browser.element('#password').should(be.visible).type(user.password)
        return self

    def click_agree_policy_checkbox(self):
        browser.element('[for="agreeTermsBox"]').should(be.visible).click()
        browser.element('#firstnameStatus').should(have.text('Great'))
        browser.element('#emailStatus').should(have.text('Great'))
        browser.element('#usernameStatus').should(have.text('free'))
        browser.element('#passwordStatus').should(have.text('Great'))
        return self

    def click_sign_up_button(self):
        browser.element('#doneButton').should(be.visible).click()
        return self

    def assert_alert_message(self):
        browser.element('.alert-box').should(be.visible)
        return self


register = RegisterPage()
