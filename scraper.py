from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import re
import os

# Capabilities
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
options = Options()
options.set_headless(headless=True)
options.binary = binary

cap = DesiredCapabilities().FIREFOX
cap['marionette'] = True

# Website urls
base_url = 'https://pathwaysguide.universityofcalifornia.edu'
videos_url = 'https://pathwaysguide.universityofcalifornia.edu/college-pathways/Berkeley%20City%20College/Computer%20Science'

# Google chrome session
driver = webdriver.Firefox(capabilities=cap,firefox_options=options,executable_path='C:\\Users\\kevin\\OneDrive\\Desktop\\TreeHacks\\The_Counselor\\geckodriver.exe')
driver.get(videos_url)
driver.implicitly_wait(100)

# First element of list is empty string (what do we want to do about this?)
collegeSelect = Select(driver.find_element_by_id('collegeSelect'))
collegeOptions = collegeSelect.options
for college in collegeOptions:
    print(college.get_attribute('value'))

print()

pathwaySelect = Select(driver.find_element_by_id('pathwaySelect'))
pathwayOptions = pathwaySelect.options
for pathway in pathwayOptions:
    print(pathway.get_attribute('value'))


#driver.get('https://google.com/')
#print('MEEP')
driver.quit()