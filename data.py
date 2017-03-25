# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:28:01 2016

@author: huliqun
"""

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import reflection

from workserver.util import SysUtil
from workserver.util import GLBConfig
from workserver.module.models import Organization,User,UserImageInfo,OperatorInfo, PutBoxSettle, UserLog, PutterInfo,CarrierInfo,CarManagerInfo,\
UserGroupInfo,MenuInfo,MenuOrganizationRule,UserGroupMenu,TrunkList,BillLodingNoRule,PutBoxFeeRule,PreplanQueryWeb,ContainerYard,\
ShipCo2Yard,CarrierPara,BLN2CarrierMissmatch,EDIExportShipInfo,ShipCoInfo,Carrier2ShipCo,\
DriverInfo, CarInfo, TransportationList, TransportationPrint, GoodsInfo, FieldRelaInfo, PackInfo

# 为了解决mysql gone away尝试使用NullPool和设置POOL_RECYCLE为5s
#engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO, pool_recycle=POOL_RECYCLE, poolclass=NullPool)


def InitTables(engine):
    # delete all tables
    #Base.metadata.drop_all(engine)
    #create all tables
    #Base.metadata.create_all(engine)
    db = scoped_session(sessionmaker(bind=engine))
    tables = reflection.Inspector.from_engine(engine).get_table_names()
    
    default_category = 1
  
#	ABC货柜航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCABC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ABC', name='ABC货柜', helpMark='ABC', fullName='ABC货柜航运公司', enName='A.B.C CONTAINTER LINE')
    db.add(shipco) 
#	亚洲货柜航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCAEL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='AEL', name='亚洲货柜', helpMark='AEL', fullName='亚洲货柜航运有限公司', enName='ASIAN EXPRESS LINE LIMITED')
    db.add(shipco) 
#	安徽外运上海公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCAHWSH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='AHWSH', name='安徽外运', helpMark='AHWSH', fullName='安徽外运上海公司', enName='')
    db.add(shipco) 
#	亚利安佳航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCALI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ALI', name='亚利安佳', helpMark='ALI', fullName='亚利安佳航运公司', enName='ALIANCA NAVEGACAO E LOGISTICA LTDA.')
    db.add(shipco) 
#	澳洲国家航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCANL ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ANL ', name='澳航', helpMark='ANL ', fullName='澳洲国家航运有限公司', enName='AUSTRILIAN NATIONAL LINE')
    db.add(shipco) 
#	澳新直航（隶属英国康德轮船公司）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCANZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ANZ', name='澳新直航', helpMark='ANZ', fullName='澳新直航（隶属英国康德轮船公司）', enName='AUSTRALIAN - NEW ZEALAND')
    db.add(shipco) 
#	美国总统轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCAPL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='APL', name='美国总统', helpMark='APL', fullName='美国总统轮船（中国）有限公司', enName='AMERICAN PREDSIDENT LINES (CHINA)CO., LTD.')
    db.add(shipco) 
#	亚海航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCASL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ASL', name='亚海航运', helpMark='ASL', fullName='亚海航运有限公司', enName='ASEAN SEAS LINE CO.,LIMITED')
    db.add(shipco) 
#	亚海航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBAX',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BAX', name='亚海航运（中东线）', helpMark='BAX', fullName='亚海航运有限公司', enName='ASEAN SEAS LINE CO.,LIMITED')
    db.add(shipco) 
#	BBC船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBBC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BBC', name='BBC船务', helpMark='BBC', fullName='BBC船务有限公司', enName='BBC CHARTERING')
    db.add(shipco) 
#	东海船务公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBDS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BDS', name='东海船务', helpMark='BDS', fullName='东海船务公司', enName='BIEN DONG SHIPPING COMPANY')
    db.add(shipco) 
#	灯塔多式联运租赁公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBEA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BEA', name='灯塔联运', helpMark='BEA', fullName='灯塔多式联运租赁公司', enName='Beacon International Leasing, LLC')
    db.add(shipco) 
#	边行上海代表处
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBEN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BEN', name='边行', helpMark='BEN', fullName='边行上海代表处', enName='BEN LINE AGENCIES(CHINA)LTD.')
    db.add(shipco) 
#	巴拉奇船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BSL', name='巴拉奇船务', helpMark='BSL', fullName='巴拉奇船务有限公司', enName='BALAJI SHIPPING （U.K）LIMITED')
    db.add(shipco) 
#	孟虎航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBTL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BTL', name='孟虎航运', helpMark='BTL', fullName='孟虎航运公司', enName='BENGAL TIGER LINE LIMITED')
    db.add(shipco) 
#	百威华洋国际海运服务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCBWHY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='BWHY', name='百威华洋', helpMark='BWHY', fullName='百威华洋国际海运服务有限公司', enName='BARWIL HUAYANG SHIPPING SERVICE CO.,LTD.')
    db.add(shipco) 
#	崇明外代
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCAI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CAI', name='崇明外代', helpMark='CAI', fullName='崇明外代', enName='')
    db.add(shipco) 
#	美国CAI国际有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCAII',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CAII', name='美国CAI', helpMark='CAII', fullName='美国CAI国际有限公司', enName='CAI International Inc.')
    db.add(shipco) 
#	智利航运国际有限公司上海代表处
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCCNI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CCNI', name='智利航运', helpMark='CCNI', fullName='智利航运国际有限公司上海代表处', enName='COMPANIA CHILENA DE NAVEGACION INTEROCEANICA S.A.SHANGHAI REP.OFFICE')
    db.add(shipco) 
#	侨丰船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCHF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CHF', name='侨丰船务', helpMark='CHF', fullName='侨丰船务有限公司', enName='CHIAO FENG SHIPPING LTD.')
    db.add(shipco) 
#	中波轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCHP ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CHP ', name='中波轮船', helpMark='CHP ', fullName='中波轮船有限公司', enName='CHINESE-POLISH JOINT STOCK SHIPPING CO.')
    db.add(shipco) 
#	中日国际轮渡有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCJF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CJF', name='中日国际轮渡', helpMark='CJF', fullName='中日国际轮渡有限公司', enName='CHINA-JAPAN INTERNATIONAL FERRY CO.,LTD.')
    db.add(shipco) 
#	长江货代
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCJHD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CJHD', name='长江货代', helpMark='CJHD', fullName='长江货代', enName='')
    db.add(shipco) 
#	天敬海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCKS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CKS', name='天敬海运', helpMark='CKS', fullName='天敬海运株式会社', enName='CHUN KYUNG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	中通国际海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CL', name='中通海运', helpMark='CL', fullName='中通国际海运有限公司', enName='CENTRANS INTERNATIONAL MARINE SHIPPING CO.,LTD')
    db.add(shipco) 
#	中通国际海运有限公司（进口空箱）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCLD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CLD', name='中通海运（进口空箱）', helpMark='CLD', fullName='中通国际海运有限公司（进口空箱）', enName='CENTRANS INTERNATIONAL MARINE SHIPPING CO.,LTD')
    db.add(shipco) 
#	朝联货柜有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCLS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CLS', name='朝联货柜', helpMark='CLS', fullName='朝联货柜有限公司', enName='CHIU LUN CONTAINER CO.,LTD')
    db.add(shipco) 
#	法国达飞轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCMA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CMA', name='法国达飞', helpMark='CMA', fullName='法国达飞轮船（中国）有限公司', enName='CMA CGM (CHINA) SHIPPING CO., LTD')
    db.add(shipco) 
#	招商货柜航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCMCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CMCL', name='招商货柜', helpMark='CMCL', fullName='招商货柜航运有限公司', enName='CHINA MERCHANTS CO.,LTD.')
    db.add(shipco) 
#	英国康德轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCML',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CML', name='英国康德', helpMark='CML', fullName='英国康德轮船有限公司', enName='CP.SHIPS (UK) LTD.')
    db.add(shipco) 
#	正利航业股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCNC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CNC', name='正利航业', helpMark='CNC', fullName='正利航业股份有限公司', enName='CHENG LIE NAVIGATION CO.,LTD.')
    db.add(shipco) 
#	科斯塔集装箱运输公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCNL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CNL', name='科斯塔', helpMark='CNL', fullName='科斯塔集装箱运输公司', enName='COSTA CONTAINER LINES')
    db.add(shipco) 
#	上海航华国际船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCNSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CNSL', name='航华船代', helpMark='CNSL', fullName='上海航华国际船务代理有限公司', enName='CHINA SAILING INTERNATIONAL SHIPPING AGENCY LTD.')
    db.add(shipco) 
#	京汉航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCOH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='COH', name='京汉航运', helpMark='COH', fullName='京汉航运有限公司', enName='COHEUNG MARINE SHIPPING CO.,LTD')
    db.add(shipco) 
#	中印海洋运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCOL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='COL', name='中印海运', helpMark='COL', fullName='中印海洋运输有限公司', enName='CHINA OCEAN LINE PTE,LTD.')
    db.add(shipco) 
#	中远集装箱运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCOSCO',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='COSCO', name='中远', helpMark='COSCO', fullName='中远集装箱运输有限公司', enName='COSCO CONTRAINER LINES CO.,LTD.')
    db.add(shipco) 
#	CP轮船（美国）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCPP',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CPP', name='CP轮船（美国）', helpMark='CPP', fullName='CP轮船（美国）', enName='CP SHIPS(USA). LLC')
    db.add(shipco) 
#	CP轮船（英国）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCPS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CPS', name='CP轮船（英国）', helpMark='CPS', fullName='CP轮船（英国）', enName='CP SHIPS(UK). LTD')
    db.add(shipco) 
#	上海华港国际船舶代理
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCPSA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CPSA', name='华港船代', helpMark='CPSA', fullName='上海华港国际船舶代理', enName='CHINA PORTS INTERNATIONAL SHIPPING AGENCY')
    db.add(shipco) 
#	重庆长江轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCQCJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CQCJ', name='重庆长江轮船', helpMark='CQCJ', fullName='重庆长江轮船有限公司', enName='')
    db.add(shipco) 
#	重庆市海运有限责任公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCQS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CQS', name='重庆海运', helpMark='CQS', fullName='重庆市海运有限责任公司', enName='CHONGQING MARINE SHIPPING CO.,LTD.')
    db.add(shipco) 
#	联华航业有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCRN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CRN', name='联华航业', helpMark='CRN', fullName='联华航业有限公司', enName='CHRINA OVERSEAS COMPANY LTD')
    db.add(shipco) 
#	中海集装箱运输股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSC', name='中海（CSCO、CSCF）', helpMark='CSC', fullName='中海集装箱运输股份有限公司', enName='CHINA SHIPPING CONTAINER LINES CO., LTD.')
    db.add(shipco) 
#	中远集运东南亚有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSE', name='中远东南亚', helpMark='CSE', fullName='中远集运东南亚有限公司', enName='COSCO CONTAINER LINES SOUTH EAST ASIA PTE. LTD.')
    db.add(shipco) 
#	康世海运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSH', name='康世海运', helpMark='CSH', fullName='康世海运', enName='CONTSHIP CN LINE')
    db.add(shipco) 
#	洋浦中诚联合航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSL', name='洋浦中诚', helpMark='CSL', fullName='洋浦中诚联合航运有限公司', enName='CHINA UNITED LINES LTD.')
    db.add(shipco) 
#	中诚联合航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSS', name='中诚航运', helpMark='CSS', fullName='中诚联合航运有限公司', enName='CULINE---CHINA UNITED LINE LTD.')
    db.add(shipco) 
#	宝华海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCST',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CST', name='宝华海运', helpMark='CST', fullName='宝华海运股份有限公司', enName='COASTAL NAVIGATION CO.,Ltd.')
    db.add(shipco) 
#	南美轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSV',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSV', name='南美轮船', helpMark='CSV', fullName='南美轮船（中国）有限公司', enName='CSAV NORASIA GROUP（CHINA) SHIPPING CO.,LTD.')
    db.add(shipco) 
#	山东省烟台国际海运公司内贸商品空箱
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSY', name='烟台海运内贸空箱', helpMark='CSY', fullName='山东省烟台国际海运公司内贸商品空箱', enName='SHANDONG PROVINCE YANTAI INTERNATIONAL MARINE SHIPPING CO.')
    db.add(shipco) 
#	山东省烟台国际海运公司内贸部
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCSYM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CSYM', name='烟台海运内贸', helpMark='CSYM', fullName='山东省烟台国际海运公司内贸部', enName='SHANDONG PROVINCE YANTAI INTERNATIONAL MARINE SHIPPING CO.')
    db.add(shipco) 
#	洋浦中诚联合航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCUL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CUL', name='洋浦中诚', helpMark='CUL', fullName='洋浦中诚联合航运有限公司', enName='CHINA UNITED LINES LTD.')
    db.add(shipco) 
#	上海长洋航业有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CY', name='长洋航业', helpMark='CY', fullName='上海长洋航业有限公司', enName='')
    db.add(shipco) 
#	朝阳航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCCYSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='CYSL', name='朝阳航运', helpMark='CYSL', fullName='朝阳航运有限公司', enName='CHO YANG SHIPPING LINES')
    db.add(shipco) 
#	丹东国际集装箱储运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDIC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DIC', name='丹东集运', helpMark='DIC', fullName='丹东国际集装箱储运有限公司', enName='')
    db.add(shipco) 
#	东进商船株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDJN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DJN', name='东进商船', helpMark='DJN', fullName='东进商船株式会社', enName='DONGJIN SHIPPING CO., LTD.')
    db.add(shipco) 
#	法国达贸轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDMS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DMS', name='法国达贸', helpMark='DMS', fullName='法国达贸轮船有限公司', enName='DELMAS')
    db.add(shipco) 
#	东南亚海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDNA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DNA', name='东南亚海运', helpMark='DNA', fullName='东南亚海运株式会社', enName='DONAGNAMA SHIPPING CO.,LTD.')
    db.add(shipco) 
#	都乐（上海）水果蔬菜贸易有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDOLE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DOLE', name='都乐', helpMark='DOLE', fullName='都乐（上海）水果蔬菜贸易有限公司', enName='DOLE (SHANGHAI) FRUITS AND VEGETABLES TRADING CO.,LTD.')
    db.add(shipco) 
#	东映海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DY', name='东映海运', helpMark='DY', fullName='东映海运株式会社', enName='PEGASUS CONTAINER SERVICE')
    db.add(shipco) 
#	东映自备箱
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCDYWW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='DYWW', name='东映自备箱', helpMark='DYWW', fullName='东映自备箱', enName='')
    db.add(shipco) 
#	达通国际航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCEAS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='EAS', name='达通航运', helpMark='EAS', fullName='达通国际航运有限公司', enName='EAS INTERNATIONAL SHIPPING CO., LTD')
    db.add(shipco) 
#	新欧亚航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCECS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ECS', name='新欧亚', helpMark='ECS', fullName='新欧亚航运有限公司', enName='N-EXPRESS L.L.C')
    db.add(shipco) 
#	德国奥登道夫
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCEOLD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='EOLD', name='奥登道夫', helpMark='EOLD', fullName='德国奥登道夫', enName='OLDENDORFF CARRIERS GMBH & CO.KG')
    db.add(shipco) 
#	先锋海运私人有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCEPC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='EPC', name='先锋海运', helpMark='EPC', fullName='先锋海运私人有限公司', enName='EP CARRIERS PTE LTD')
    db.add(shipco) 
#	香港阿联酋船务(中国)有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCESL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ESL', name='香港阿联酋船务', helpMark='ESL', fullName='香港阿联酋船务(中国)有限公司', enName='EMIRATES SHIPPING AGENCIES(CHINA)LIMITED')
    db.add(shipco) 
#	香港阿联酋船务(中国)有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCESL1',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ESL1', name='香港阿联酋船务', helpMark='ESL1', fullName='香港阿联酋船务(中国)有限公司', enName='EMIRATES SHIPPING AGENCIES(CHINA)LIMITED')
    db.add(shipco) 
#	香港阿联酋船务(中国)有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCESL2',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ESL2', name='香港阿联酋船务', helpMark='ESL2', fullName='香港阿联酋船务(中国)有限公司', enName='EMIRATES SHIPPING AGENCIES(CHINA)LIMITED')
    db.add(shipco) 
#	香港阿联酋船务(中国)有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCESL3',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ESL3', name='香港阿联酋船务', helpMark='ESL3', fullName='香港阿联酋船务(中国)有限公司', enName='EMIRATES SHIPPING AGENCIES(CHINA)LIMITED')
    db.add(shipco) 
#	埃塞俄比亚国家航运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCESLSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ESLSC', name='埃塞俄比亚航运', helpMark='ESLSC', fullName='埃塞俄比亚国家航运', enName='ETHIOPIAN SHIPPING LINES & BEIJIN')
    db.add(shipco) 
#	长荣海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCEVG',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='EVG', name='长荣', helpMark='EVG', fullName='长荣海运股份有限公司', enName='EVERGREEN MARINE CORP. LTD.')
    db.add(shipco) 
#	汉堡南美泛澳航线
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFHS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FHS', name='汉堡南美泛澳航线', helpMark='FHS', fullName='汉堡南美泛澳航线', enName='FESCO AUSTRALIA NEW ZEALAND LINER')
    db.add(shipco) 
#	佛罗伦集装箱服务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFLR',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FLR', name='佛罗伦集箱', helpMark='FLR', fullName='佛罗伦集装箱服务有限公司', enName='Florens Container Services Company Ltd. ')
    db.add(shipco) 
#	自由箱
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFREE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FREE', name='自由箱', helpMark='FREE', fullName='自由箱', enName='FREE USE')
    db.add(shipco) 
#	俄罗斯远东海洋轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FSC', name='俄罗斯远东', helpMark='FSC', fullName='俄罗斯远东海洋轮船有限公司', enName='FAR EASTERN SHIPPING CO.,LTD.')
    db.add(shipco) 
#	富腾船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFTI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FTI', name='富腾船务', helpMark='FTI', fullName='富腾船务有限公司', enName='FIEET TRANS INTERNATIONAL LTD')
    db.add(shipco) 
#	浩达船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFWS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FWS', name='浩达船务', helpMark='FWS', fullName='浩达船务有限公司', enName='FAIRWIND SHIPPING CO.,LTD')
    db.add(shipco) 
#	友航轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCFWSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='FWSL', name='友航轮船', helpMark='FWSL', fullName='友航轮船有限公司', enName='FAIRWEATHER STEAMSHIP CO.,LTD')
    db.add(shipco) 
#	吉与宝有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGB',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GB', name='吉与宝', helpMark='GB', fullName='吉与宝有限公司', enName='GEARBULK AG ')
    db.add(shipco) 
#	大新华轮船（烟台）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGCS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GCS', name='大新华轮船', helpMark='GCS', fullName='大新华轮船（烟台）有限公司', enName='GRAND CHINA SHIPPING (YANTAI) CO.,LTD')
    db.add(shipco) 
#	Seacoglobal Leasing, LLC
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGES',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GES', name='新加坡SEACO', helpMark='GES', fullName='Seacoglobal Leasing, LLC', enName='新加坡SEACO国际有限公司')
    db.add(shipco) 
#	金发船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GF', name='金发船务', helpMark='GF', fullName='金发船务有限公司', enName='GOLDEN FORTUNE SHIPPING CO.,LTD.')
    db.add(shipco) 
#	格兰远东航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGIL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GIL', name='格兰远东', helpMark='GIL', fullName='格兰远东航运有限公司', enName='GARANT INTERMODAL LTD.')
    db.add(shipco) 
#	大众海运有限公司（美国）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGMA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GMA', name='大众海运（美国）', helpMark='GMA', fullName='大众海运有限公司（美国）', enName='GENERAL MARITIME AGENCY INC')
    db.add(shipco) 
#	美国海湾航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGPL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GPL', name='美国海湾航运', helpMark='GPL', fullName='美国海湾航运有限公司', enName='GULF PACIFIC LINE')
    db.add(shipco) 
#	金星轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GSL', name='金星轮船', helpMark='GSL', fullName='金星轮船有限公司', enName='GOLD STAR LINE LTD.')
    db.add(shipco) 
#	大南航运（澳大利亚）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGSS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GSS', name='大南航运', helpMark='GSS', fullName='大南航运（澳大利亚）有限公司', enName='Great Southern Shipping Australia Pty Ltd')
    db.add(shipco) 
#	美国大西北汽船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGWS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GWS', name='美国大西北汽船', helpMark='GWS', fullName='美国大西北汽船公司', enName='GREAT WESTERN STEAMSHIP COMPANY')
    db.add(shipco) 
#	俄罗斯戈尔诺萨沃思克航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCGZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='GZ', name='俄罗斯戈尔诺萨沃思克', helpMark='GZ', fullName='俄罗斯戈尔诺萨沃思克航运公司', enName='GORNOZAVODSK SHIPPING COMPANY')
    db.add(shipco) 
#	宁波外运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHAI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HAI', name='宁波外运', helpMark='HAI', fullName='宁波外运', enName='')
    db.add(shipco) 
#	兴亚海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHAL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HAL', name='兴亚海运', helpMark='HAL', fullName='兴亚海运株式会社', enName='HEUNG-A SHIPPING CO.,LTD.')
    db.add(shipco) 
#	上海海华轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHAS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HAS', name='上海海华', helpMark='HAS', fullName='上海海华轮船有限公司', enName='SHANGHAI HAI HUA SHIPPING CO., LTD')
    db.add(shipco) 
#	珲春创力海运物流有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHCCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HCCL', name='珲春创力', helpMark='HCCL', fullName='珲春创力海运物流有限公司', enName='HUNCHUN CHUANGLI SHIPPING LOGISTICS CO.LTD')
    db.add(shipco) 
#	观海船务
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHDS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HDS', name='观海船务', helpMark='HDS', fullName='观海船务', enName='HAFIZ DARYA SHIPPING COMPANY（FOR CARRIER OWN UNIT）')
    db.add(shipco) 
#	观海船务（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHDSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HDSL', name='观海船务（租）', helpMark='HDSL', fullName='观海船务（租）', enName='HAFIZ DARYA SHIPPING COMPANYHDSL（FOR LEASED UNIT）')
    db.add(shipco) 
#	上海海富国际集装箱货运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHFL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HFL', name='上海海富货运', helpMark='HFL', fullName='上海海富国际集装箱货运有限公司', enName='')
    db.add(shipco) 
#	华钢
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHG',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HG', name='华钢', helpMark='HG', fullName='华钢', enName='')
    db.add(shipco) 
#	上海海华轮船有限公司沿海内支线
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHHA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HHA', name='海华内支线', helpMark='HHA', fullName='上海海华轮船有限公司沿海内支线', enName='COASTAL FEEDER SECTION OF SHANGHAI HAI HUA SHIPPING CO., LTD')
    db.add(shipco) 
#	韩进海运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHJS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HJS', name='韩进海运', helpMark='HJS', fullName='韩进海运（中国）有限公司', enName='HANJIN SHIPPING(CHINA)CO., LTD.')
    db.add(shipco) 
#	东方船务（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHKS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HKS', name='东方船务', helpMark='HKS', fullName='东方船务（中国）有限公司', enName='HONG KONG AND EASTERN SHIPPING AGENCIES LTD.')
    db.add(shipco) 
#	赫伯罗特船务（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHLC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HLC', name='赫伯罗特', helpMark='HLC', fullName='赫伯罗特船务（中国）有限公司', enName='HAPAG-LLOYD (CHINA) SHIPPING LIMITED')
    db.add(shipco) 
#	青岛海隆达物流有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHLD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HLD', name='海隆达物流', helpMark='HLD', fullName='青岛海隆达物流有限公司上海分公司', enName='CHINA HI-LANDER LINE SHANGHAI BRANCH')
    db.add(shipco) 
#	港业航运（香港）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHLK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HLK', name='港业航运', helpMark='HLK', fullName='港业航运（香港）有限公司', enName='HARBOUR-LINK LINES（HK）LTD.')
    db.add(shipco) 
#	英国荣昇海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHML',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HML', name='英国荣昇', helpMark='HML', fullName='英国荣昇海运有限公司', enName='HATSU MARINE LIMITED')
    db.add(shipco) 
#	现代商船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHMM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HMM', name='现代商船', helpMark='HMM', fullName='现代商船（中国）有限公司', enName='HYUNDAI MERCHANT MARINE LTD.')
    db.add(shipco) 
#	湖南远洋运输公司 
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHNYY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HNYY', name='湖南远洋', helpMark='HNYY', fullName='湖南远洋运输公司 ', enName='')
    db.add(shipco) 
#	河北远洋船舶代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHOS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HOS', name='河北远洋', helpMark='HOS', fullName='河北远洋船舶代理有限公司', enName='Hebei Ocean Shipping Agency Ltd')
    db.add(shipco) 
#	美国海天航运有限责任公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHRZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HRZ', name='美国海天', helpMark='HRZ', fullName='美国海天航运有限责任公司', enName='HORIZON LINES,LLC.')
    db.add(shipco) 
#	汉堡南美航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHSD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HSD', name='汉堡南美', helpMark='HSD', fullName='汉堡南美航运公司', enName='HAMBURG SUDAMERIKANISCHE DAMPFSCHIFFFAHRTS-GESELLSCHAFT KG')
    db.add(shipco) 
#	韩星海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHSLI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HSLI', name='韩星海运', helpMark='HSLI', fullName='韩星海运株式会社', enName='HANSUNG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	德利航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHUB',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HUB', name='德利航运', helpMark='HUB', fullName='德利航运有限公司', enName='HUB SHIPPING SDN BHD')
    db.add(shipco) 
#	海文航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCHW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='HW', name='海文航运', helpMark='HW', fullName='海文航运有限公司', enName='HAI WIN SHIPPING HK.CO')
    db.add(shipco) 
#	运达航运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCIAL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='IAL', name='运达航运', helpMark='IAL', fullName='运达航运股份有限公司', enName='INTERASIA LINES LTD.')
    db.add(shipco) 
#	爱尔全球集装箱服务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCICL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ICL', name='爱尔全球', helpMark='ICL', fullName='爱尔全球集装箱服务有限公司', enName='IAL CONTAINER LINE (H.K.),LTD.')
    db.add(shipco) 
#	全美集装箱货柜有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCICS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ICS', name='全美货柜', helpMark='ICS', fullName='全美集装箱货柜有限公司', enName='')
    db.add(shipco) 
#	印达斯集装箱航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCIDL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='IDL', name='印达斯', helpMark='IDL', fullName='印达斯集装箱航运有限公司', enName='Indus Container Lines Pvt Ltd.')
    db.add(shipco) 
#	伊朗航运（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCIRN+',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='IRN+', name='伊朗航运租箱', helpMark='IRN+', fullName='伊朗航运（租）', enName='')
    db.add(shipco) 
#	伊朗伊斯兰共和国航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCIRNL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='IRNL', name='伊朗航运', helpMark='IRNL', fullName='伊朗伊斯兰共和国航运公司', enName='ISLAMIC REPUBLIC OF IRAN SHIPPING LINES')
    db.add(shipco) 
#	英之杰航运（香港）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCISS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ISS', name='英之杰', helpMark='ISS', fullName='英之杰航运（香港）有限公司', enName='INCHCAPE SHIPPING SERVICES')
    db.add(shipco) 
#	嘉宏船代
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JH', name='嘉宏船代', helpMark='JH', fullName='嘉宏船代', enName='JH')
    db.add(shipco) 
#	上海集海航运有限公司（内贸）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJHHY ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JHHY ', name='上海集海航运（内贸）', helpMark='JHHY ', fullName='上海集海航运有限公司（内贸）', enName='SHANGHAI JIHAI SHIPPING CO.,LTD.')
    db.add(shipco) 
#	捷杰航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJNJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JNJ', name='捷杰航运', helpMark='JNJ', fullName='捷杰航运有限公司', enName='J&J SHIPPING')
    db.add(shipco) 
#	日本安通国际株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJOT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JOT', name='日本安通', helpMark='JOT', fullName='日本安通国际株式会社', enName='ONTO SHIPPING INT L INC.')
    db.add(shipco) 
#	江苏海洋运输公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJSM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JSM', name='江苏海洋运输', helpMark='JSM', fullName='江苏海洋运输公司', enName='JIANGSU MARINE SHIPPING CO.')
    db.add(shipco) 
#	江苏苏亚
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCJSSY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='JSSY', name='江苏苏亚', helpMark='JSSY', fullName='江苏苏亚', enName='')
    db.add(shipco) 
#	神原汽船
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCKKC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='KKC', name='神原汽船', helpMark='KKC', fullName='神原汽船', enName='KAMBARA KISEN CO.,LTD.')
    db.add(shipco) 
#	川崎汽船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCKL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='KL', name='川崎汽船', helpMark='KL', fullName='川崎汽船（中国）有限公司', enName='KAWASAKI KISEN KAISHA LTD.')
    db.add(shipco) 
#	川崎汽船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCKLA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='KLA', name='川崎汽船', helpMark='KLA', fullName='川崎汽船（中国）有限公司', enName='KAWASAKI KISEN KAISHA LTD.')
    db.add(shipco) 
#	高丽海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCKMT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='KMT', name='高丽海运', helpMark='KMT', fullName='高丽海运株式会社', enName='KOREA MARINE TRANSPORT CO.,LTD.')
    db.add(shipco) 
#	联杰海运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCLJHY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='LJHY', name='联杰海运', helpMark='LJHY', fullName='联杰海运', enName='')
    db.add(shipco) 
#	意大利邮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCLT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='LT', name='意大利邮船', helpMark='LT', fullName='意大利邮船公司', enName='LLOYD TRIESTINO DI NAVIGAZIONE S.P.A.')
    db.add(shipco) 
#	美国莱克斯轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCLYK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='LYK', name='美国莱克斯', helpMark='LYK', fullName='美国莱克斯轮船有限公司', enName='LYKES LINES LTD.')
    db.add(shipco) 
#	马鲁巴航运有限公司（南美邮船）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMAR',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MAR', name='马鲁巴航运', helpMark='MAR', fullName='马鲁巴航运有限公司（南美邮船）', enName='MARUBA SHIPPING')
    db.add(shipco) 
#	美森轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMAT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MAT', name='美森轮船', helpMark='MAT', fullName='美森轮船有限公司', enName='MATSON NAVIGATION COMPANY,INC')
    db.add(shipco) 
#	海威航运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMAX',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MAX', name='海威航运', helpMark='MAX', fullName='海威航运', enName='MAXICON CONTAINER LINE.')
    db.add(shipco) 
#	卡朋特航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMBF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MBF', name='卡朋特航运', helpMark='MBF', fullName='卡朋特航运有限公司', enName='MBF CARPENTERS SHIPPING LIMITED')
    db.add(shipco) 
#	MCC运输新加坡有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMCC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MCC', name='MCC运输', helpMark='MCC', fullName='MCC运输新加坡有限公司', enName='MCC TRANSPORT')
    db.add(shipco) 
#	东方国际
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MCL', name='东方国际', helpMark='MCL', fullName='东方国际', enName='')
    db.add(shipco) 
#	迈捷箱运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMCLU',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MCLU', name='迈捷箱运', helpMark='MCLU', fullName='迈捷箱运公司', enName='MAGISTRAL CONTAINER LINES')
    db.add(shipco) 
#	澳大利亚海胜船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMCS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MCS', name='海胜船务', helpMark='MCS', fullName='澳大利亚海胜船务有限公司', enName='MERCHANT SHIPPING')
    db.add(shipco) 
#	法国达飞轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMDV',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MDV', name='法国达飞', helpMark='MDV', fullName='法国达飞轮船（中国）有限公司', enName='CMA CGM (CHINA) SHIPPING CO.,LTD.')
    db.add(shipco) 
#	玛丽亚那班轮私人有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMEL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MEL', name='玛丽亚那班轮', helpMark='MEL', fullName='玛丽亚那班轮私人有限公司', enName='MARIANA EXPRESS LINES PTE LTD')
    db.add(shipco) 
#	铭鸿船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MH', name='铭鸿船务', helpMark='MH', fullName='铭鸿船务有限公司', enName='MENGHORNG SHIPPING LTD.')
    db.add(shipco) 
#	马来西亚国际航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMISC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MISC', name='马来西亚', helpMark='MISC', fullName='马来西亚国际航运有限公司', enName='MALAYSIA INTERNATIONAL SHIPPING CORPN BHD.')
    db.add(shipco) 
#	丰年航业（香港）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMLL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MLL', name='丰年航业', helpMark='MLL', fullName='丰年航业（香港）有限公司', enName='MAINLAND NAVIGATION (HONGKONG) CO., LIMITED')
    db.add(shipco) 
#	商船三井（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMOL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MOL', name='商船三井', helpMark='MOL', fullName='商船三井（中国）有限公司', enName='MITSUI OSAKA LINES (CHINA) CO., LTD')
    db.add(shipco) 
#	瑞士地中海航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MSC', name='瑞士地中海', helpMark='MSC', fullName='瑞士地中海航运有限公司', enName='MEDITERRANEAN SHIPPING COMPANY S.A.')
    db.add(shipco) 
#	马士基（中国）航运有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMSK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MSK', name='马士基', helpMark='MSK', fullName='马士基（中国）航运有限公司上海分公司', enName='MAERSK(CHINA) SHIPPING CO.,LTD.SHANGHAI BRANCH')
    db.add(shipco) 
#	民生轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MSL', name='民生', helpMark='MSL', fullName='民生轮船有限公司', enName='MINSHENG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	明达航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMTN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MTN', name='明达航运', helpMark='MTN', fullName='明达航运有限公司', enName='MING TAT NAVIGATION LTD.')
    db.add(shipco) 
#	海威箱运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCMXC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='MXC', name='海威箱运', helpMark='MXC', fullName='海威箱运', enName='MAXICON CONTAINER LINE.')
    db.add(shipco) 
#	宁波远洋运输有限公司（日本航线）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNBOS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NBOS', name='宁波远洋运输（日本航线）', helpMark='NBOS', fullName='宁波远洋运输有限公司（日本航线）', enName='NINGBO OCEAN SHIPPING CO.,LTD')
    db.add(shipco) 
#	尼罗河航运私有有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNDS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NDS', name='尼罗河航运', helpMark='NDS', fullName='尼罗河航运私有有限公司', enName='NILE DUTCH AFRICA LINE B.V.')
    db.add(shipco) 
#	渣华邮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNEDL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NEDL', name='渣华邮船', helpMark='NEDL', fullName='渣华邮船公司', enName='NEDLLOYD LINES')
    db.add(shipco) 
#	新海航业有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNEHU',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NEHU', name='新海航业', helpMark='NEHU', fullName='新海航业有限公司', enName='NEWSEAS NAVIGATION CORP')
    db.add(shipco) 
#	俄罗斯萨哈林航运有限公司（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNEW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NEW', name='萨哈林航运（租）', helpMark='NEW', fullName='俄罗斯萨哈林航运有限公司（租）', enName='SAKHALIN SHIPPING COMPANY')
    db.add(shipco) 
#	东方海皇轮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNOL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NOL', name='东方海皇', helpMark='NOL', fullName='东方海皇轮船公司', enName='NEPTUNE ORIENT LINE LTD.')
    db.add(shipco) 
#	北欧亚航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNOR',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NOR', name='北欧亚', helpMark='NOR', fullName='北欧亚航运有限公司', enName='NORASIA CONTAINER LINES LTD.')
    db.add(shipco) 
#	新东船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNOS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NOS', name='新东船务', helpMark='NOS', fullName='新东船务有限公司', enName='NEW ORIENT SHIPPING LTD.')
    db.add(shipco) 
#	新太平洋航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNPL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NPL', name='新太平洋航运', helpMark='NPL', fullName='新太平洋航运有限公司', enName='NEW PACIFIC LINE')
    db.add(shipco) 
#	南青集装箱班轮公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNQ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NQ', name='南青班轮', helpMark='NQ', fullName='南青集装箱班轮公司', enName='NANQING CONTAINER LINES CO.')
    db.add(shipco) 
#	南星海运株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NS', name='南星海运', helpMark='NS', fullName='南星海运株式会社', enName='NAMSUNG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	沙特阿拉伯国际航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NSC', name='沙特阿拉伯', helpMark='NSC', fullName='沙特阿拉伯国际航运有限公司', enName='NATIONAL SHIPPING CO. OF SAUDI ARABIA')
    db.add(shipco) 
#	宁波远洋运输有限公司（仁川航线）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNSI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NSI', name='宁波远洋运输（仁川航线）', helpMark='NSI', fullName='宁波远洋运输有限公司（仁川航线）', enName='NINGBO OCEAN SHIPPING CO.,LTD')
    db.add(shipco) 
#	日本邮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNYK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NYK', name='日本邮船', helpMark='NYK', fullName='日本邮船（中国）有限公司', enName='NIPPON YUSEN KAISHA LINE LTD.')
    db.add(shipco) 
#	新西兰航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNZL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NZL', name='新西兰航运', helpMark='NZL', fullName='新西兰航运有限公司', enName='Newzealand shipping co.,ltd.')
    db.add(shipco) 
#	新西兰快航
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCNZUE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='NZUE', name='新西兰快航', helpMark='NZUE', fullName='新西兰快航', enName='NEW ZEALAND UUITED EXPRESS')
    db.add(shipco) 
#	上海安通船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCONT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ONT', name='安通船务', helpMark='ONT', fullName='上海安通船务代理有限公司', enName='')
    db.add(shipco) 
#	东方海外货柜航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCOOCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='OOCL', name='东方海外', helpMark='OOCL', fullName='东方海外货柜航运（中国）有限公司', enName='ORIENT OVERSEAS CONTAINER LINE LTD.')
    db.add(shipco) 
#	东方海外货柜航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCOOL1',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='OOL1', name='东方海外', helpMark='OOL1', fullName='东方海外货柜航运（中国）有限公司', enName='ORIENT OVERSEAS CONTAINER LINE LTD.')
    db.add(shipco) 
#	东方海外货柜航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCOOL2',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='OOL2', name='东方海外', helpMark='OOL2', fullName='东方海外货柜航运（中国）有限公司', enName='ORIENT OVERSEAS CONTAINER LINE LTD.')
    db.add(shipco) 
#	葩亚集装箱航运私人有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPAC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PAC', name='葩亚', helpMark='PAC', fullName='葩亚集装箱航运私人有限公司', enName='PACC CONTAINER LINE PTE. LTD.')
    db.add(shipco) 
#	上海泛亚航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPAN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PAN', name='泛亚航运', helpMark='PAN', fullName='上海泛亚航运有限公司', enName='SHANGHAI PANASIA SHIPPING CO.,LTD.')
    db.add(shipco) 
#	哥伦比亚航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPAS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PAS', name='哥伦比亚', helpMark='PAS', fullName='哥伦比亚航运有限公司', enName='NEW PACIFIC')
    db.add(shipco) 
#	泛州海运株式会社（汎洲、凡洲）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPCS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PCS', name='泛州海运', helpMark='PCS', fullName='泛州海运株式会社（汎洲、凡洲）', enName='PAN CONTINENTAL SHIPPING CO.,LTD.')
    db.add(shipco) 
#	马来西亚大众海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPDZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PDZ', name='马来西亚大众海运', helpMark='PDZ', fullName='马来西亚大众海运有限公司', enName='PERKAPALAN DAI ZHUN SDN.BHD.')
    db.add(shipco) 
#	巴拿马环球轮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPGST',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PGST', name='巴拿马环球轮船', helpMark='PGST', fullName='巴拿马环球轮船公司', enName='PANAMA/GLOBE STEAMER LINES.S.A')
    db.add(shipco) 
#	上海浦海航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PH', name='浦海航运', helpMark='PH', fullName='上海浦海航运有限公司', enName='SHANGHAI PUHAI SHIPPING CO., LTD.')
    db.add(shipco) 
#	上海浦海航运（香港）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPHL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PHL', name='浦海香港', helpMark='PHL', fullName='上海浦海航运（香港）有限公司', enName='SHANGHAI PUHAI SHIPPING(HONGKONG) CO.,LTD.')
    db.add(shipco) 
#	太平船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPIL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PIL', name='太平船务', helpMark='PIL', fullName='太平船务有限公司', enName='PACIFIC INTERNATIONAL LINES LTD')
    db.add(shipco) 
#	太平船务（中国）有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPIL1',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PIL1', name='太平船务', helpMark='PIL1', fullName='太平船务（中国）有限公司上海分公司', enName='Pacific International Line(China)Ltd. Shanghai Branch')
    db.add(shipco) 
#	泛韩物流
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPKE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PKE', name='泛韩物流', helpMark='PKE', fullName='泛韩物流', enName='PAN KOREA LOGISTICS')
    db.add(shipco) 
#	帕尔马海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPMA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PMA', name='帕尔马海运', helpMark='PMA', fullName='帕尔马海运有限公司', enName='PERMA SHIPPING LINE PTE. LTD.')
    db.add(shipco) 
#	巴基斯坦海运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPNSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PNSC', name='巴基斯坦', helpMark='PNSC', fullName='巴基斯坦海运公司', enName='PAKISTAN SHIPPING CORPORATION')
    db.add(shipco) 
#	世腾（中国）船务服务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPOL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='POL', name='世腾船务', helpMark='POL', fullName='世腾（中国）船务服务有限公司', enName='PAN OCEAN SHIPPING CO., LTD.')
    db.add(shipco) 
#	铁行渣华（中国）船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPON',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PON', name='铁行渣华', helpMark='PON', fullName='铁行渣华（中国）船务有限公司', enName='P&O NEDLLOYD (CHINA) LTD.')
    db.add(shipco) 
#	海南泛洋航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPOS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='POS', name='海南泛洋', helpMark='POS', fullName='海南泛洋航运有限公司', enName='HAINAN PAN OCEAN SHIPPING CO.,LTD.')
    db.add(shipco) 
#	波塞冬航运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPSDN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PSDN', name='波塞冬航运', helpMark='PSDN', fullName='波塞冬航运', enName='POSEIDON SHIPPING CO.LTD.')
    db.add(shipco) 
#	釜山远洋
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PSL', name='釜山远洋', helpMark='PSL', fullName='釜山远洋', enName='PUSAN SHIPPING CO., LTD.')
    db.add(shipco) 
#	宝威船务有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCPWK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='PWK', name='宝威船务', helpMark='PWK', fullName='宝威船务有限公司上海分公司', enName='POWICK SHIPPING LIMITED REPRESENTATIVE OFFICE')
    db.add(shipco) 
#	青岛海运诺扬航运有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCQNS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='QNS', name='诺扬航运上海', helpMark='QNS', fullName='青岛海运诺扬航运有限公司上海分公司', enName='QINGDAO MARINE NOAH S ARK SHIPPING CO.,LTD.SHANGHAI BRANCH')
    db.add(shipco) 
#	全通（天津）实业有限公司上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCQTSH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='QTSH', name='全通上海', helpMark='QTSH', fullName='全通（天津）实业有限公司上海分公司', enName='ZEN CONTINENTAL(TIANJIN)ENTERPRISES CO.,LTD.SHANGHAI BRANCH')
    db.add(shipco) 
#	俄亚海洋轮船运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCRACL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='RACL', name='俄亚海运', helpMark='RACL', fullName='俄亚海洋轮船运输有限公司', enName='RASIACON LIMITED')
    db.add(shipco) 
#	俄亚海洋轮船运输有限公司（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCRACZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='RACZ', name='俄亚海运（租）', helpMark='RACZ', fullName='俄亚海洋轮船运输有限公司（租）', enName='RASIACON LIMITED')
    db.add(shipco) 
#	宏海箱运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCRCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='RCL', name='宏海箱运', helpMark='RCL', fullName='宏海箱运有限公司', enName='REGIONAL CONTAINER LINES PTE LTD.')
    db.add(shipco) 
#	瑞克麦斯轮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCRICK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='RICK', name='瑞克麦斯', helpMark='RICK', fullName='瑞克麦斯轮船公司', enName='RICKMERS LINE')
    db.add(shipco) 
#	南非航运公司中国总代理
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSAF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SAF', name='南非航运', helpMark='SAF', fullName='南非航运公司中国总代理', enName='SAFMARINE CONTAINER LINES.GENERAL AGENT IN CHINA')
    db.add(shipco) 
#	俄罗斯萨哈林航运有限公司（正）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSAS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SAS', name='萨哈林航运（正）', helpMark='SAS', fullName='俄罗斯萨哈林航运有限公司（正）', enName='SAKHALIN SHIPPING COMPANY')
    db.add(shipco) 
#	迅航
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSCAN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SCAN', name='迅航', helpMark='SCAN', fullName='迅航', enName='SCANDUTCH')
    db.add(shipco) 
#	俄罗斯联合航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSCF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SCF', name='俄罗斯联合航运', helpMark='SCF', fullName='俄罗斯联合航运公司', enName='SCF ORIENTAL LINES LTD')
    db.add(shipco) 
#	印度国家航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSCI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SCI', name='印度国家航运', helpMark='SCI', fullName='印度国家航运公司', enName='THE SHIPPING CORPORATION OF INDIA LTD.')
    db.add(shipco) 
#	土星集装箱航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSCL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SCL', name='土星航运', helpMark='SCL', fullName='土星集装箱航运有限公司', enName='SATURN CONTAINER LINES PTE LTD')
    db.add(shipco) 
#	海运船务（新加坡）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSCO',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SCO', name='海运（新加坡）（代理BEN边行）', helpMark='SCO', fullName='海运船务（新加坡）有限公司', enName='SEA CONSORTIUM PTE LTD')
    db.add(shipco) 
#	山东省国际海运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSDM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SDM', name='山东国际海运', helpMark='SDM', fullName='山东省国际海运公司', enName='SHANDONG PROVINCE MARINE SHIPPING CO.')
    db.add(shipco) 
#	海洋集装箱运输有限公司（英国）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSEAC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SEAC', name='海洋集装箱运输（英国）', helpMark='SEAC', fullName='海洋集装箱运输有限公司（英国）', enName='SEA CONTAINER LTD.')
    db.add(shipco) 
#	南泰船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSEAW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SEAW', name='南泰船务', helpMark='SEAW', fullName='南泰船务有限公司', enName='HAMDA/SEAWISE')
    db.add(shipco) 
#	胜利船务（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSEN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SEN', name='德国胜利', helpMark='SEN', fullName='胜利船务（中国）有限公司', enName='SENATOR LINES(CHINA)CO.,LTD')
    db.add(shipco) 
#	上海国际轮渡有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSFC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SFC', name='上海国际轮渡', helpMark='SFC', fullName='上海国际轮渡有限公司', enName='SHANGHAI INTERNATIONAL FERRY CO.,LTD.')
    db.add(shipco) 
#	海兴国货
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSHX',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SHX', name='海兴国货', helpMark='SHX', fullName='海兴国货', enName='')
    db.add(shipco) 
#	上海仁川国际渡轮有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSIF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SIF', name='仁川国际渡轮', helpMark='SIF', fullName='上海仁川国际渡轮有限公司', enName='SHANGHAI INCHON INTERNATIONAL FERRY CO., LTD.')
    db.add(shipco) 
#	上海外运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSINO',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SINO', name='上海外运', helpMark='SINO', fullName='上海外运', enName='SINOTRAN')
    db.add(shipco) 
#	新海丰集装箱运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSIT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SIT', name='新海丰集运', helpMark='SIT', fullName='新海丰集装箱运输有限公司', enName='SITC CONTAINER LINES (SHANGHAI) CO.,LTD.')
    db.add(shipco) 
#	上海市锦江航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSJJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SJJ', name='锦江航运', helpMark='SJJ', fullName='上海市锦江航运有限公司', enName='SHANGHAI JINJIANG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	上海市锦江航运有限公司（直提空箱）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSJJZ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SJJZ', name='锦江航运（直提空箱）', helpMark='SJJZ', fullName='上海市锦江航运有限公司（直提空箱）', enName='SHANGHAI JINJIANG SHIPPING CO.,LTD.')
    db.add(shipco) 
#	缅甸五星轮船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSLA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SLA', name='缅甸五星', helpMark='SLA', fullName='缅甸五星轮船公司', enName='MYANMA FIVE STAR LINE')
    db.add(shipco) 
#	牡丹江外运（大连） 有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSMDJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SMDJ', name='牡丹江外运', helpMark='SMDJ', fullName='牡丹江外运（大连） 有限公司', enName='SINOTRANS MUDANJIANG(DALIAN)CO.')
    db.add(shipco) 
#	司马泰航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSMH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SMH', name='司马泰航运', helpMark='SMH', fullName='司马泰航运有限公司', enName='SIMATECH SHIPPING PTE LTD')
    db.add(shipco) 
#	海马船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSMSK',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SMSK', name='海马船务', helpMark='SMSK', fullName='海马船务有限公司', enName='SINO MAERSK CO.,LTD.')
    db.add(shipco) 
#	长锦商船（中国）船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSNKO',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SNKO', name='长锦商船', helpMark='SNKO', fullName='长锦商船（中国）船务有限公司', enName='SINOKOR MERCHANT MARINE (CHINA) CO., LTD.')
    db.add(shipco) 
#	中外运集装箱运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSNL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SNL', name='中外运集运', helpMark='SNL', fullName='中外运集装箱运输有限公司', enName='SINOTRANS CONTAINER LINES CO.,LTD.')
    db.add(shipco) 
#	货主自备箱
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSOC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SOC', name='货主自备箱', helpMark='SOC', fullName='货主自备箱', enName='SOC')
    db.add(shipco) 
#	顺发航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSOF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SOF', name='顺发航运', helpMark='SOF', fullName='顺发航运有限公司', enName='SOFAST SHIPPING LIMITED')
    db.add(shipco) 
#	上海海华国际货运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSPA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SPA', name='上海海华货运', helpMark='SPA', fullName='上海海华国际货运有限公司', enName='')
    db.add(shipco) 
#	中富运通
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSPAL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SPAL', name='中富运通', helpMark='SPAL', fullName='中富运通', enName='')
    db.add(shipco) 
#	上海港国际集装箱货运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSPCFA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SPCFA', name='上海港国际集装箱货运', helpMark='SPCFA', fullName='上海港国际集装箱货运有限公司', enName='SHANGHAI PORT INTERNATIONAL CONTAINER FORWARDING CO., LTD')
    db.add(shipco) 
#	新加坡速达航运私人有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSPD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SPD', name='速达海运', helpMark='SPD', fullName='新加坡速达航运私人有限公司', enName='SPEEDA SHIPPING COMPANY ( S ) PTE LTD')
    db.add(shipco) 
#	暹罗国际航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSPIC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SPIC', name='暹罗航运', helpMark='SPIC', fullName='暹罗国际航运有限公司', enName='SIAM PAETRA INTERNATIONAL CO., LTD.')
    db.add(shipco) 
#	俄罗斯萨哈林航运有限公司（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSSA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SSA', name='萨哈林航运（租）', helpMark='SSA', fullName='俄罗斯萨哈林航运有限公司（租）', enName='SAKHALIN SHIPPING COMPANY')
    db.add(shipco) 
#	上海快航株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSSE',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SSE', name='上海快航', helpMark='SSE', fullName='上海快航株式会社', enName='SHANGHAI SUPER EXPRESS CO., LTD.')
    db.add(shipco) 
#	海峡船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSSGP',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SSGP', name='海峡船务', helpMark='SSGP', fullName='海峡船务有限公司', enName='STRAITS SHIPPING LTD.')
    db.add(shipco) 
#	萨姆达拉船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SSL', name='萨姆达拉', helpMark='SSL', fullName='萨姆达拉船务有限公司', enName='SAMUDERA SHIPPING LINE.,LTD.')
    db.add(shipco) 
#	中国外运天津有限公司海运分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSTJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='STJ', name='中外运天津海运', helpMark='STJ', fullName='中国外运天津有限公司海运分公司', enName='SINOTRANS TIANJIN COMPANY LIMITED MARINE TRANSPORTATION BRANCH')
    db.add(shipco) 
#	申卫
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SW', name='申卫', helpMark='SW', fullName='申卫', enName='')
    db.add(shipco) 
#	昭和海运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSWAL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SWAL', name='昭和海运', helpMark='SWAL', fullName='昭和海运', enName='SHOWA LINE LTD.')
    db.add(shipco) 
#	俄罗斯萨哈林航运有限公司（租）
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSWF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SWF', name='萨哈林航运（租）', helpMark='SWF', fullName='俄罗斯萨哈林航运有限公司（租）', enName='SAKHALIN SHIPPING COMPANY')
    db.add(shipco) 
#	太古船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSWIR',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SWIR', name='太古船代', helpMark='SWIR', fullName='太古船务代理有限公司', enName='SEIRE SHIPPING(AGENCIES) LTD.')
    db.add(shipco) 
#	海陆船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSWL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SWL', name='海陆船务', helpMark='SWL', fullName='海陆船务有限公司', enName='SEAWAY SHIPPING LINE CO., LTD.')
    db.add(shipco) 
#	志晓船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSWS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SWS', name='志晓船务', helpMark='SWS', fullName='志晓船务有限公司', enName='SWELL CHIEF SHIPPING CO., LTD.')
    db.add(shipco) 
#	山东省烟台国际海运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCSYMS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='SYMS', name='烟台海运', helpMark='SYMS', fullName='山东省烟台国际海运公司', enName='SHANDONG PROVINCE YANTAI INTERNATIONAL MARINE SHIPPING CO.')
    db.add(shipco) 
#	通亚航运公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTAL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TAL', name='通亚航运', helpMark='TAL', fullName='通亚航运公司', enName='TRANS ASIAN SHIPPING SERVICES PRIVATE LIMITED')
    db.add(shipco) 
#	美国天泰货柜租赁有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTEX',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TEX', name='美国天泰', helpMark='TEX', fullName='美国天泰货柜租赁有限公司', enName='Textainer Equipment Management(U.S.)Ltd')
    db.add(shipco) 
#	致远船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTFL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TFL', name='致远船务', helpMark='TFL', fullName='致远船务有限公司', enName='TRANSFAR SHIPPING CO., LIMITED')
    db.add(shipco) 
#	台骅国际有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTHI',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='THI', name='台骅国际', helpMark='THI', fullName='台骅国际有限公司', enName='THI LTD')
    db.add(shipco) 
#	天津津海海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTJM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TJM', name='天津津海', helpMark='TJM', fullName='天津津海海运有限公司', enName='TIANJIN JINHAI MARINE SHIPPING CO., LTD.')
    db.add(shipco) 
#	天津外运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTJST',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TJST', name='天津外运', helpMark='TJST', fullName='天津外运', enName='')
    db.add(shipco) 
#	天神国际海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTKSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TKSL', name='天神海运', helpMark='TKSL', fullName='天神国际海运有限公司', enName='TIANJIN-KOBE INTERNATIONAL MARINE SHIPPING CO., LTD.')
    db.add(shipco) 
#	墨西哥航运有限公司 
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTMM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TMM', name='墨西哥航运', helpMark='TMM', fullName='墨西哥航运有限公司 ', enName='TRANSPORTACION MARITIME MEXICANA SOCIEDAD ANONIAM')
    db.add(shipco) 
#	天津市海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTMS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TMS', name='天津海运', helpMark='TMS', fullName='天津市海运股份有限公司', enName='TIANJIN MARINE SHIPPING CO.,LTD.')
    db.add(shipco) 
#	台湾航业股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTNC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TNC', name='台湾航业', helpMark='TNC', fullName='台湾航业股份有限公司', enName='TAIWAN NAVIGATION COMPANY')
    db.add(shipco) 
#	东航船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTOHO',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TOHO', name='东航船务', helpMark='TOHO', fullName='东航船务有限公司', enName='TOHO LINE SHIPPING LTD.')
    db.add(shipco) 
#	塔斯曼东方航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTOL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TOL', name='塔斯曼东方', helpMark='TOL', fullName='塔斯曼东方航运有限公司', enName='TASMAN ORIENT LINE LTD.')
    db.add(shipco) 
#	泛太航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTPL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TPL', name='泛太航运', helpMark='TPL', fullName='泛太航运有限公司', enName='TRANS-PACIFIC LINES LIMITED')
    db.add(shipco) 
#	连捷海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTRMA',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TRMA', name='连捷海运', helpMark='TRMA', fullName='连捷海运有限公司', enName='TRMA')
    db.add(shipco) 
#	特来顿国际租箱公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTRT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TRT', name='特来顿租箱', helpMark='TRT', fullName='特来顿国际租箱公司', enName='Triton Container International Limited.')
    db.add(shipco) 
#	德祥航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TSC', name='德祥航运', helpMark='TSC', fullName='德祥航运有限公司', enName='T.S.LINES LTD.')
    db.add(shipco) 
#	太荣商船株式会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCTYS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='TYS', name='太荣商船', helpMark='TYS', fullName='太荣商船株式会社', enName='TAIYOUNG SHIPPING CO.,LTD')
    db.add(shipco) 
#	非洲联船公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCUAF',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='UAF', name='非洲联船', helpMark='UAF', fullName='非洲联船公司', enName='UNITED AFRICA FEEDER LINE')
    db.add(shipco) 
#	阿联轮船（上海）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCUASC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='UASC', name='阿联轮船', helpMark='UASC', fullName='阿联轮船（上海）有限公司', enName='United Arab Shipping Agency Company (Shanghai) Limited')
    db.add(shipco) 
#	立荣海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCUNG',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='UNG', name='立荣海运', helpMark='UNG', fullName='立荣海运股份有限公司', enName='UNIGLORY MARINE CORPORATION')
    db.add(shipco) 
#	利迅船务公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCUNS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='UNS', name='利迅船务', helpMark='UNS', fullName='利迅船务公司', enName='UNSION SHIPPING CO.')
    db.add(shipco) 
#	环球船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCUWSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='UWSL', name='环球船务', helpMark='UWSL', fullName='环球船务有限公司', enName='UNI-WORLD SHIPPING LTD.')
    db.add(shipco) 
#	沃斯克海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCVAS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='VAS', name='沃斯克海运', helpMark='VAS', fullName='沃斯克海运有限公司', enName='VASCO MARITIME PTE LTD.')
    db.add(shipco) 
#	威高物流（上海）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCVGW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='VGW', name='威高物流', helpMark='VGW', fullName='威高物流（上海）有限公司', enName='V-GROW LOGISTICS （SHANGHAI）CO.,LTD.')
    db.add(shipco) 
#	西威航运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCVSSL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='VSSL', name='西威航运', helpMark='VSSL', fullName='西威航运', enName='SEAWAYS SHIPPING LINE LTD')
    db.add(shipco) 
#	芜湖安华船务 
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWHAH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WHAH', name='芜湖安华', helpMark='WHAH', fullName='芜湖安华船务 ', enName='')
    db.add(shipco) 
#	武汉长伟航运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWHCW',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WHCW', name='武汉长伟', helpMark='WHCW', fullName='武汉长伟航运', enName='')
    db.add(shipco) 
#	万海航运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWHL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WHL', name='万海航运', helpMark='WHL', fullName='万海航运股份有限公司', enName='WAN HAI LINES CO., LTD.')
    db.add(shipco) 
#	大连威兰德船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWIN',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WIN', name='大连威兰德', helpMark='WIN', fullName='大连威兰德船务有限公司', enName='WINLAND SHIPPING CO.,LTD.')
    db.add(shipco) 
#	祀进海空
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWJS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WJS', name='祀进海空', helpMark='WJS', fullName='祀进海空', enName='')
    db.add(shipco) 
#	环世集装箱运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWLC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WLC', name='环世集运', helpMark='WLC', fullName='环世集装箱运输有限公司', enName='WORLDWIDE CONTAINER LINE LIMITED.')
    db.add(shipco) 
#	西海航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWOS',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WOS', name='西海航运', helpMark='WOS', fullName='西海航运有限公司', enName='WEST OCEAN SHIPPING COMPANY LIMITED')
    db.add(shipco) 
#	香港宏光发展有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWSDL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WSDL', name='香港宏光', helpMark='WSDL', fullName='香港宏光发展有限公司', enName='WIDE SHINE DEVELOPMENT LTD')
    db.add(shipco) 
#	华轮-威尔森（中国）船务有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWWL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WWL', name='华轮-威尔森', helpMark='WWL', fullName='华轮-威尔森（中国）船务有限公司', enName='WALLENIUS WILHELMSEN LINES')
    db.add(shipco) 
#	无锡江太
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCWXJT',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='WXJT', name='无锡江太', helpMark='WXJT', fullName='无锡江太', enName='')
    db.add(shipco) 
#	持箱人不明
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCXXX',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='XXX', name='持箱人不明', helpMark='XXX', fullName='持箱人不明', enName='')
    db.add(shipco) 
#	阳明海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCYML',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='YML', name='阳明海运', helpMark='YML', fullName='阳明海运股份有限公司', enName='YANGMING MARINE TRANSPORT CORP')
    db.add(shipco) 
#	洋浦惠隆海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCYPHL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='YPHL', name='洋浦惠隆', helpMark='YPHL', fullName='洋浦惠隆海运有限公司', enName='YPHL')
    db.add(shipco) 
#	阳海海运株氏会社
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCYSC',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='YSC', name='阳海海运', helpMark='YSC', fullName='阳海海运株氏会社', enName='YANGHAI SHIPPING CO.LTD.')
    db.add(shipco) 
#	亿通航运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCYTL',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='YTL', name='亿通航运', helpMark='YTL', fullName='亿通航运股份有限公司', enName='YI TONG CONTAINER LINE LTD.')
    db.add(shipco) 
#	中国扬子江轮船股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCYZJ',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='YZJ', name='扬子江', helpMark='YZJ', fullName='中国扬子江轮船股份有限公司', enName='CHINA YANGTZE RIVER SHIPPING CO.,LTD')
    db.add(shipco) 
#	上海振华国际船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCZHCD',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ZHCD', name='振华船代', helpMark='ZHCD', fullName='上海振华国际船务代理有限公司', enName='SHANGHAI ZHENHUA INTERNATIONAL SHIPPING AGENCY CO.')
    db.add(shipco) 
#	中海航集
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCZHH',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ZHH', name='中海航集', helpMark='ZHH', fullName='中海航集', enName='')
    db.add(shipco) 
#	以星综合航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCZIM',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ZIM', name='以星', helpMark='ZIM', fullName='以星综合航运（中国）有限公司', enName='ZIM INTEGRATED SHIPPING SERVICES （CHINA）CO.,LTD.')
    db.add(shipco) 
#	浙江远洋
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCZJYY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ZJYY', name='浙江远洋', helpMark='ZJYY', fullName='浙江远洋', enName='')
    db.add(shipco) 
#	中铁国际货运上海分公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'SCZTHY',
                accountType = GLBConfig.ATYPE_SHIPCO, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    shipco = ShipCoInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_SHIPCO, 
                code='ZTHY', name='中铁货运', helpMark='ZTHY', fullName='中铁国际货运上海分公司', enName='')
    db.add(shipco)
    
#################################################################
    
    #        美国总统轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CAPL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)    
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='APL', name='APL', helpMark='APL', fullName='美国总统轮船（中国）有限公司')
    db.add(carrier) 
    #        中日国际轮渡有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCJF',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CJF', name='新鉴真', helpMark='CJF', fullName='中日国际轮渡有限公司')
    db.add(carrier)
    #        中诚联合航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCSS',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CSS', name='联合', helpMark='CSS', fullName='中诚联合航运有限公司')
    db.add(carrier)
    #        中通国际海运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)   
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CL', name='中通', helpMark='CL', fullName='中通国际海运有限公司')
    db.add(carrier)      
    #        上海华港国际船舶代理
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCPSA',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CPSA', name='华港', helpMark='CPSA', fullName='上海华港国际船舶代理')
    db.add(carrier)
    #        上海航华国际船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCNSL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CNSL', name='航华', helpMark='CNSL', fullName='上海航华国际船务代理有限公司')
    db.add(carrier)
    #        法国达飞轮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCMA',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CMA', name='达飞', helpMark='CPCMASA', fullName='法国达飞轮船（中国）有限公司')
    db.add(carrier)
    #        中远
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCOSCO',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='COSCO', name='中远', helpMark='COSCO', fullName='中远集装箱运输有限公司')
    db.add(carrier)
    #        中海集装箱运输股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CCSC',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='CSC', name='中海', helpMark='CSC', fullName='中海集装箱运输股份有限公司')
    db.add(carrier)
    #        达通
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CEAS',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='EAS', name='达通', helpMark='EAS', fullName='达通国际航运有限公司')
    db.add(carrier)
    #        亿通
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CYTL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='YTL', name='亿通', helpMark='YTL', fullName='亿通航运股份有限公司')
    db.add(carrier)
    #        川崎汽船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CKL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)  
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='KL', name='老K', helpMark='KL', fullName='川崎汽船（中国）有限公司')
    db.add(carrier)   
    #        日本邮船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CNYK',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='NYK', name='NYK', helpMark='NYK', fullName='日本邮船（中国）有限公司')
    db.add(carrier)
    #        商船三井（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CMOL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='MOL', name='大阪', helpMark='MOL', fullName='商船三井（中国）有限公司')
    db.add(carrier)
    #        地中海
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CMSC',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='MSC', name='地中海', helpMark='MSC', fullName='上海联东地中海国际船舶代理有限公司')
    db.add(carrier)
    #        民生轮船有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CMSK',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='MSK', name='马士基', helpMark='MSK', fullName='马士基（中国）航运有限公司上海分公司')
    db.add(carrier)
    #        新海航业有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CNEHU',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='NEHU', name='新海', helpMark='NEHU', fullName='新海航业有限公司')
    db.add(carrier)    
    #        现代商船（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CHMM',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='HMM', name='现代', helpMark='HMM', fullName='现代商船（中国）有限公司')
    db.add(carrier)   
#        上海安通船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CONT',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='ONT', name='安通', helpMark='ONT', fullName='上海安通船务代理有限公司')
    db.add(carrier)
#        东方海外货柜航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'COOCL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user) 
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='OOCL', name='东方', helpMark='OOCL', fullName='东方海外货柜航运（中国）有限公司')
    db.add(carrier)
#        上海海华国际货运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CSPA',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)    
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='SPA', name='海华', helpMark='SPA', fullName='上海海华国际货运有限公司')
    db.add(carrier)  
#        上海外运
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CSINO',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='SINO', name='外运', helpMark='SINO', fullName='上海中外运船务代理有限公司')
    db.add(carrier)
#        新海丰集装箱运输有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CSIT',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='SIT', name='海丰', helpMark='SIT', fullName='新海丰集装箱运输有限公司')
    db.add(carrier)
#        上海市锦江航运有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CSJJ',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='SJJ', name='锦江', helpMark='SJJ', fullName='上海市锦江航运有限公司')
    db.add(carrier)
#        上海顺德国际船舶代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CSHUNDE',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='SHUNDE', name='顺德', helpMark='SHUNDE', fullName='上海顺德国际船舶代理有限公司')
    db.add(carrier)
#        万海航运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CWHL',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='WHL', name='联骏', helpMark='WHL', fullName='万海航运股份有限公司')
    db.add(carrier)
#        中国上海外轮代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CWAIDAI',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='WAIDAI', name='外代', helpMark='WAIDAI', fullName='中国上海外轮代理有限公司')
    db.add(carrier)
#        中国扬子江轮船股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CYZJ',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='YZJ', name='扬子江', helpMark='YZJ', fullName='中国扬子江轮船股份有限公司')
    db.add(carrier)
#        阳明海运股份有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CYML',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='YML', name='阳明', helpMark='YML', fullName='阳明海运股份有限公司')
    db.add(carrier)
#        上海中和国际物流
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CZHONGHE',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='ZHONGHE', name='中和', helpMark='ZHONGHE', fullName='上海中和国际物流')
    db.add(carrier)
#        以星综合航运（中国）有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CZIM',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='ZIM', name='以星', helpMark='ZIM', fullName='以星综合航运（中国）有限公司')
    db.add(carrier)
#        上海振华国际船务代理有限公司
    user = User(OID = GLBConfig.SUPERCO, userID = SysUtil.genUserID(), userName = 'CZHCD',
                accountType = GLBConfig.ATYPE_CARRIER, password = GLBConfig.PASSWORD_DEFAULT, email = 'test@example.com')
    db.add(user)
    carrier = CarrierInfo(OID = GLBConfig.SUPERCO, userID = user.userID, userGroupID=GLBConfig.GTYPE_CARRIER, 
                          code='ZHCD', name='振华', helpMark='ZHCD', fullName='上海振华国际船务代理有限公司')
    db.add(carrier)

####################################################################################
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'CNSL',
                webName = '航华',
                website = 'http://www.chinasailing.com.cn')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'SPA',
                webName = '海华',
                website = 'http://202.136.213.238:8080/ShipSuiteWeb/bi/index.htm')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'SINO',
                webName = '外运',
                website = 'http://http://www.sinoagentsh.com/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'APL',
                webName = 'APL',
                website = 'http://101.231.209.227/ERS/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'HAL',
                webName = '新亚',
                website = 'http://www.penavico.sh.cn/proxy/proxy_query.jsp?tab=tab-2#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'ASL',
                webName = '亚海',
                website = 'http://www.penavico.sh.cn/proxy/proxy_query.jsp?tab=tab-2#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'KL',
                webName = '老K',
                website = 'http://58.246.192.28:8001/Initial.aspx')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'NYK',
                webName = 'NYK',
                website = 'http://cloud.easipass.com/nykeir2/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'HMM',
                webName = '现代',
                website = 'http://www.hmm21.com/')
    db.add(queryWeb)
    
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'OOCL',
                webName = '东方海外',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'MSK',
                webName = '马士基',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'HJS',
                webName = '韩进',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'CMA',
                webName = '达飞',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'MOL',
                webName = '三井',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'PIL',
                webName = '太平',
                website = 'http://cloud.easipass.com/ols/home.do#')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'MSC',
                webName = '联东地中海',
                website = 'http://web.lindomsc.com/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'COSCO',
                webName = '中远',
                website = 'http://ebusiness.coscon.com/NewEB/home.html')
    db.add(queryWeb)
    
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'WAIDAI',
                webName = '外代',
                website = 'http://www.penavico.sh.cn/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'CPSA',
                webName = '华港',
                website = 'http://www.chinaports-agency.com/query/ckfxcd.jsp')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'ZHCD',
                webName = '振华',
                website = 'http://61.181.252.146:7002/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'SHUNDE',
                webName = '顺德',
                website = 'http://www.sun-dial.com/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'ZHONGHE',
                webName = '中和',
                website = 'http://service.chinaconcord.com:8080/')
    db.add(queryWeb)
    queryWeb = PreplanQueryWeb(OID = GLBConfig.YANGQICO,
                webID = 'SJJ',
                webName = '锦江',
                website = 'http://www.jjshipping.cn/')
    db.add(queryWeb)
    
    
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