from selene import browser, be, have


class UserProfilePage:
    def click_custom_food_tab(self):
        browser.element('//li/a[contains(text(), "Custom Foods")]').should(be.visible).click()
        return self

    def add_new_custom_food(self, value):
        browser.element('[class="alert-box warning"] a').should(be.visible).click()
        browser.element('input#fTitle').should(be.blank).type(value)
        browser.element('#fAddCustomFood #imageSuggestion').should(be.visible)
        browser.element('//div[contains(text(), "Save the Custom Food")]').should(be.visible).click()
        browser.element('div[class="jquery-notify-bar success top"]').should(be.visible)
        return self

    def assert_custom_food_was_added(self, value):
        self.click_custom_food_tab()
        browser.driver.refresh()
        browser.element('.customFoodBoxId-0 h4 a').should(have.text(value))
        return self

    def delete_custom_food(self):
        browser.element('.optionGroup+a').should(be.visible).click()
        browser.element('//div[contains(text(), "Delete the Custom Food")]').should(be.visible).click()
        browser.driver.switch_to.alert.accept()
        return self


profile = UserProfilePage()
