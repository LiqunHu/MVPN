# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:07 2016

@author: huliqun
"""
import unittest
import json
import binascii
from falcon import testing

import sys
sys.path.append('..')
from workserver.util.AES_PKCS7_extension import Cryptor
from MainServer import app

class TestAuth(testing.TestCase):  
  
    def setUp(self):  
        self.api = app
  
#    def test_regUser(self):  
#        headers = {'content-type':'application/json'}
#        body = '{"username":"wahaha@qq.com","displayname":"wahaha","email":"wahaha@qq.com","password":"123456","mobile":"18698729476"}'
#        result =self.simulate_post('/api/users',headers=headers,body=body ) 
#        self.assertEqual(result.status_code, 201)  
    
    def test_auth(self):
        
        import hashlib
        def md5(s):
            m = hashlib.md5()
            m.update(s.encode("utf-8"))
            return m.hexdigest()
        
#        print("pwd : %s" % md5('123456'))
        iv, encrypted = Cryptor.encrypt('aaa', md5('12345678'))
        print(md5('12345678'))
#        print("iv : %s" % iv.decode())
#        print("encrypted : %s" % binascii.b2a_base64(encrypted).rstrip())
        print(Cryptor.decrypt(encrypted,md5('12345678'), iv))
#        headers = {'content-type':'application/json'}
#        body = {
#                'oid': 2,
#                'username':'admin',
#                'identifyCode':encrypted,
#                'magicNo':iv.decode()
#                }
#        result =self.simulate_post('/api/auth',headers=headers,body=json.dumps(body) ) 
#        self.assertEqual(result.status_code, 200)
#        print(result.text)
        # should raise an exception for an immutable sequence  
#        self.assertRaises(TypeError, random.shuffle, (1,2,3))  

if __name__ == '__main__':  
    unittest.main()        