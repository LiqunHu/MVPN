# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:25:02 2016

@author: huliqun
"""

import requests
import json
import uuid
import base64

_SERVER_HOST = '127.0.0.1'
_SERVER_PORT = 8000
_SERVER_BASE_URL = 'http://{0}:{1}/api/users'.format(_SERVER_HOST, _SERVER_PORT)

headers = {'content-type':'application/json'}
body = '{"username":"wahaha@qq.com","displayname":"wahaha","email":"wahaha@qq.com","password":"123456","mobile":"18698729476"}'
#resp = requests.get(_SERVER_BASE_URL)
resp = requests.post(_SERVER_BASE_URL, headers=headers,data=body)
print(resp.text)
print(resp)


headers = {'Authorization': '3161cc5a950fead158ebe803f7e56822',
           'Account-ID': '111111111111111',
           'content-type':'application/json'}
password = '123456'
#resp = requests.get(_SERVER_BASE_URL, headers=headers,data=body)
#print(resp.text)
#print(resp)

import pyDes
import hashlib
def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.digest()

# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
data = str(uuid.uuid4()).replace('-','')
k = pyDes.triple_des(md5('123456'), pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = base64.b64encode(k.encrypt(data)).decode()
idf = base64.b64encode(k.encrypt('wahaha@qq.com')).decode()
headers = {'content-type':'application/json'}
bodyData = {
        'username':'wahaha@qq.com',
        'identifyCode':idf
        }
print(idf)
body = json.dumps(bodyData)


print("Encrypted: %r" % idf)
print("Decrypted: %r" % k.decrypt(base64.b64decode(idf.encode())).decode() )

_SERVER_BASE_URL = 'http://{0}:{1}/api/auth'.format(_SERVER_HOST, _SERVER_PORT)
resp = requests.get(_SERVER_BASE_URL, headers=headers,data=body)
print(resp.text)
print(resp)

headers = {'Cookie':'awesession=c7f406241bcc49209eb58a527520e051-1465822334-fe92174a8e3956edc8befc20911a0b54c8f7b2db; Domain=aaaa.com;',
           'content-type':'application/json'}
_SERVER_BASE_URL = 'http://{0}:{1}/api/users'.format(_SERVER_HOST, _SERVER_PORT)
resp = requests.get(_SERVER_BASE_URL, headers=headers,data=body)
print(resp.text)
print(resp)
