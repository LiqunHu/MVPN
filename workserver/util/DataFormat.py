# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:13:02 2016

@author: huliqun
"""
import logging
import falcon
import json
from werkzeug.http import parse_options_header
from werkzeug.formparser import MultiPartParser, default_stream_factory

from workserver.util import SysUtil


class MultipartMiddleware(object):

    def __init__(self, parser=None):
        self.logger = logging.getLogger('serverLog')

    def process_request(self, req, resp, **kwargs):

        if 'multipart/form-data' not in (req.content_type or ''):
            return

        mimetype, options = parse_options_header(req.content_type)
        size = req.content_length
        #
        boundary = options.get('boundary').encode()
        if not boundary:
            raise ValueError('No boundary')
        #
        parser = MultiPartParser(stream_factory=default_stream_factory)
        form, files = parser.parse(req.stream, boundary, size)
        if 'form' in req._params.keys():
            raise ValueError('form exists')

        if 'files' in req._params.keys():
            raise ValueError('form exists')

        req._params['form'] = form
        req._params['files'] = files

class JSONTranslator(object):
    def __init__(self):
        self.logger = logging.getLogger('serverLog')

    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
            self.logger.info(req.headers)
            self.logger.info('Message length is 0')
            return

        if req.content_type.split(';')[0] == 'application/json':
            body = req.stream.read()
            if not body:
                raise falcon.HTTPBadRequest('Empty request body',
                                            'A valid JSON document is required.')
            try:
                req.context['doc'] = json.loads(body.decode('utf-8'))
                if 'user' in req.context:
                    SysUtil.createOperateLog(req)

            except (ValueError, UnicodeDecodeError):
                raise falcon.HTTPError(falcon.HTTP_753,
                                       'Malformed JSON',
                                       'Could not decode the request body. The '
                                       'JSON was incorrect or not encoded as '
                                       'UTF-8.')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps(req.context['result'])
