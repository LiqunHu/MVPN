# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:07 2016

@author: huliqun
"""
import unittest
import json
from falcon import testing

from MainServer import app
  
class TestCAPTCHATrans(testing.TestCase):  
  
    def setUp(self):  
        self.api = app
  
    def test_CAPTCHATrans(self):  
        headers = {'content-type':'image/png'}
        with open('D://111.png', 'rb') as testFile:
#        with open('/home/pwork/workserver/testing/TestCAPTCHA.png', 'rb') as testFile:
#            print(io.BytesIO(testFile.read()).getbuffer().nbytes)
            
            result = self.simulate_post('/api/commontools/captchatrans',headers=headers,body=testFile.read() )
#            result = self.simulate_request('POST', path='/api/commontools/captchatrans',headers=headers,body=testFile.read() )
            self.assertEqual(result.status_code, 200)
            resultJson = json.loads(result.text)
            self.assertEqual(resultJson['data']['codeString'], "1906")  