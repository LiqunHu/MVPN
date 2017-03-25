# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:18:23 2016

@author: huliqun
@email: huliquns@126.com
"""
from wsgiref import simple_server
import falcon

from workserver.util import DataFormat
from workserver.util import Authority
from workserver.util import LogUtil
from workserver.util import SysUtil

from workserver.service import AuthSRV
from workserver.service.system import operatorControlSRV, groupControlSRV,menuControlSRV, groupMenuControlSRV, userSettingSRV

LogUtil.initLog()
SysUtil.global_init()
# Configure your WSGI server to load "things.app" (app is a WSGI callable)
app = falcon.API(middleware=[
    Authority.MimeTypesCheck(),
    Authority.AuthMiddleware(),
    DataFormat.JSONTranslator(),
    DataFormat.MultipartMiddleware(),
])

app.add_route('/api/auth', AuthSRV.AuthResource())
app.add_route('/api/system/operatorcontrol', operatorControlSRV.OperatorControlResource())
app.add_route('/api/system/groupcontrol', groupControlSRV.GroupControlResource())
app.add_route('/api/system/groupmenucontrol', groupMenuControlSRV.GroupMenuControlResource())
app.add_route('/api/system/menucontrol', menuControlSRV.MenuControlResource())
app.add_route('/api/system/userSettingControl', userSettingSRV.UserSettingResource())

#app.add_route('/{user_id}/things', ThingsSrv.ThingsResource(db))

# If a responder ever raised an instance of StorageError, pass control to
# the given handler.
#app.add_error_handler(StorageError, StorageError.handle)

# Proxy some things to another service; this example shows how you might
# send parts of an API off to a legacy system that hasn't been upgraded
# yet, or perhaps is a single cluster that all data centers have to share.
#sink = SinkAdapter()
#app.add_sink(sink, r'/search/(?P<engine>ddg|y)\Z')

# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 9000, app)
    httpd.serve_forever()

#gunicorn -b 127.0.0.1:9000 MainServer:app
