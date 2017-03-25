# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:28:01 2016

@author: huliqun
"""

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import reflection

from workserver.util import SysUtil
from workserver.util import GLBConfig
from workserver.module.models import User, UserFileInfo, OperatorInfo, UserLog, UserGroupInfo,MenuInfo,\
UserGroupMenu

# 为了解决mysql gone away尝试使用NullPool和设置POOL_RECYCLE为5s
#engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO, pool_recycle=POOL_RECYCLE, poolclass=NullPool)


def InitTables(engine):
    # delete all tables
    #Base.metadata.drop_all(engine)
    #create all tables
    #Base.metadata.create_all(engine)
    db = scoped_session(sessionmaker(bind=engine))
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    
    # determine if it needs to re-create the table.
        
    
    if 'tbl_user' not in tables:
        User.__table__.create(engine)
        
        user = User(userID = SysUtil.genUserID(),
                userName = 'admin',
                accountType = GLBConfig.ATYPE_ADMINISTRATOR,
                    password = 'admin',
                    email = 'test@example.com')
        db.add(user)
        db.commit()
    
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_userfileinfo' not in tables:
        UserFileInfo.__table__.create(engine)
        
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_usergroupinfo' not in tables:
        UserGroupInfo.__table__.create(engine)
        userGroupInfo = UserGroupInfo(userGroupType = GLBConfig.GTYPE_ADMINISTRATOR,
                                  userGroupName = 'Administrator')
        db.add(userGroupInfo)
        db.commit()
        
        
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_operatorinfo' not in tables:
        OperatorInfo.__table__.create(engine)
    
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_userlog' not in tables:
        UserLog.__table__.create(engine)
        
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_menuinfo' not in tables:
        MenuInfo.__table__.create(engine)
        
        db.add_all([
        MenuInfo(menuID = 1, menuType = '00', fMenuID = 0, menuName = '系统管理', menuPath = '', menuIcon = 'fa-cogs', menuIdx = 99),

        MenuInfo(menuType = '01', fMenuID = 1, menuName = '用户组维护', menuPath = '/system/groupControl', menuIcon = '', menuIdx = 1),
        MenuInfo(menuType = '01', fMenuID = 1, menuName = '菜单维护', menuPath = '/system/menuControl', menuIcon = '', menuIdx = 2),
        MenuInfo(menuType = '01', fMenuID = 1, menuName = '组菜单维护', menuPath = '/system/groupMenuControl', menuIcon = '', menuIdx = 3),
        MenuInfo(menuType = '01', fMenuID = 1, menuName = '操作员维护', menuPath = '/system/operatorControl', menuIcon = '', menuIdx = 4),
        ])
        db.commit()
        
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    if 'tbl_usergroupmenu' not in tables:
        UserGroupMenu.__table__.create(engine)
        userGroupInfo = db.query(UserGroupInfo).filter_by(userGroupName = 'Administrator').first()
        menu = db.query(MenuInfo).filter_by(menuName = '系统管理').first()
        userGroupMenu = UserGroupMenu(userGroupID = userGroupInfo.userGroupID,menuID = menu.menuID,menuType = menu.menuType,fMenuID  = menu.fMenuID,menuName = menu.menuName,menuPath = menu.menuPath, menuIcon = menu.menuIcon,menuIdx = menu.menuIdx)
        db.add(userGroupMenu)
        menu = db.query(MenuInfo).filter_by(menuName = '操作员维护').first()
        userGroupMenu = UserGroupMenu(userGroupID = userGroupInfo.userGroupID,menuID = menu.menuID,menuType = menu.menuType,fMenuID  = menu.fMenuID,menuName = menu.menuName,menuPath = menu.menuPath, menuIcon = menu.menuIcon,menuIdx = menu.menuIdx)
        db.add(userGroupMenu)
        menu = db.query(MenuInfo).filter_by(menuName = '用户组维护').first()
        userGroupMenu = UserGroupMenu(userGroupID = userGroupInfo.userGroupID,menuID = menu.menuID,menuType = menu.menuType,fMenuID  = menu.fMenuID,menuName = menu.menuName,menuPath = menu.menuPath, menuIcon = menu.menuIcon,menuIdx = menu.menuIdx)
        db.add(userGroupMenu)
        menu = db.query(MenuInfo).filter_by(menuName = '菜单维护').first()
        userGroupMenu = UserGroupMenu(userGroupID = userGroupInfo.userGroupID,menuID = menu.menuID,menuType = menu.menuType,fMenuID  = menu.fMenuID,menuName = menu.menuName,menuPath = menu.menuPath, menuIcon = menu.menuIcon,menuIdx = menu.menuIdx)
        db.add(userGroupMenu)
        menu = db.query(MenuInfo).filter_by(menuName = '组菜单维护').first()
        userGroupMenu = UserGroupMenu(userGroupID = userGroupInfo.userGroupID,menuID = menu.menuID,menuType = menu.menuType,fMenuID  = menu.fMenuID,menuName = menu.menuName,menuPath = menu.menuPath, menuIcon = menu.menuIcon,menuIdx = menu.menuIdx)
        db.add(userGroupMenu)
        db.commit()
    
if __name__ == '__main__':
    SysUtil.global_init()
    engine = SysUtil.get_engine_handle()
    def msg(msg, *args):
        msg = msg % args
        print("\n\n\n" + "-" * len(msg.split("\n")[0]))
        print(msg)
        print("-" * len(msg.split("\n")[0]))

    msg("Creating Tree Table:")

    InitTables(engine)