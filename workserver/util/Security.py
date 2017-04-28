# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:13:02 2016

@author: huliqun
"""
import hashlib
import falcon
import time

from workserver.util import GLBConfig
from workserver.util import SysUtil
from workserver.util.AES_PKCS7_extension import Cryptor
from workserver.module.models import User, UserGroupMenu, UserGroupInfo
import workserver.settings as settings
ALLOWED_IMAGE_TYPES = (
    'image/jpg',                   
    'image/gif',
    'image/jpeg',
    'image/png',
)
    
def validate_image_type(req, resp, resource, params):
    if req.content_type not in ALLOWED_IMAGE_TYPES:
        msg = 'Image type not allowed. Must be PNG, JPEG, or GIF'
        raise falcon.HTTPBadRequest('Bad request', msg)

def user2token(user, identifyCode, magicNo,max_age):
    '''
    Generate token str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.userID, identifyCode, expires, settings.SECRET_KEY)
    L = [user.userID, magicNo, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

def token2user(req,logging):
    token_str = req.get_header('authorization')
    db = SysUtil.get_db_handle()
    session = db()
    if not token_str:
        logging.info('no token')
        return None
    try:
        L = token_str.split('-')
        if len(L) != 4:
            return None
        
        uid, magicNo, expires, sha1 = L
        if int(expires) < time.time():
            logging.info('expires')
            return None
        
        user = session.query(User).filter_by(userID=uid, dataStatus=GLBConfig.ENABLE).first()
        if user is None:
            logging.info('user do not exist')
            return None
        magicNo, idf = Cryptor.encrypt(user.userName, user.password, magicNo)
        s = '%s-%s-%s-%s' % (uid, idf, expires, settings.SECRET_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        if userAuthCheck(session, req, user, logging) == False:
            logging.info('userAuthCheck Failed')
            return None
        return user
    except Exception as e:
        SysUtil.exceptionPrint(logging, e)
        return None
    finally:
        session.close()
        

def userAuthCheck(session, req, user, logging):
    if user is None:
        logging.info('user is none')
        return False
    else:
        exInfo = None
        if user.accountType == GLBConfig.TYPE_OPERATOR:
            exInfo = session.query(OperatorInfo).filter_by(userID=user.userID).first()

        if exInfo is not None:
            userGroupID = exInfo.userGroupID
        elif user.accountType == GLBConfig.ATYPE_ADMINISTRATOR or user.accountType == GLBConfig.ATYPE_PUTBOXCOMPANY:
            if user.accountType == GLBConfig.ATYPE_ADMINISTRATOR:
                groupType = GLBConfig.GTYPE_ADMINISTRATOR
            else:
                groupType = GLBConfig.GTYPE_PUTBOXCOMPANY

            userGroup = session.query(UserGroupInfo).filter_by(userGroupType=groupType).first()
            if userGroup is not None:
                userGroupID = userGroup.userGroupID
            else:
                return False
        else:
            return False
        
        menuLists = session.query(UserGroupMenu).filter_by(userGroupID = userGroupID)
        menus = [ item.menuPath.split('/')[-1].upper() for item in menuLists]
        funcStr = req.path.split('/')[-1].upper()
        if funcStr not in menus and funcStr != 'AUTH' and funcStr != 'USERSETTINGCONTROL':
            logging.info(userGroupID)
            logging.info(menus)
            logging.info(funcStr)
            logging.info('menus not in funcStr')
            return False
            
        return True
    return True
            