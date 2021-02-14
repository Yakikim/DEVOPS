from selenium import webdriver

# Windows:
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("https://translate.google.co.il/")
#driver.implicitly_wait(15)
#web_element = driver.find_element_by_class_name("mqNsCe tQlvad")

web_element = driver.find_element_by_link_text("היסטוריה").send_keys(Keys.ENTER)
if web_element.is_enabled():
    web_element.click()

print(driver)