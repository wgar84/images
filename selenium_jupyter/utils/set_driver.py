# %%
from selenium import webdriver


def set_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')  # example
    options.add_argument("window-size=1400,600")
    driver = webdriver.Remote("http://driver:4444/wd/hub", options=options)
    driver.maximize_window()
    return driver