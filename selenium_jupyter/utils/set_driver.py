# %%
from selenium import webdriver


def set_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # example
    driver = webdriver.Remote("http://driver:4444/wd/hub", options=options)
    return driver