# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:51:58 2016

@author: huliqun
"""

DEBUG = False
dbEchoFlag = False

# SECURITY WARNING: keep the secret key used in production secret!
COOKIE_NAME = 'awesession'
SECRET_KEY = 'zc7#_66#g%u2n$j_)j$-r(swt63d(2l%wc2y=wqt_m8kpy%04*'
TOKEN_AGE = 86400
DOMAIN = ''


log_file = '/logs/serverlog'
files_storage_path = '/webfiles/static/images'
temp_path = '/webfiles/temp'
#log_file = '/Users/huliqun/Work/VFND/servdata/logs/serverlog'
#files_storage_path = '/Users/huliqun/Work/VFND/static/static/files'
#temp_path = '/Users/huliqun/Work/VFND/static/temp'



tmp_url_base = '/temp/'
images_url_base = '/static/files/'

dbUrl='mysql+pymysql://root:123456@testsql:3306/test?charset=utf8'
#dbUrl='mysql+pymysql://test:test@localhost:3306/test?charset=utf8'

#spyder config
spyderErrorTimes = 2
spyderTimeout = 3
spyderDelayTime = 2
