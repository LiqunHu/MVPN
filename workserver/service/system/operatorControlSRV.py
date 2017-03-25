# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon
import datetime

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import User, OperatorInfo, UserGroupInfo
from workserver.util import SysUtil

class OperatorControlResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        if req_para['method'] == 'init':
            self.result['data'] = self.initAct(req)
        elif req_para['method'] == 'search':
            self.result['data'] = self.searchAct(req)
        elif req_para['method'] == 'add':
            user = self.addAct(req)
            self.result['data'] = {}
            self.result['data']['userID'] = user.userID
        elif req_para['method'] == 'modify':
            user = self.modifyAct(req)
            self.result['data'] = {}
        elif req_para['method'] == 'delete':
            user = self.deleteAct(req)
            self.result['data'] = {}
        else:
            self.errorReturn(GLBConfig.API_ERROR, '方法不支持.')
                
        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()
    
    def initAct(self,req):
        opuser = req.context['user']
        returnData = {}
        groupData = []
        for group in self.session.query(UserGroupInfo).filter(UserGroupInfo.userGroupType==GLBConfig.GTYPE_OPERATORGROUP,  
                                                              UserGroupInfo.userGroupStatus==GLBConfig.ENABLE):
            groupData.append({'id':group.userGroupID, 'value':group.userGroupID, 'text':group.userGroupName})
        returnData['groupInfo'] = groupData
        return returnData
        
    def searchAct(self,req):
        result = []
        for user, operator in self.session.query(User, OperatorInfo).\
            filter(User.userID==OperatorInfo.userID).\
            filter(User.accountType==GLBConfig.ATYPE_OPERATOR).\
            filter(User.dataStatus==GLBConfig.ENABLE).\
            order_by(User.makeTime.desc()).all():
            row = {}
            row = SysUtil.schema2Json(operator)
            row['userName'] = user.userName
            result.append(row)
        return result
        
    def addAct(self,req):
        opuser = req.context['user']
        doc = req.context['doc']
        user = self.session.query(User).filter_by(userName=doc['userName']).first()
        if user is not None:
            self.errorReturn(GLBConfig.API_ERROR, '用户已存在.')
        else:
            try:
                user = User(userID = SysUtil.genUserID(),
                    userName = doc['userName'],
                    password = GLBConfig.INITPASSWORD,
                    accountType = GLBConfig.ATYPE_OPERATOR,
                    mobile = doc['mobile'],
                    email = doc['email'])
                self.session.add(user)
                self.session.flush() # flush the session
                operator = OperatorInfo(
                    userID = user.userID,
                    userGroupID = doc['userGroupID'],
                    helpMark = doc['helpMark'],
                    name = doc['name'],
                    mobile = doc['mobile'],
                    email = doc['email'],
                    )
                self.session.add(operator)
                self.session.commit()
            except Exception as ex:
                SysUtil.exceptionPrint(self.logger, ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        return user
    
    def modifyAct(self,req):
        opuser = req.context['user']
        doc = req.context['doc']
        user = self.session.query(User).filter_by(userName=doc['old']['userName']).first()
        if user is None:
            self.logger.info(doc)
            self.errorReturn(GLBConfig.API_ERROR, '用户不存在')
        else:
            if user.userID != doc['old']['userID'] or doc['old']['userID'] != doc['new']['userID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '用户信息错误')
            try:
                user.userName = doc['new']['userName']
                user.mobile = doc['new']['mobile']
                user.email = doc['new']['email']
                
                operator = self.session.query(OperatorInfo).filter_by(userID=user.userID).first()
                if operator is None:
                    self.errorReturn(GLBConfig.API_ERROR, '用户不存在')
                operator.userGroupID = doc['new']['userGroupID']
                operator.name = doc['new']['name']
                operator.helpMark = doc['new']['helpMark'],
                operator.mobile = doc['new']['mobile']
                operator.email = doc['new']['email']
                self.session.commit()
            except Exception as ex:
                SysUtil.exceptionPrint(self.logger, ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        return user
        
    def deleteAct(self,req):
        opuser = req.context['user']
        doc = req.context['doc']
        user = self.session.query(User).filter_by(userName=doc['userName']).first()
        if user is None:
            self.errorReturn(GLBConfig.API_ERROR, '用户不存在')
        else:
            if user.userID != doc['userID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '用户信息错误')
            operator = self.session.query(OperatorInfo).filter_by(userID=user.userID).first()
            if operator is None:
                self.errorReturn(GLBConfig.API_ERROR, '用户不存在')
            try:     
                operator.dataStatus = GLBConfig.DISABLE
                operator.modifyTime = datetime.datetime.now()
                user.dataStatus = GLBConfig.DISABLE
                user.modifyTime = datetime.datetime.now()
                self.session.commit()
            except Exception as ex:
                SysUtil.exceptionPrint(self.logger, ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')