#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Search result windows chrome
#И используем наши шаги.
  Given website "ru.aliexpress.com"
  When close pop up and wait "3" sec
  And fill in "iPhoneX"
  And press search
  Then check search result more than '0'
