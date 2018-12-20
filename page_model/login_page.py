from acceptance.locators.login_page_locators import LoginPageLocators
from acceptance.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        return super(LoginPage, self).url + '/login/'

    @property
    def email_field(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL)

    @property
    def password_field(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    @property
    def login_button_field(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def invalid_credentials_error(self):
        try:
            return self.driver.find_element(*LoginPageLocators.LOGIN_ERROR_INVALID_CREDENTIALS)
        except:
            return None
