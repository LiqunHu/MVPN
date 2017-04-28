# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:13:02 2016

@author: huliqun
"""

import falcon
import logging

from workserver.util import Security
from workserver.util import GLBConfig
from workserver.module.models import Menu


class AuthMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger('serverLog')
        self.db = SysUtil.get_db_handle()

    def initialize(self):
        self.session = self.db()

    def release(self):
        self.session.close()

    def process_request(self, req, resp):
        try:
            self.initialize()
            menuList = self.session.query(Menu).filter_by(
                auth_flag=GLBConfig.NOAUTH, state=GLBConfig.ENABLE).all()
            if authCheckFlag is None:
                self.logger.info('authCheckFlag')
                raise falcon.HTTPError(falcon.HTTP_703,
                                       'API error',
                                       'Please make sure your api is correct.')

            if authCheckFlag:
                user = Security.token2user(req, self.logger)

                if user is None:
                    self.logger.info('UNAUTHORIZED')
                    raise falcon.HTTPError(falcon.HTTP_401,
                                           'UNAUTHORIZED',
                                           'Auth Failed or session expired')
                req.context['user'] = user
        except Exception as ex:
            self.logger.error(ex)
            raise falcon.HTTPError(falcon.HTTP_401,
                                   'UNAUTHORIZED',
                                   'Auth Failed or session expired')


class MimeTypesCheck(object):
    def __init__(self):
        self.logger = logging.getLogger('serverLog')

    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPError(falcon.HTTP_406,
                                   'NOT_ACCEPTABLE',
                                   'This API only supports responses encoded as JSON.')
        if 'application/json' in req.content_type.split(';'):
            length = req.content_length
            if length is not None and length > GLBConfig.MAX_BODY_LIMIT:
                raise falcon.HTTPError(falcon.HTTP_413,
                                       'TOO_LARGE',
                                       'The size of the request is too large.')

        if req.method in ('POST', 'PUT', 'GET'):
            req_para = falcon.util.uri.parse_query_string(req.query_string)
            if 'method' in req_para.keys() and req_para['method'] == 'upload':
                return
            if req.content_type.split(';')[0] not in GLBConfig.ALLOWED_MIME_TYPES:
                self.logger.info(req.content_type)
                raise falcon.HTTPError(falcon.HTTP_415,
                                       'UNSUPPORTED_MEDIA_TYPE',
                                       'content type error.')
