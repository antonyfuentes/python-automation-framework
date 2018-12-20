from behave import *

from acceptance.page_model.login_page import LoginPage

use_step_matcher('re')


@when('I login as user "(.*)" and password "(.*)"')
def step_impl(context, username, password):
    login_page = LoginPage(context.driver)
    login_page.email_field.send_keys(username)
    login_page.password_field.send_keys(password)
    login_page.login_button_field.click()
