#1, 2

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )
driver.get("http://www.walla.co.il")
ws_title = driver.title
driver.refresh()
print(ws_title)
print(driver.title)

#3
# Yes its same

#4

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )
driver.get("https://translate.google.com/")
driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").send_keys("תרגם אותי")
driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/button").click()
driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[1]/div/div[2]/input").send_keys("Hebrew")
driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

#5

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )
driver.get("https://www.youtube.com")
driver.find_element_by_xpath('//input[@id="search"]').send_keys("sultans of swing")
driver.find_element_by_xpath('//input[@id="search"]').send_keys(Keys.ENTER)

#6
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )

driver.get("https://translate.google.com/")
web_element = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").location
print(web_element)
web_element = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/button").parent
print(web_element)
web_element = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[1]/div/div[2]/input").tag_name
print(web_element)

#7
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )

driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("yakikim@gmail.com")
driver.find_element_by_id("pass").send_keys("********")
driver.find_element_by_id("u_0_b").click()
driver.close()

#chllenge
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="geckodriver.exe"
                           )
print(driver.get_cookies())
for i in driver.get_cookies():
    print(i)
driver.delete_all_cookies()
driver.close()
