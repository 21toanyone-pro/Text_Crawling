# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:55:48 2019

@author: VIP
"""

import requests
from bs4 import BeautifulSoup
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
req = requests.get('http://sillok.history.go.kr/popup/print.do?id=kaa_10107017_002&gubun=chn')

# HTML 소스 가져오기
html = req.text

# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')


old_word = soup.select(
    'cont_area > div.viewer_wrap > div.viewer_type.v_type06 > div.v_txt_wrap.v_txt_org > p'
)
#cont_area > div.viewer_wrap > div.viewer_type.v_type06 > div.v_txt_wrap.v_txt_org

word_moduel = soup.find('p',{'class':'paragraph'})

save = open('./text.txt', 'w', encoding='utf')
save.write(word_moduel.get_text().strip())

