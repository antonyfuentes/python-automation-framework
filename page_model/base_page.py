from acceptance.locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:8000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def home(self):
        return self.driver.find_element(*BasePageLocators.NAV_LINKS).find_element(*BasePageLocators.HOME)

    @property
    def login(self):
        return self.driver.find_element(*BasePageLocators.NAV_LINKS).find_element(*BasePageLocators.LOGIN)

    @property
    def cart(self):
        try:
            return self.driver.find_element(*BasePageLocators.CART)
        except:
            return None

    @property
    def messages(self):
        return self.driver.find_element(*BasePageLocators.MESSAGES)
