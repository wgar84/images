# %%
from selenium import webdriver

# %%
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# %%

# %%
driver = webdriver.Remote("http://driver:4444/wd/hub", options=chrome_options)
print('connected to driver')

# %%

# %%
driver.get('www.google.com')
screenshot = driver.save_screenshot('code/test.png')

# %%
driver.quit()