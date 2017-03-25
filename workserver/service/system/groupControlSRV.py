# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:27:57 2016

@author: lixiaomeng
"""
import falcon
from sqlalchemy.sql import text

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import OperatorInfo, UserGroupInfo
from workserver.util import SysUtil

class GroupControlResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        if req_para['method'] == 'init':
            self.result['data'] = self.initAct(req)
        elif req_para['method'] == 'search':
            self.result['data'] = self.searchAct(req)
        elif req_para['method'] == 'add':
            self.result['data'] = self.addAct(req)
        elif req_para['method'] == 'modify':
            self.modifyAct(req)
            self.result['data'] = {}
        elif req_para['method'] == 'delete':
            self.deleteAct(req)
            self.result['data'] = {}
        else:
            self.errorReturn(GLBConfig.API_ERROR, '方法不支持')
                
        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()
    
    def initAct(self,req):
        returnData = {}
        returnData['statusInfo'] = GLBConfig.STSTUSINFO
        return returnData
        
    def searchAct(self,req):
        result = []         
        
        for col in self.session.query(UserGroupInfo).\
            filter(UserGroupInfo.userGroupType!=GLBConfig.GTYPE_ADMINISTRATOR).\
            filter(UserGroupInfo.userGroupName!='administrator').\
            all():
            row = {}
            row = SysUtil.schema2Json(col)
            result.append(row)
        return result
        
    def addAct(self,req):
        doc = req.context['doc']
        rtn = {}
        userGroup = self.session.query(UserGroupInfo).filter_by(userGroupName=doc['userGroupName']).first()
        if userGroup is not None:
            self.errorReturn(GLBConfig.API_ERROR, '用户组已经存在')
        else:
            try:
                userGroup = UserGroupInfo(userGroupType = GLBConfig.GTYPE_OPERATORGROUP,
                                          userGroupName = doc['userGroupName'],
                                          userGroupStatus = GLBConfig.ENABLE)
                self.session.add(userGroup)
                self.session.commit()
                rtn = SysUtil.schema2Json(userGroup)
            except Exception as ex:
                self.logger.error(ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        return rtn
    
    def modifyAct(self,req):
        doc = req.context['doc']
        userGroup = self.session.query(UserGroupInfo).filter_by(userGroupName=doc['old']['userGroupName']).first()
        if userGroup is None:
            self.logger.info(doc)
            self.errorReturn(GLBConfig.API_ERROR, '用户组不存在')
        else:
            if userGroup.userGroupID != doc['old']['userGroupID'] or doc['old']['userGroupID'] != doc['new']['userGroupID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '用户组信息错误')

            try:
                userGroup.userGroupName = doc['new']['userGroupName']
                userGroup.userGroupStatus = doc['new']['userGroupStatus']
                self.session.commit()
            except Exception as ex:
                self.logger.error(ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        return userGroup
        
    def deleteAct(self,req):
        doc = req.context['doc']
        userGroup = self.session.query(UserGroupInfo).filter_by(userGroupName=doc['userGroupName']).first()
        if userGroup is None:
            self.errorReturn(GLBConfig.API_ERROR, '用户组不存在')
        else:
            if userGroup.userGroupID != doc['userGroupID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '用户组信息错误')
            else:
                operatorInfos = self.session.query(OperatorInfo).filter_by(userGroupID=userGroup.userGroupID).all()
                
                if len(operatorInfos) > 0:
                    self.errorReturn(GLBConfig.API_ERROR, '组下已存在操作员')
                else:
                    try:
                        self.session.delete(userGroup)
                        self.session.commit()
                    except Exception as ex:
                        self.logger.error(ex)
                        self.session.rollback()
                        self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')