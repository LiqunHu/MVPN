# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon
import datetime

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import User, OperatorInfo
from workserver.util import SysUtil

class UserSettingResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        if req_para['method'] == 'setpwd':
            self.setpwdAct(req)
            self.result['data'] = {}
        elif req_para['method'] == 'midify':
            self.modifyAct(req)
            self.result['data'] = {}
        elif req_para['method'] == 'upload':
            uploadurl = self.uploadAct(req)
            self.result['data'] = {}
            self.result['data']['uploadurl'] = uploadurl
        else:
            self.errorReturn(GLBConfig.API_ERROR, '方法不支持.')
                
        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()
    
    def modifyAct(self, req):
        opuser = req.context['user']
        doc = req.context['doc']
        try:
            u = self.session.query(User).filter_by(userID=opuser.userID).first()
            if u is None:
                self.errorReturn(GLBConfig.API_ERROR, '用户不存在.')
            if doc['headImg']:
                if u.headImg != doc['headImg']:
                    u.headImg = SysUtil.fileMmove(doc['headImg'], 'dir', 'headimg')
            if doc['mobile']:
                u.mobile = doc['mobile']
            
            exInfo = None
            if u.accountType == GLBConfig.ATYPE_OPERATOR:
                exInfo = self.session.query(OperatorInfo).filter_by(userID=u.userID).first()
            
            if exInfo is not None:
                if doc['mobile']:
                    exInfo.mobile = doc['mobile']
    
                if doc['name']:
                    exInfo.name = doc['name']
            self.session.commit()
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.logger.error(doc)
            self.session.rollback()
            self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
    
    def setpwdAct(self,req):
        opuser = req.context['user']
        doc = req.context['doc']

        if opuser.password != doc['oldPwd']:
            self.errorReturn(GLBConfig.API_ERROR, '密码错误.')
        
        u = self.session.query(User).filter_by(userID=opuser.userID).first()
        if u is None:
            self.errorReturn(GLBConfig.API_ERROR, '用户不存在.')
        u._password = doc['pwd']
        u.pChangeDate = datetime.datetime.now()
        self.session.commit()
    
    def uploadAct(self,req):
        try:
            uploadurl = SysUtil.fileSave(req,self.logger)            
            return uploadurl
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.session.rollback()
            self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')