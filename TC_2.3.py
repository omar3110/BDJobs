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


google = driver.find_element_by_id('gplus_button').click()
time.sleep(5)
driver.get('https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttps%2Fmybdjobs.bdjobs.com%3Fid%3Dauth208618&response_type=permission%20id_token&scope=profile%20email&openid.realm&include_granted_scopes=true&client_id=656340698751-kt8lk3hujr2grfo7rnjmddb85rmg1c2q.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fmybdjobs.bdjobs.com&fetch_basic_profile=false&gsiwebsdk=2&flowName=GeneralOAuthFlow')
time.sleep(5)
gmail = driver.find_element_by_id('identifierId').send_keys(
    'mdomarfaruq.generalmail@gmail.com')
time.sleep(5)

Next = driver.find_element_by_xpath(
    '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(5)
