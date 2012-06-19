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

import unittest
from mock import Mock
from xivo_ws.client.webservice import WebServiceClient


class TestWebServiceClient(unittest.TestCase):
    def setUp(self):
        self._http_client = Mock()

    def _new_web_service_client(self):
        return WebServiceClient(self._http_client)

    def test_view_calls_http_client_correctly(self):
        ws_client = self._new_web_service_client()
        self._http_client.get.return_value = u'{}'

        ws_client.view(u'/foo/', u'1')

        self._http_client.get.assert_called_with(u'/foo/?act=view&id=1')

    def test_add_calls_http_client_correctly(self):
        ws_client = self._new_web_service_client()

        ws_client.add(u'/foo/', {u'a': u'b'})

        self._http_client.post.assert_called_with(u'/foo/?act=add', '{"a": "b"}',
                                             {u'Content-Type': u'application/json'})
