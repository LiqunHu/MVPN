# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:53:36 2016

@author: Administrator
"""

import logging

import sys
sys.path.append('..')
from workserver.util import LogUtil
from workserver.util import SysUtil
from workserver.util.preplanQuery import preplanQuery

LogUtil.initLog()
SysUtil.global_init()
logger = logging.getLogger('serverLog')
engine = SysUtil.get_engine_handle()
db = SysUtil.get_db_handle()
session = db()

print(preplanQuery(logger, session).preplanQuery('APL',{'billLodingNo': 'APLU069536629'}))
#print(preplanQuery(logger, session).preplanQuery('2',{'billLodingNo': 'SHA16710907601'}))
#print(preplanQuery(logger, session).preplanQuery('3',{'billLodingNo': 'SNL6SHJL31B3030'}))
#print(preplanQuery(logger, session).preplanQuery('9',{'billLodingNo': 'APLU069538226'}))
#print(preplanQuery(logger, session).preplanQuery('10',{'billLodingNo': 'KKLUSH9883671'}))
#print(preplanQuery(logger, session).preplanQuery('11',{'billLodingNo': 'NYKSSH6ATD544600'}))
#print(preplanQuery(logger, session).preplanQuery('12',{'billLodingNo': 'HDMUQSLH6261934'}))
#print(preplanQuery(logger, session).preplanQuery('20',{'billLodingNo': 'SXHKF0181'}))
#print(preplanQuery(logger, session).preplanQuery('21',{'billLodingNo': 'ESLF52074'}))
#print(preplanQuery(logger, session).preplanQuery('22',{'billLodingNo': 'DJSCSHBMSE618505'}))
#print(preplanQuery(logger, session).preplanQuery('23',{'billLodingNo': 'SXCHF1887'}))
#print(preplanQuery(logger, session).preplanQuery('24',{'billLodingNo': 'EGLV142650040483'}))
#print(preplanQuery(logger, session).preplanQuery('25',{'billLodingNo': 'JJNR0002753'}))
#print(preplanQuery(logger, session).preplanQuery('98',{'billLodingNo': '177VSHSHS07723'}))
#print(preplanQuery(logger, session).preplanQuery('99',{'billLodingNo': 'COSU6140723770'}))
