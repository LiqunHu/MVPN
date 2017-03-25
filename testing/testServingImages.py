# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:25:02 2016

@author: huliqun
"""

import requests
import os

_SERVER_HOST = '127.0.0.1'
_SERVER_PORT = 8000
_SERVER_BASE_URL = 'http://{0}:{1}/images'.format(_SERVER_HOST, _SERVER_PORT)
headers = {'Authorization': '3161cc5a950fead158ebe803f7e56822',
           'Account-ID': '111111111111111',
           'content-type':'image/jpeg'}

#resp = requests.get(_SERVER_BASE_URL)
#resp = requests.post(_SERVER_BASE_URL, headers=headers,files=files)
resp = requests.post(_SERVER_BASE_URL, headers=headers,data=open('./test.jpg', 'rb'))
print(resp)
local = resp.headers.get('location')
print(local)

_FILE_URL = 'http://{0}:{1}{2}'.format(_SERVER_HOST, _SERVER_PORT, local)
resp = requests.get(_FILE_URL, headers=headers)
fp = open('11.jpg','wb')
fp.write(resp.content)
fp.close()