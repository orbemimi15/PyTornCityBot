from selenium import webdriver
import time
import random

# Create a new instance of the Chrome driver
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

# go to the torn city home page
driver.get("http://www.torn.com")

#Login
time.sleep(random.uniform(1,3))

username1 = driver.find_element_by_id("player")
username1.send_keys("EMAIL")

password1 = driver.find_element_by_id("password")
password1.send_keys("PASSWORD")
password1.submit()
time.sleep(random.uniform(1,3))

#Deposit money
driver.get("http://www.torn.com/properties.php#/p=options&tab=vault")
#vault = driver.find_element_by_id("icon32").click()
time.sleep(random.uniform(1,3))

#Scroll down to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

vaultsubmit1 = driver.find_element_by_xpath('//*[@id="properties-page-wrap"]/div[3]/div[8]/div[3]/form[2]/div[2]/span/span/input')
vaultsubmit1.click()

time.sleep(random.uniform(1,3))
#Do Gym
""" gym1 = driver.find_element_by_xpath('//*[@id="nav-gym"]/a').click()
recaptchaA = driver.find_element_by_xpath('//*[@id="ui-id-2"]/span').click()
recaptchaB = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]').click()
"""

#Logout
logout1 = driver.find_element_by_class_name("logout").click()
time.sleep(random.uniform(1,3))

driver.quit()
