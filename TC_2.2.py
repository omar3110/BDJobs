from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import sys
import time
# import pytest
# # import allure


driver = webdriver.Chrome("chromedriver")
driver.get("https://www.bdjobs.com/")
time.sleep(5)

SignIn = driver.find_element_by_class_name("mh").click()
time.sleep(5)

MyJobsSignIn = driver.find_element_by_xpath(
    '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li/div[1]/div[2]/div[3]/a[1]').click()
time.sleep(5)


fb = driver.find_element_by_id('fb_button').click()
time.sleep(5)
