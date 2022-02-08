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

MyJobsSignIn = driver.find_element_by_xpath(
    '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li/div[1]/div[2]/div[3]/a[1]').click()
time.sleep(5)

Id = driver.find_element_by_id(
    'TXTUSERNAME').send_keys("omarfaruq3110@gmail.com")
time.sleep(5)

Next = driver.find_element_by_xpath(
    '//*[@id="form1"]/div[2]/div/div[2]/div/div[2]/input').click()
time.sleep(5)

Pass = driver.find_element_by_id('TXTPASS').send_keys("o01676787008")
time.sleep(5)

sign_in = driver.find_element_by_xpath(
    '//*[@id="form1"]/div[2]/div/div[2]/div/div[2]/input').click()
time.sleep(15)

LiveJobs = driver.find_element_by_xpath(
    '//*[@id="main"]/div/div[1]/div/div[2]/a[1]/div/div').click()
time.sleep(5)
