from selenium.webdriver.common.by import By


class BasePageLocators:
    # TITLE
    TITLE = By.CSS_SELECTOR, "a.navbar-brand h3"

    # NAV LINKS
    NAV_LINKS = By.CSS_SELECTOR, "header nav .navbar-right"

    # nav bar options
    HOME = By.CSS_SELECTOR, "li a[href='/']"
    COURSES = By.CSS_SELECTOR, "li a[href^='/products/list/']"
    LOGIN = By.CSS_SELECTOR, "li a[href='/login/']"
    CART = By.CSS_SELECTOR, "li a[href='/cart/']"
    MESSAGES = By.CSS_SELECTOR, "li a[href='/messages/']"
