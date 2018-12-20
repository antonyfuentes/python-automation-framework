from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = By.CSS_SELECTOR, "[name='email']"
    PASSWORD = By.CSS_SELECTOR, "[name='password']"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#main_container_wrapper button[type='submit']"
    LOGIN_ERROR_INVALID_CREDENTIALS = By.XPATH, "//li[text()='Credenciales inválidas']"
