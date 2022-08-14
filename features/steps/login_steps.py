from behave import *
from selenium.webdriver.common.by import By

@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("http://automationpractice.com/index.php")
    assert(context.browser.title) == "My Store"

@when(u'I click Sign in')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "a.login").click()
    assert(context.browser.find_element(By.CSS_SELECTOR, "h1.page-heading").text) == "AUTHENTICATION"

@when(u'I fill my credential')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("dtechover@example.com")
    context.browser.find_element(By.ID, "passwd").send_keys("Test1234")
    context.browser.find_element(By.ID, "SubmitLogin").click()

@then(u'I should be logged in')
def step_impl(context):
    assert(context.browser.find_element(By.CSS_SELECTOR, "h1.page-heading").text) == "MY ACCOUNT"

@when(u'I fill wrong email')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("dtechover@test.com")
    context.browser.find_element(By.ID, "passwd").send_keys("Test1234")
    context.browser.find_element(By.ID, "SubmitLogin").click()

@then(u'I should not be logged in')
def step_impl(context):
    assert(context.browser.find_element(By.CSS_SELECTOR, "h1.page-heading").text) == "AUTHENTICATION"

@then(u'I should see the error message')
def step_impl(context):
    assert(context.browser.find_element(By.CSS_SELECTOR, "div.alert-danger").text) == "There is 1 error\nAuthentication failed."