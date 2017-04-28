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
from workserver.module.models import Domain, User, UserGroup, UserGroupMenu
import workserver.settings as settings
from workserver.util import SysUtil


class AuthResource(ServiceBase):
    def on_post(self, req, resp):
        self.initialize()
        doc = req.context['doc']
        try:
            domain = self.session.query(Domain).filter_by(
                domain=doc['domain']).first()

            if domain is None:
                self.errorReturn(GLBConfig.API_ERROR, 'auth_01')

            user = self.session.query(User).filter_by(
                domain_id=domain.uid, username=doc['username'], state=GLBConfig.ENABLE).first()
            if user is None:
                self.errorReturn(GLBConfig.API_ERROR, 'auth_01')
            else:
                if doc['username'] != user.username:
                    self.errorReturn(GLBConfig.API_ERROR, 'auth_01')
                try:
                    decrypted = Cryptor.decrypt(
                        doc['identifyCode'], user.password, doc['magicNo'])

            if decrypted != username:
                self.errorReturn(GLBConfig.API_ERROR, 'auth_01')
            else:
                session_token = Security.user2token(
                    user, doc['identifyCode'], doc['magicNo'], settings.TOKEN_AGE)
                resp.append_header('authorization', session_token)
                returnd = self.loginInit(user)
                if not returnd:
                    self.errorReturn(GLBConfig.SYSTEM_ERROR, 'common_02')
                self.result['info'] = returnd
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.errorReturn(GLBConfig.API_ERROR, 'auth_01')

        req.context['result'] = self.result
        resp.status = falcon.HTTP_200
        self.release()

    def loginInit(self, user):
        returnData = {}
        if user.headImg:
            returnData['avatar'] = user.avatar
        else:
            returnData['avatar'] = '/static/images/base/head.gif'
        returnData['id'] = user.id
        returnData['created_at'] = user.created_at.strftime('%b. %Y')
        exInfo = None
        try:
            userGroup = self.session.query(UserGroup).filter_by(
                uid=user.usergroup_id).first()

            if userGroup:
                returnData.description = usergroup.name
                returnData['menulist'] = self.menuListInit(userGroup.uid)
            else:
                return None
        except Exception as ex:
            self.logger.error(ex)
            return None

        return returnData

    def menuListInit(self, userGroupID):
        def iterationMenu(GroupID, fMenuID):
            returnlist = []
            for item in self.session.query(UserGroupMenu).filter_by(usergroup_id=GroupID, f_menu_id=fMenuID).order_by(UserGroupMenu.menu_index):
                subMenu = []
                if item._type == GLBConfig.MTYPE_ROOT:
                    subMenu = iterationMenu(GroupID, item.uid)
                returnlist.append({'_type': item._type, 'menu_name': item.menu_name,
                                   'menu_path': item.menu_path, 'menu_icon': item.menu_icon, 'sub_menu': sub_menu})
            return returnlist

        return iterationMenu(userGroupID, 0)
