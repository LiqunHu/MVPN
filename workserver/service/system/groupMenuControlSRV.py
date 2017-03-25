# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:27:57 2016

@author: lixiaomeng
"""
import falcon
from sqlalchemy import and_, or_, not_

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import MenuInfo, UserGroupInfo, UserGroupMenu
from workserver.util import SysUtil

class GroupMenuControlResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        if req_para['method'] == 'init':
            self.result['data'] = self.initAct(req)
        elif req_para['method'] == 'search':
            self.result['data'] = self.searchAct(req)
        elif req_para['method'] == 'searchCheck':
            self.result['data'] = self.searchCheckAct(req)
        elif req_para['method'] == 'modify':
            self.modifyAct(req)
            self.result['data'] = {}
        else:
            self.errorReturn(GLBConfig.API_ERROR, '方法不支持')
                
        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()
        
    def initAct(self,req):
        opuser = req.context['user']
        returnData = {}
        returnData['groupInfo'] = []
        for group in self.session.query(UserGroupInfo).\
            filter_by(userGroupType=GLBConfig.GTYPE_OPERATORGROUP, userGroupStatus=GLBConfig.ENABLE):
            returnData['groupInfo'].append({
                              'id': group.userGroupID, 
                              'text': group.userGroupName, 
                             })
        
        menuInfo = []

        def iterationMenu(fMenuID):
            for item in self.session.query(MenuInfo).\
                filter(MenuInfo.fMenuID==fMenuID).\
                order_by(MenuInfo.menuIdx):
                if item.menuType == '00':
                    menuInfo.append({'menuID':item.menuID, 'menuType':item.menuType, 'menuIcon':item.menuIcon, 'fMenuID':item.fMenuID, 'menuName':item.menuName, 'menuPath':item.menuPath, 'menuIdx': item.menuIdx})
                    iterationMenu(item.menuID)
                else:
                    menuInfo.append({'menuID':item.menuID, 'menuType':item.menuType, 'menuIcon':item.menuIcon, 'fMenuID':item.fMenuID, 'menuName':item.menuName, 'menuPath':item.menuPath, 'menuIdx': item.menuIdx})
            return menuInfo
            
        returnData['menuInfo'] = iterationMenu(0)
        return returnData
        
    def searchCheckAct(self,req):
        doc = req.context['doc']
        returnData = {}
        groupMenus = []
        for item in self.session.query(UserGroupMenu).filter_by(userGroupID=doc['userGroupID']).all():
            groupMenus.append(item.menuID)

        returnData['groupMenu'] = groupMenus
        return returnData
    
    def modifyAct(self,req):
        doc = req.context['doc']

        try:
            self.session.query(UserGroupMenu).filter(UserGroupMenu.userGroupID==doc['userGroupID']).delete()
            self.session.flush()
            
            for menu in doc['userGroupMenu']:
                userGroupMenu = UserGroupMenu(
                            userGroupID = doc['userGroupID'],
                            menuID = menu['menuID'],
                            menuType = menu['menuType'],
                            fMenuID = menu['fMenuID'],
                            menuName = menu['menuName'],
                            menuPath = menu['menuPath'],
                            menuIcon = menu['menuIcon'],
                            menuIdx = menu['menuIdx'])
                self.session.add(userGroupMenu)
                self.session.flush()
            self.session.commit()
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.session.rollback()
            self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')    