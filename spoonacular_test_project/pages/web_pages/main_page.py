from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("")
        return self

    def click_start_now(self):
        browser.element('#startNowButton').should(be.visible).click()
        return self

    def fill_authorization_form(self, user):
        browser.element('#signIn').should(be.visible)
        browser.element('[name="email"]').should(be.visible).type(user.email)
        browser.element('[name="password"]').should(be.visible).type(user.password)
        browser.element('form button').click()
        return self

    def assert_successful_authorisation(self, user):
        browser.element('.lightGrey #tagLine').should(have.text(user.login))
        return self

    def assert_unsuccessful_authorisation(self):
        browser.element('#signInError').should(have.text('Sorry, the login information was incorrect.'))
        return self

    def log_in(self, user):
        self.open()
        self.click_start_now()
        self.fill_authorization_form(user)

    def assert_main_title_text(self, text):
        browser.element('div h1').should(have.text(text))
        return self

    def click_circle(self, text):
        browser.element(f'//a[contains(text(), "{text}")]').click()
        return self

    def assert_link(self, url):
        assert url in browser.driver.current_url
        return self

    def click_sign_up(self):
        browser.element('form button').should(be.visible)
        browser.element('[href="/registerEmail"]').should(be.visible).click()
        return self

    def go_to_register_page(self):
        browser.open("registerEmail")
        return self

    def go_to_reset_password_page(self):
        browser.open("forgotPassword")
        return self


main = MainPage()
