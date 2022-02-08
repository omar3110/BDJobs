from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import sys
import time


driver = webdriver.Chrome("chromedriver")
driver.get("https://www.bdjobs.com/")
time.sleep(5)

SignIn = driver.find_element_by_class_name("mh").click()
time.sleep(5)

EmployersSignIn = driver.find_element_by_xpath(
    '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li/div[2]/div[2]/div[3]/a[1]').click()
time.sleep(5)

UserName = driver.find_element_by_id(
    'NAME').send_keys("omarfaruq3110@gmail.com")
time.sleep(5)

Password = driver.find_element_by_id(
    'PASS').send_keys("o01676787008")
time.sleep(5)

SignIn = driver.find_element_by_id('sighIn').click()
time.sleep(5)
