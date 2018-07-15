# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from features.pages.search_page import SearchPage


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

