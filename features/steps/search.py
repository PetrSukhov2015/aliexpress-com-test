# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from features.pages.search_page import SearchPage, SearchPageAndroid


@given('website "{url}"')
def step(context, url):
    chrome_options = webdriver.ChromeOptions()
    context.browser = webdriver.Chrome(executable_path='D:\\work\\testing\\auto.ru\\chromedriver.exe')
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)
    context.page = SearchPage(context.browser)
    context.page.open("http://" +url)

@when('close pop up and wait "{s}" sec')
def step (context, s):
    context.page.close_pop_up()
    context.page.wait(int(s))


@when('fill in "{request}"')
def step(context,request):
    context.page.fill(request)

@when('press search')
def step(context):
    context.page.search()


@then ('check search result more than "{num}"')
def step(context,num):
    context.page.check_result_more_than(num)


@given ('android')
def step(context):
    #caps
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Alcatel One Touch'
    desired_caps['app'] = 'D:/aliexpress-com-test/features/ali.apk'
    desired_caps['appPackage'] = 'com.alibaba.aliexpresshd'
    desired_caps['appActivity'] = 'com.aliexpress.module.home.MainActivity'  # 'com.alibaba.aliexpresshd.'
    #driver
    context.a_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.a_driver.implicitly_wait(120)
    #page
    context.a_page = SearchPageAndroid(context.a_driver)




@when('android app fill in "{a_request}"')
def step(context,a_request):
    context.a_page.a_fill(a_request)

@when('android press search')
def step(context):
    context.a_page.a_search()

@then('android check search result')
def step(context):
    context.a_page.a_check_result()


