from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id("cookies")


actions = ActionChains(driver)
actions.click(cookie)

for x in range(5000):
    actions.perform()
