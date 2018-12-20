from behave import *
from selenium import webdriver

from acceptance.page_model.login_page import LoginPage

use_step_matcher('re')


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = LoginPage(context.driver)
    context.driver.get(page.url)
