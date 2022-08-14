from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("disable-gpu")
    if os.getenv("HEADLESS") == 'true':
      options.add_argument("headless")

    context.browser = webdriver.Chrome(options=options)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()
