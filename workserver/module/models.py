# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:18:23 2016

@author: huliqun
"""
from sqlalchemy import Column, Integer, SmallInteger, String, Date, Time,\
    Text, DateTime, func,BigInteger,Float
from sqlalchemy.ext.declarative import declarative_base
from workserver.util import GLBConfig

Base = declarative_base()

class User(Base):
    __tablename__ = 'tbl_user'
    userID = Column(String(50), primary_key=True, unique=True, nullable=False)
    accountType = Column(String(2), nullable=False) #00-管理员
    userName = Column(String(32), unique=True, nullable=False)
    mobile = Column(String(250))
    email = Column(String(250))
    _password = Column('password', String(64), default='', nullable=False)
    pResetFlag = Column(String(2), default='0', nullable=False)
    pChangeDate = Column(DateTime(), default=func.now(), nullable=False)
    pErrorTimes = Column(Integer, default=0, nullable=False)
    headImg = Column(String(250))
    makeTime = Column(DateTime(), default=func.now(), nullable=False)
    modifyTime = Column(DateTime(), default=func.now(), nullable=False)
    # status: 1 enable, 0 disabled
    dataStatus = Column(String(5), default=GLBConfig.ENABLE, nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        import hashlib
        # encrypt the password with md5
        self._password = hashlib.md5(password.encode('utf-8')).hexdigest()

class UserFileInfo(Base):
    __tablename__ = 'tbl_userfileinfo'
    fileID = Column(BigInteger, primary_key=True,autoincrement=True)
    userID = Column(String(50))
    path = Column(String(300))
    apiName = Column(String(30), nullable=False)
    relaID = Column(String(80))
    fileType = Column(String(30))
    makeTime = Column(DateTime(), default=func.now())
    modifyTime = Column(DateTime(), default=func.now())

class OperatorInfo(Base):
    __tablename__ = 'tbl_operatorinfo'
    userID = Column(String(50), primary_key=True, nullable=False)
    userGroupID =  Column(Integer)
    name = Column(String(32))
    mobile = Column(String(250))
    email = Column(String(250))
    gender = Column(String(2), default='U')
    IDType = Column(String(2), default='00')
    IDNo = Column(String(30))
    birthday = Column(DateTime)
    helpMark = Column(String(32))
    contact = Column(String(100))
    address = Column(String(200))
    makeTime = Column(DateTime(), default=func.now(), nullable=False)
    modifyTime = Column(DateTime(), default=func.now(), nullable=False)
    dataStatus = Column(String(5), default=GLBConfig.ENABLE, nullable=False)

class UserGroupInfo(Base):
    __tablename__ = 'tbl_usergroupinfo'
    userGroupID = Column(Integer, primary_key=True,autoincrement=True)
    userGroupType = Column(String(10), nullable=False)
    userGroupName = Column(String(250), nullable=False)
    userGroupStatus =  Column(String(10), default='1', nullable=False)

class MenuInfo(Base):
    __tablename__ = 'tbl_menuinfo'
    menuID = Column(Integer, primary_key=True,autoincrement=True)
    menuType = Column(String(2), nullable=False) #00-目录 01菜单
    fMenuID  = Column(Integer, nullable=False)
    menuName = Column(String(250), default='', nullable=False)
    menuPath = Column(String(250), default='', nullable=True)
    menuIcon = Column(String(250), default='', nullable=True)
    menuIdx = Column(Integer, default=99, nullable=False)

class UserGroupMenu(Base):
    __tablename__ = 'tbl_usergroupmenu'
    userGroupID = Column(Integer, primary_key=True, nullable=False)
    menuID = Column(Integer, primary_key=True, nullable=False)
    menuType = Column(String(2), nullable=False) #00-目录 01菜单
    fMenuID  = Column(Integer, nullable=False)
    menuName = Column(String(250), default='', nullable=False)
    menuPath = Column(String(250), default='', nullable=True)
    menuIcon = Column(String(250), default='', nullable=True)
    menuIdx = Column(Integer, default=99, nullable=False)

class UserLog(Base):
    __tablename__ = 'tbl_userlog'
    uid = Column(String(50), primary_key=True, nullable=False)
    userID = Column(String(50))
    API = Column(String(100))
    paras = Column(Text)
