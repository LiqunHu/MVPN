# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:18:23 2016

@author: huliqun
"""
from sqlalchemy import Column, Integer, SmallInteger, String, Date, Time,\
    Text, DateTime, func, BigInteger, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.interfaces import MapperExtension
from workserver.util import GLBConfig

Base = declarative_base()


class BaseExtension(MapperExtension):
    def before_update(self, mapper, connection, instance):
        """ set the updated_at  """
        instance.version += 1


class Domain(Base):
    __tablename__ = 'tbl_domain'
    __mapper_args__ = {'extension': BaseExtension()}
    uid = Column('id', BigInteger, primary_key=True, autoincrement=True)
    domain = Column(String(100), unique=True, nullable=False)
    description = Column(String(200))
    state = Column(String(5), default=GLBConfig.ENABLE, nullable=False)
    version = Column(BigInteger, default=0, nullable=False)
    created_at = Column(DateTime(), default=func.now(), nullable=False)
    updated_at = Column(DateTime(), default=func.now(), nullable=False)


class User(Base):
    __tablename__ = 'tbl_user'
    __mapper_args__ = {'extension': BaseExtension()}
    uid = Column('id', BigInteger, primary_key=True, autoincrement=True)
    domain_id = Column(BigInteger, nullable=False)
    usergroup_id = Column(BigInteger, nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    _password = Column('password', String(100), default='', nullable=False)
    name = Column(String(20))
    gender = Column(String(1))
    avatar = Column(String(200))
    address = Column(String(100))
    country = Column(String(20))
    city = Column(String(40))
    zipcode = Column(String(32))
    _type = Column('type', String(3), nullable=False)  # 00-管理员
    state = Column(String(5), default=GLBConfig.ENABLE, nullable=False)
    version = Column(BigInteger, default=0, nullable=False)
    created_at = Column(DateTime(), default=func.now(), nullable=False)
    updated_at = Column(DateTime(), default=func.now(), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        import hashlib
        # encrypt the password with md5
        self._password = hashlib.md5(password.encode('utf-8')).hexdigest()


class UserGroup(Base):
    __tablename__ = 'tbl_usergroup'
    __mapper_args__ = {'extension': BaseExtension()}
    uid = Column('id', BigInteger, primary_key=True, autoincrement=True)
    domain_id = Column(BigInteger, nullable=False)
    name = Column(String(50))
    _type = Column('type', String(3), nullable=False)
    state = Column(String(5), default=GLBConfig.ENABLE, nullable=False)
    version = Column(BigInteger, default=0, nullable=False)
    created_at = Column(DateTime(), default=func.now(), nullable=False)
    updated_at = Column(DateTime(), default=func.now(), nullable=False)


class Menu(Base):
    __tablename__ = 'tbl_menu'
    __mapper_args__ = {'extension': BaseExtension()}
    uid = Column('id', BigInteger, primary_key=True, autoincrement=True)
    _type = Column('type', String(3), nullable=False)
    f_menu_id = Column(BigInteger, nullable=False)
    auth_flag = Column(String(2), default=GLBConfig.AUTH, nullable=False)
    menu_name = Column(String(100), nullable=False)
    menu_path = Column(String(100))
    menu_icon = Column(String(100))
    menu_index = Column(Integer, default=99, nullable=False)


class UserGroupMenu(Base):
    __tablename__ = 'tbl_usergroupmenu'
    __mapper_args__ = {'extension': BaseExtension()}
    uid = Column('id', BigInteger, primary_key=True, autoincrement=True)
    usergroup_id = Column(BigInteger, nullable=False)
    menu_id = Column(BigInteger, nullable=False)
    _type = Column('type', String(3), nullable=False)
    f_menu_id = Column(BigInteger, nullable=False)
    menu_name = Column(String(100), nullable=False)
    menu_path = Column(String(100))
    menu_icon = Column(String(100))
    menu_index = Column(Integer, default=99, nullable=False)
