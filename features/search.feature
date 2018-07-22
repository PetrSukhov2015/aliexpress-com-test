Feature: Checking search

Scenario: Search result windows chrome
  Given website "ru.aliexpress.com"
  When close pop up and wait "3" sec
  And fill in "iPhoneX"
  And press search
  Then check search result more than '0'

Scenario: Search result android
  Given android
  When android app fill in "iPhoneX"
  And android press search
  Then android check search result
