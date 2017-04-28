# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:55:50 2016

@author: huliqun
"""

ALLOWED_MIME_TYPES = (
    'application/json',
    'multipart/form-data',
    'image/jpg',
    'image/gif',
    'image/jpeg',
    'image/png',
    'application/pdf',
)

MAX_BODY_LIMIT = 64 * 1024

INITPASSWORD = '123456'

# error type
API_ERROR = 'API ERROR'
SYSTEM_ERROR = 'SYSTEM ERROR'

# status code
ENABLE = '1'
DISABLE = '0'
STSTUSINFO = [
    {'id': ENABLE, 'value': ENABLE, 'text': '有效'},
    {'id': DISABLE, 'value': DISABLE, 'text': '无效'}
]

# status code
SUCCESS = '1'
FAILED = '0'

# status code
TRUE = '1'
FALSE = '0'

# menu auth flag
AUTH = '1'
NOAUTH = '0'

# GENDER
UNKNOWN = 'U'
MALE = 'M'
FEMALE = 'F'

GENDERINFO = [
    {'id': 'U', 'value': 'U', 'text': '未知'},
    {'id': 'M', 'value': 'M', 'text': '男'},
    {'id': 'F', 'value': 'F', 'text': '女'}
]

# ID
IDTYPE_IDCARD = '01'

PASSWORD_DEFAULT = '88888888'

IDTYPEINFO = [
    {'id': '00', 'value': '00', 'text': '未知'},
    {'id': '01', 'value': '01', 'text': '身份证'},
    {'id': '02', 'value': '02', 'text': '居住证'},
    {'id': '03', 'value': '03', 'text': '签证'},
    {'id': '04', 'value': '04', 'text': '护照'},
    {'id': '05', 'value': '05', 'text': '户口本'},
    {'id': '06', 'value': '06', 'text': '军人证'},
    {'id': '07', 'value': '07', 'text': '港澳通行证'}
]

# menu type
MTYPE_ROOT = '00'
MTYPE_LEAF = '01'

# type
TYPE_ADMINISTRATOR = '00'
TYPE_OPERATORGROUP = '01'

# file type
FTYPE_IMG = '0'
FTYPE_FILE = '1'
