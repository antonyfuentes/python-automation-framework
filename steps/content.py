from behave import *

from acceptance.page_model.base_page import BasePage
from acceptance.page_model.login_page import LoginPage

use_step_matcher('re')


@then('I should not see the cart and messages icons')
def step_impl(context):
    base_page = BasePage(context.driver)
    assert base_page.cart is None or not base_page.cart.is_displayed()


@step('I should see the cart and messages icons')
def step_impl(context):
    base_page = BasePage(context.driver)
    assert base_page.cart is not None and base_page.cart.is_displayed()


@step('I should see login invalid credentials error')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.invalid_credentials_error is not None and page.invalid_credentials_error.is_displayed()
