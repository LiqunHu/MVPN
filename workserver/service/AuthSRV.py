# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon

from workserver.util import GLBConfig
from workserver.util import Security
from workserver.util.AES_PKCS7_extension import Cryptor
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import User, OperatorInfo, UserGroupInfo, UserGroupMenu
import workserver.settings as settings
from workserver.util import SysUtil

class AuthResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        doc = req.context['doc']
        username = doc['username']
        try:
            user = self.session.query(User).filter_by(userName=username, dataStatus=GLBConfig.ENABLE).first()
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        if user is None:
            self.errorReturn(GLBConfig.API_ERROR, '用户不存在或密码错误')
        else:
            if doc['username'] != user.userName:
                self.errorReturn(GLBConfig.API_ERROR, '用户不存在或密码错误')
            try:
                decrypted = Cryptor.decrypt(doc['identifyCode'], user.password, doc['magicNo'])
            except Exception as ex:
                SysUtil.exceptionPrint(self.logger, ex)
                self.errorReturn(GLBConfig.API_ERROR, '用户不存在或密码错误')
                
            if decrypted != username:
                self.errorReturn(GLBConfig.API_ERROR, '用户不存在或密码错误')
            else:
                session_token = Security.user2token(user,doc['identifyCode'], doc['magicNo'],settings.TOKEN_AGE)
                resp.append_header('authorization', session_token)
#                resp.set_cookie(settings.COOKIE_NAME, session_token,
#                        max_age=settings.COOKIE_AGE, domain='NULL', secure=False )
                returnd = self.loginInit(user)
                if not returnd:
                    self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
                self.result['data'] = returnd
                
        req.context['result'] = self.result
        resp.set_header('Powered-By', 'putBox')
        resp.status = falcon.HTTP_200
        self.release()
    
    def loginInit(self, user):
        returnData = {}
        if user.headImg:
            returnData['headImg'] = user.headImg
        else:
            returnData['headImg'] = '/static/images/base/head.gif'
        returnData['userID'] = user.userID
        returnData['makedate'] = user.makeTime.strftime('%b. %Y')
        exInfo = None
        try:
            if user.accountType == GLBConfig.ATYPE_ADMINISTRATOR:
                userGroup = self.session.query(UserGroupInfo).filter_by(userGroupType=GLBConfig.GTYPE_ADMINISTRATOR ,userGroupName='Administrator').first()
                if userGroup is not None:
                    menuList = self.menuListInit(userGroup.userGroupID)
                    returnData['menulist'] = menuList
                else:
                    self.errorReturn(GLBConfig.API_ERROR, '用户组不存在')
                
                returnData['role'] = '超级管理员'
                returnData['name'] = user.userName
                returnData['groupName'] = '未知'
            elif user.accountType == GLBConfig.ATYPE_OPERATOR:
                exInfo = self.session.query(OperatorInfo).filter_by(userID=user.userID).first()
                if exInfo is not None:
                    menuList = self.menuListInit(exInfo.userGroupID)
                    returnData['menulist'] = menuList
                    returnData['role'] = '操作员'
                    returnData['name'] = exInfo.name
                    returnData['groupName'] = '未知'
            else:
                return None
        except Exception as ex:
            self.logger.error(ex)
            return None
        finally:
            self.session.close()
            
        return returnData

    def menuListInit(self, userGroupID):
        def iterationMenu(GroupID, fMenuID):
            returnlist = []
            for item in self.session.query(UserGroupMenu).filter_by(userGroupID=GroupID, fMenuID=fMenuID ).order_by(UserGroupMenu.menuIdx):
                subMenu = []
                if item.menuType == GLBConfig.MTYPE_ROOT:
                   subMenu = iterationMenu(GroupID, item.menuID)
                returnlist.append({'menuType':item.menuType, 'menuName':item.menuName, 'menuPath':item.menuPath, 'menuIcon':item.menuIcon, 'subMenu':subMenu })
            return returnlist
        
        return iterationMenu(userGroupID,0)