# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:07 2016

@author: huliqun
"""
import json
import binascii
from falcon import testing

from workserver.util.AES_PKCS7_extension import Cryptor
        
import hashlib
def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()
    
def getAuthToken(obj, oid ,username, password):   
#        print("pwd : %s" % md5('123456'))
    iv, encrypted = Cryptor.encrypt(username, md5(password))
#        print("iv : %s" % iv.decode())
#        print("encrypted : %s" % binascii.b2a_base64(encrypted).rstrip())
    headers = {'content-type':'application/json'}
    body = {
            'oid': oid,
            'username':username,
            'identifyCode':encrypted,
            'magicNo':iv.decode()
            }
    result = obj.simulate_post('/api/auth',headers=headers,body=json.dumps(body) ) 
    if result.status_code != 200:
        return None
        
    return result.headers['Authorization']
        # should raise an exception for an immutable sequence  
#        self.assertRaises(TypeError, random.shuffle, (1,2,3))  
