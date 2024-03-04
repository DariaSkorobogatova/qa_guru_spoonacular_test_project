from selene import browser, be, have


class ForgotPasswordPage:
    def enter_email(self, email):
        browser.element('#email').should(be.visible).type(email)
        return self

    def click_send_button(self):
        browser.element('#doneButton').should(be.enabled).click()

    def assert_success_alert_message(self, text):
        browser.element('[class="alert-box success"]').should(have.text(text))
        return self

    def assert_failure_alert_message(self, text):
        browser.element('#emailStatus').should(have.text(text))
        return self


forgot_password = ForgotPasswordPage()