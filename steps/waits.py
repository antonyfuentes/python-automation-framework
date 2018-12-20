from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@given('I wait for navbar')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BasePage.navigation)
    )
