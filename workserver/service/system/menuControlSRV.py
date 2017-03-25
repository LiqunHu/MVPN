# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import MenuInfo, UserGroupMenu

class MenuControlResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        if req_para['method'] == 'init':
            self.result['data'] = self.initAct()
        elif req_para['method'] == 'search':
            self.result['data'] = self.searchAct()
        elif req_para['method'] == 'add':
            menu = self.addAct(req)
            self.result['data'] = {}
            self.result['data']['menuID'] = menu.menuID
        elif req_para['method'] == 'modify':
            menu = self.modifyAct(req)
            self.result['data'] = {}
        elif req_para['method'] == 'delete':
            menu = self.deleteAct(req)
            self.result['data'] = {}
        else:
            self.errorReturn(GLBConfig.API_ERROR, '不支持该种操作类型')
                
        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()
    
    def initAct(self):
        returnData = {}
        menuData = [{'id': 0,'text': '根菜单'}]
        for menu in self.session.query(MenuInfo).filter_by(menuType=GLBConfig.MENU_LIST_TYPE).order_by(MenuInfo.menuIdx):
            menuData.append({'id':menu.menuID,'text':menu.menuName})
        returnData['fMenuInfo'] = menuData

        return returnData
        
    def searchAct(self):
        returnlist = []
        def iterationMenu(fMenuID):
            for item in self.session.query(MenuInfo).filter_by(fMenuID=fMenuID).order_by(MenuInfo.menuIdx):
                if item.menuType == '00':
                    returnlist.append({'menuID':item.menuID, 'menuType':item.menuType, 'menuIcon':item.menuIcon, 'fMenuID':item.fMenuID, 'menuName':item.menuName, 'menuPath':item.menuPath, 'menuIdx': item.menuIdx})
                    iterationMenu(item.menuID)
                else:
                    returnlist.append({'menuID':item.menuID, 'menuType':item.menuType, 'menuIcon':item.menuIcon, 'fMenuID':item.fMenuID, 'menuName':item.menuName, 'menuPath':item.menuPath, 'menuIdx': item.menuIdx})
            return returnlist
        return iterationMenu(0)
        
    def addAct(self, req):
        doc = req.context['doc']
        menu = self.session.query(MenuInfo).filter_by(menuName=doc['menuName']).first()
        if menu is not None:
            self.errorReturn(GLBConfig.API_ERROR, '菜单名已存在')
        else:
            if doc['fMenuID'] == 0:
                menuType = '00'
            else:
                menuType = '01'
            try:
                menu = MenuInfo(menuName = doc['menuName'],
                    menuIcon = doc['menuIcon'],
                    menuPath = doc['menuPath'],
                    fMenuID = doc['fMenuID'],
                    menuType = menuType,
                    menuIdx = doc['menuIdx'])
                self.session.add(menu)
                self.session.commit()
            except Exception as ex:
                self.logger.error(ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
        return menu
    
    def modifyAct(self, req):
        doc = req.context['doc']
        menu = self.session.query(MenuInfo).filter_by(menuName=doc['old']['menuName']).first()
        if menu is None:
            self.logger.info(doc)
            self.errorReturn(GLBConfig.API_ERROR, '该菜单不存在')
        else:
            if menu.menuID != doc['old']['menuID'] or doc['old']['menuID'] != doc['new']['menuID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '菜单信息出错')

            if (doc['old']['fMenuID'] == 0 and doc['new']['fMenuID'] != 0) or (doc['old']['fMenuID'] != 0 and doc['new']['fMenuID'] == 0):
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '功能菜单和目录菜单不能相互切换')

            try:
                menu.menuName = doc['new']['menuName']
                menu.menuIcon = doc['new']['menuIcon']
                menu.menuPath = doc['new']['menuPath']
                menu.fMenuID = doc['new']['fMenuID']
                menu.menuIdx = doc['new']['menuIdx']
    
                userMenus = self.session.query(UserGroupMenu).filter_by(menuID=menu.menuID).all()
                for userMenu in userMenus:
                    userMenu.menuName = doc['new']['menuName']
                    userMenu.menuIcon = doc['new']['menuIcon']
                    userMenu.menuPath = doc['new']['menuPath']
                    userMenu.fMenuID = doc['new']['fMenuID']
                    userMenu.menuIdx = doc['new']['menuIdx']
                    self.session.merge(userMenu)
                    self.session.flush() # flush the session
    
                self.session.merge(menu)
                self.session.commit()
            except Exception as ex:
                self.logger.error(ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')
                
        return menu
        
    def deleteAct(self, req):
        doc = req.context['doc']
        menu = self.session.query(MenuInfo).filter_by(menuName=doc['menuName']).first()
        if menu is None:
            self.errorReturn(GLBConfig.API_ERROR, '该菜单不存在')
        else:
            if menu.menuID != doc['menuID']:
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '菜单信息出错')
            
            try:
                for subMenu in self.session.query(MenuInfo).filter_by(fMenuID=menu.menuID).all():
                    for subUserMenu in self.session.query(UserGroupMenu).filter_by(menuID=subMenu.menuID).all():
                        self.session.delete(subUserMenu)
                        self.session.flush()
                    
                    self.session.delete(subMenu)
                    self.session.flush()
                    
                for userMenu in self.session.query(UserGroupMenu).filter_by(menuID=menu.menuID).all():
                    self.session.delete(userMenu)
                    self.session.flush() # flush the session
    
                self.session.delete(menu)
                self.session.commit()
            except Exception as ex:
                self.logger.error(ex)
                self.session.rollback()
                self.errorReturn(GLBConfig.SYSTEM_ERROR, '系统错误')