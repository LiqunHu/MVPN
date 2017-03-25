# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:07 2016

@author: huliqun
"""
import unittest

from falcon import testing

import sys
sys.path.append('..\\..')
from MainServer import app
from testing.common import auth
  
class TestCAPTCHATrans(testing.TestCase):  
  
    def setUp(self):  
        self.api = app
  
    def test_post_get_list(self):  
        
        headers = {'content-type':'application/json',
        'Authorization': auth.getAuthToken(self, '1','admin','admin')}
        body = '{}'
        result = self.simulate_post('/api/system/usercontrol',query_string='method=init', headers=headers,body=body) 
        print(result.json)
        self.assertEqual(result.status_code, 200) 

        result = self.simulate_post('/api/system/usercontrol',query_string='method=search', headers=headers,body=body) 
        print(result.json)
        self.assertEqual(result.status_code, 200)  
        
        body = '{"username":"111@qq.com","displayname":"wahaha","email":"1111@qq.com","mobile":"18698729476","usergroupid":"1"}'
        result = self.simulate_post('/api/system/usercontrol',query_string='method=add', headers=headers,body=body) 
        print(result.json)
        self.assertEqual(result.status_code, 200)  
        userid = result.json['data']['userid']
        
        body = '{"old":{"userid":"'+userid+'","username":"111@qq.com","displayname":"wahaha","email":"1111@qq.com","mobile":"18698729476","usergroupid":"1"},"new":{"userid":"'+userid+'","username":"111@qq.com","displayname":"wahahalulu","email":"1111@qq.com","mobile":"18698729476","usergroupid":"1"}}'
        result = self.simulate_post('/api/system/usercontrol',query_string='method=modify', headers=headers,body=body) 
        print(result.json)
        self.assertEqual(result.status_code, 200)  
        
        body = '{"userid":"'+userid+'","username":"111@qq.com","displayname":"wahahalulu","email":"1111@qq.com","mobile":"18698729476","usergroupid":"1"}'
        result = self.simulate_post('/api/system/usercontrol',query_string='method=delete', headers=headers,body=body) 
        print(result.json)
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':  
    unittest.main()        