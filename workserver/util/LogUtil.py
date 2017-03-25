# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:59:20 2016

@author: huliqun
"""
import logging

import workserver.settings as settings

class LogUtil(object):
    
    @staticmethod
    def initLog():
        logger = logging.getLogger('serverLog')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(settings.log_file)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)

    @staticmethod
    def initLogBatch(className):
        logger = logging.getLogger('batchLog_'+className)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(settings.log_file + '_' + className)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)

