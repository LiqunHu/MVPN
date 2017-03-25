# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:13:02 2016

@author: huliqun
"""
import logging
import falcon

from workserver.util import SysUtil,GLBConfig

class ServiceBase(object):
    db = None
    dbr = None
    result = {}
    result['retCode'] = 0
    result['message'] = 'Success'
    result['data'] = None
    
    def __init__(self):
        self.logger = logging.getLogger('serverLog')
        self.engine = SysUtil.get_engine_handle()        
        self.db = SysUtil.get_db_handle()
        
    def initialize(self):
        self.session = self.db()    
    
    def release(self):
        self.session.close()
        
    def __del__(self):
        pass
#        if self.db is not None:
#            self.db.remove()
#        if self.dbr is not None:
#            self.dbr.remove()

    def errorReturn(self, errorType, message):
        self.session.rollback()
        self.session.close()
        
        errorCode = falcon.HTTP_701
        if errorType == GLBConfig.API_ERROR:
            errorCode = falcon.HTTP_702
        elif errorType == GLBConfig.SYSTEM_ERROR:
            errorCode = falcon.HTTP_703
        
        raise falcon.HTTPError(errorCode,
               errorType,
               message)