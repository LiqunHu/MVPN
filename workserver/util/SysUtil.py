# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:59:20 2016

@author: huliqun
"""
import random, string
import mimetypes
import os
import uuid
import json
import traceback
from selenium import webdriver
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.pool import QueuePool
from PIL import Image
from jinja2 import Environment, PackageLoader
import pdfkit
import falcon

import workserver.settings as settings
from workserver.module.models import UserLog

#http://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
def json_alchemy_encoder(revisit_self = False, fields_excape = []):
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                # go through each field in this SQLalchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    val = obj.__getattribute__(field)

                    # is this field another SQLalchemy object, or a list of SQLalchemy objects?
                    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
                        # unless we're expanding this field, stop here
                        if field in fields_excape:
                            # not expanding this field: set it to None and continue
                            continue
                    try:
                        json.dumps(val)     # this will fail on non-encodable values, like other classes
                        fields[field] = val
                    except TypeError:    # 添加了对datetime的处理
                        if isinstance(val, datetime.datetime):
                            if field == 'modifytime':
                                fields[field] = val.strftime('%Y-%m-%d %H:%M')
                            else:
                                fields[field] = val.strftime('%Y-%m-%d')
                        elif isinstance(val, datetime.date):
                            fields[field] = val.isoformat()
                        elif isinstance(val, datetime.timedelta):
                            fields[field] = (datetime.datetime.min + val).time().isoformat()
                        else:
                            fields[field] = None
                    if fields[field] is None:
                        fields[field] = ''
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder

def schema2Json(schemaIns):
    return json.loads(json.dumps(schemaIns, cls=json_alchemy_encoder(False, []), check_circular=False))

class GlobalVar:
    engine_handle = None
    enginer_handle = None
    db_handle = None
    glb_browser = None
    glb_browser_in_use = 0
    jinja2env = Environment(loader=PackageLoader('workserver', 'templates'))

def global_init():
    GlobalVar.engine_handle = create_engine(settings.dbUrl, encoding="utf-8",poolclass=QueuePool, pool_size=50, pool_recycle=3600, echo=settings.dbEchoFlag)
    GlobalVar.db_handle = sessionmaker(bind=GlobalVar.engine_handle)

def get_engine_handle():
    return GlobalVar.engine_handle

def get_db_handle():
    return GlobalVar.db_handle

def get_glb_browser():
    if GlobalVar.glb_browser is None:
        GlobalVar.glb_browser = webdriver.PhantomJS()

    if GlobalVar.glb_browser_in_use > 0:
        GlobalVar.glb_browser_in_use += 1
        if  GlobalVar.glb_browser_in_use > 20:
            free_glb_browser()
        return 'delay'
    else:
        GlobalVar.glb_browser_in_use = 1

    return GlobalVar.glb_browser

def get_jinja2_env():
    return GlobalVar.jinja2env

def release_glb_browser():
    GlobalVar.glb_browser_in_use = 0

def free_glb_browser():
    if GlobalVar.glb_browser is not None:
        GlobalVar.glb_browser.quit()
        GlobalVar.glb_browser = None

def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def genUserID():
    return random_word(5) + str(uuid.uuid1()).replace('-','')

def fileSave(req,logger):
    filename = ''
    if 'multipart/form-data' in (req.content_type or ''):
        uploadfile = req.params['files'].getlist('file')
        if uploadfile:
            ext = mimetypes.guess_extension(uploadfile[0].mimetype)
            filename = '{uuid}{ext}'.format(uuid=str(uuid.uuid4()).replace('-',''), ext=ext)
            file_path = os.path.join(settings.temp_path, filename)
            logger.info(file_path)

            with open(file_path, 'wb') as upload_file:
                while True:
                    chunk = uploadfile[0].stream.read(4096)
                    if not chunk:
                        break

                    upload_file.write(chunk)

        avatar_file =  req.params['files'].getlist('avatar_file')
        if avatar_file:
            img = Image.open(avatar_file[0].stream)

            avatar_data =  req.params['form'].getlist('avatar_data')
            if avatar_data:
                img_trans = json.loads(avatar_data[0])
                rotate_img = img.rotate(-1 *img_trans['rotate'])
                crop_img = rotate_img.crop((img_trans['x'], img_trans['y'], img_trans['x'] + img_trans['width'], img_trans['y'] + img_trans['height']))


            filename = '{uuid}.jpg'.format(uuid=str(uuid.uuid4()).replace('-',''))
            image_path = os.path.join(settings.temp_path, filename)
            crop_img.save(image_path)
#        ext = mimetypes.guess_extension(req.content_type)
    else:
        ext = mimetypes.guess_extension(req.content_type)
        filename = '{uuid}{ext}'.format(uuid=str(uuid.uuid4()).replace('-',''), ext=ext)
        image_path = os.path.join(settings.temp_path, filename)
        logger.info(image_path)

        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break

                image_file.write(chunk)

    return settings.tmp_url_base + filename

def getRandomPdf(template, pagePara, pdfkit_options, logger):
    try:
        env = get_jinja2_env()
        template = env.get_template(template)
        htmlString = template.render(pagePara=pagePara)
#        output = open('/home/putbox/11.html', 'w')
#        output = open('E:/11.html', 'w')
#        output.write(htmlString)
#        output.close()
        filename = '{uuid}.pdf'.format(uuid=str(uuid.uuid4()).replace('-',''))
        file_path = os.path.join(settings.temp_path, filename)
        file_url = settings.tmp_url_base + filename
        pdfkit.from_string(htmlString, file_path, pdfkit_options)
        return file_path, file_url
    except Exception as ex:
        exceptionPrint(logger, ex)
        return None, None

def fileMmove(url, mode='date', reladir=''):
    filename = url.split('/')[-1]
    if mode == 'date':
        nowDate = datetime.datetime.now()
        relpath = nowDate.strftime('%Y') + '/' + nowDate.strftime('%m') + '/' + nowDate.strftime('%d') + '/'
    if mode == 'file':
        nowDate = datetime.datetime.now()
        relpath = 'files/' + nowDate.strftime('%Y') + '/' + nowDate.strftime('%m') + '/' + nowDate.strftime('%d') + '/'
    elif mode == 'dir':
        relpath = reladir + '/'

    svpath = os.path.join(settings.files_storage_path, relpath)

    if not os.path.exists(svpath):
        os.makedirs(svpath)

    os.rename(os.path.join(settings.temp_path, filename), os.path.join(svpath, filename))
    return settings.images_url_base + relpath + filename

def exceptionPrint(logger, ex):
    logger.error(traceback.print_exc())
    logger.error(ex)

def genLogID():
    db = get_db_handle()
    session = db()
    currentIndex = int(session.execute('select nextval(\'LogSeq\')').first()[0])
    index = '%011d' % (currentIndex)
    today = datetime.datetime.now().strftime('LG%Y%m%d')
    session.commit()
    return today + index

def createOperateLog(req):
    methodApi = req.path.split('/')[-1].upper()
    if methodApi == 'AUTH':
        return

    req_para = falcon.util.uri.parse_query_string(req.query_string)
    if req_para['method'] == 'init':
        return
    elif req_para['method'] == 'search':
        return

    db = get_db_handle()
    session = db()
    userLog = UserLog(uid = genLogID(),
            userID = req.context['user'].userID,
            API = req.relative_uri,
            paras = str(req.context['doc']))
    session.add(userLog)
    session.commit()

def numMoneyFormat(num):
    if num:
        return '%.2f' % (num/100.00)
    else:
        return '0.00'

def moneyNumFormat(money):
    return round(float(money) * 100)

def readAppVersion():
    result = {}
    file_object = open('appVersion.txt')
    try:
        code = file_object.readline().strip('\n')
        name = file_object.readline().strip('\n')
        path = file_object.readline().strip('\n')
        result['code'] = code
        result['name'] = name
        result['path'] = path
    finally:
        file_object.close()
        return result
