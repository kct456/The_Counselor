from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests
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
base_url = 'https://pathwaysguide.universityofcalifornia.edu/college-pathways/'
videos_url = 'https://pathwaysguide.universityofcalifornia.edu/college-pathways/Berkeley%20City%20College/Computer%20Science'

# Firefox session
driver = webdriver.Firefox(capabilities=cap,firefox_options=options,executable_path='C:\\Users\\kevin\\OneDrive\\Desktop\\TreeHacks\\The_Counselor\\geckodriver.exe')
driver.get(videos_url)
driver.implicitly_wait(100)

# First element of list is empty string (what do we want to do about this?)
collegeSelect = Select(driver.find_element_by_id('collegeSelect'))
collegeOptions = collegeSelect.options
pathwaySelect = Select(driver.find_element_by_id('pathwaySelect'))
pathwayOptions = pathwaySelect.options

#driver.quit()

# BeautifulSoup stuff
'''
col = collegeOptions[1].get_attribute('value')
path = pathwayOptions[8].get_attribute('value')

colTransform = ''.join([x.replace(' ','%20') for x in col])
pathTransform = ''.join([x.replace(' ','%20') for x in path])

url = base_url + colTransform + '/' + pathTransform

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

print(len(soup.find_all('b')))
'''
'''
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 52.0) Gecko/20100101 Firefo/52.0'})

col = collegeOptions[1].get_attribute('value')
path = pathwayOptions[8].get_attribute('value')

colTransform = ''.join([x.replace(' ','%20') for x in col])
pathTransform = ''.join([x.replace(' ','%20') for x in path])

url = base_url + colTransform + '/' + pathTransform

driver.get(url)
driver.implicitly_wait(100)
page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
meep = soup.findAll('b')
print(url)
print(meep)
'''
'''
for college in collegeOptions:
    print(college.get_attribute('value'))

for pathway in pathwayOptions:
    print(pathway.get_attribute('value'))
'''


'''
cLen = len(collegeOptions)
pLen = len(pathwayOptions)
partialBitMap = [[0 for y in range(cLen)] for x in range(pLen)]
exceptionList = []
'''
'''
for i in range(1,cLen):
    for j in range(1,pLen):
        collegeVal = collegeOptions[i].get_attribute('value')
        pathwayVal = pathwayOptions[j].get_attribute('value')
        collegeSelect.select_by_value(collegeVal)
        pathwaySelect.select_by_value(pathwayVal)
        driver.implicitly_wait(10000)
        elem = driver.find_element_by_class_name('col-md-12')
        driver.implicitly_wait(10000)
        try:
            text = elem.text
        except:
            print('Exception occurs')
            exceptionList.append((i,j))
        driver.implicitly_wait(10000)
        if(len(text) >= 3 and text[:4] == 'THIS'):
            partialBitMap[i][j] = 1
            print(text[:4])
    print(partialBitMap[i])
'''
'''
for college in collegeOptions:
    for pathway in pathwayOptions:
        collegeVal = college.get_attribute('value')
        pathwayVal = pathway.get_attribute('value')
        collegeSelect.select_by_value(collegeVal)
        pathwaySelect.select_by_value(pathwayVal)
        driver.implicitly_wait(10000)
        #elem = driver.find_element_by_class_name('body > app-root > div:nth-child(2) > div > college-pathways > div > div > div > div.pathways-results > div > div.panel.panel-info > div > div.resultsgrid > div.row.pathway-header > div > h4')
        
        elem = driver.find_element_by_xpath('/html/body/app-root/div[2]/div/college-pathways/div/div/div/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[1]/b')
        try:
            print(elem.text)
        except:
            continue
        driver.implicitly_wait(10000)
        print(collegeVal,pathwayVal)
        print('-----------------------------------------')
'''
cLen = len(collegeOptions)
pLen = len(pathwayOptions)
for i in range(1,cLen):
    collegeVal = collegeOptions[i].get_attribute('value')
    collegeSelect.select_by_value(collegeVal)
    for j in range(1,pLen):
        pathwayVal = pathwayOptions[j].get_attribute('value')
        pathwaySelect.select_by_value(pathwayVal)
        try:
            elem = driver.find_element_by_xpath('/html/body/app-root/div[2]/div/college-pathways/div/div/div/div[4]/div/div[1]/div/div[1]/div[3]/div[3]/div[1]')
            print(elem.text)
            elem = driver.find_element_by_xpath('/html/body/app-root/div[2]/div/college-pathways/div/div/div/div[4]/div/div[1]/div/div[1]/div[4]/div[1]')
            print(elem.text)
        except:
            continue
        print(collegeVal,pathwayVal)
        print('-----------------------------------------')

print('MOOP')
driver.quit()