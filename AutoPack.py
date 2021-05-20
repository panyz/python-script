from selenium import webdriver
from time import sleep
import sys

browser = webdriver.Chrome()
browser.get('xxxxx')

username = browser.find_element_by_id('j_username')
username.send_keys('xxx')
pwd = browser.find_element_by_name('j_password')
pwd.send_keys('xxx')
btn = browser.find_element_by_name('Submit')
btn.submit()

link = browser.find_element_by_link_text('android_dev_MiniPos')
link.click()

link = browser.find_element_by_link_text('Build with Parameters')
link.click()

sleep(5)
branchname = '//option[text()="origin/feature_%s"]' % sys.argv[1]
branch = browser.find_element_by_xpath(branchname)
branch.click()

checkboxelems = browser.find_elements_by_xpath('//input[@name="value"]')
checkboxelems[1].click()

button = browser.find_element_by_id('yui-gen1-button')
button.submit()