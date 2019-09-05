# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:06:27 2019

@author: DUSK
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome('C:\\chromedriver.exe') #위치

driver.implicitly_wait(2) # 로딩 시간

driver.get('http://sillok.history.go.kr/id/kaa_000001') #조선왕조실록 첫 페이지



driver.find_element_by_xpath('//*[@id="cont_area"]/div[1]/ul[2]/li[2]/a').click()