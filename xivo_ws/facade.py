# -*- coding: UTF-8 -*-

# Copyright (C) 2012  Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_ws.client.http import HTTPClient
from xivo_ws.client.webservice import WebServiceClient
from xivo_ws.registry import get_registered_ws_class


class BaseXivoServer(object):
    def __init__(self, ws_client):
        self.ws_client = ws_client
        for name, ws_class  in get_registered_ws_class().iteritems():
            ws = ws_class(ws_client)
            setattr(self, name, ws)


class XivoServer(BaseXivoServer):
    def __init__(self, host, username=None, password=None):
        BaseXivoServer.__init__(self, self._new_ws_client(host, username, password))

    def _new_ws_client(self, host, username, password):
        http_client = HTTPClient(host, username, password)
        ws_client = WebServiceClient(http_client)
        return ws_client

    def check_ws(self):
        self.ws_client.check_ws()
