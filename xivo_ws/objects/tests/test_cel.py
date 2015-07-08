# -*- coding: utf-8 -*-

# Copyright (C) 2012-2014 Avencall
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

from __future__ import unicode_literals

import unittest

from mock import Mock
from xivo_ws.objects.cel import CEL, CELWebService


class TestCEL(unittest.TestCase):

    def test_from_list_obj_dict(self):
        obj_dict = {
            'id': 21074,
            'eventtype': 'CHAN_START',
            'eventtime': '2012-02-27 03:27:21.017623',
            'userdeftype': '',
            'cid_name': 'Sup - asterisk',
            'cid_num': 'asterisk',
            'cid_ani': '',
            'cid_rdnis': '',
            'cid_dnid': '',
            'exten': '42803',
            'context': 'default',
            'channame': 'IAX2/assurancetourisk-durallo-16052',
            'appname': '',
            'appdata': '',
            'amaflags': '3',
            'accountcode': '',
            'peeraccount': '',
            'uniqueid': '1330331241.287',
            'linkedid': '1330331241.287',
            'userfield': '',
            'peer': '',
            'amaflagsmeta': 'documentation'
        }

        cel = CEL.from_list_obj_dict(obj_dict)

        self.assertEqual(cel.id, 21074)
        self.assertEqual(cel.eventtype, 'CHAN_START')
        self.assertEqual(cel.eventtime, '2012-02-27 03:27:21.017623')
        self.assertEqual(cel.userdeftype, '')
        self.assertEqual(cel.cid_name, 'Sup - asterisk')
        self.assertEqual(cel.cid_num, 'asterisk')
        self.assertEqual(cel.cid_ani, '')
        self.assertEqual(cel.cid_rdnis, '')
        self.assertEqual(cel.cid_dnid, '')
        self.assertEqual(cel.exten, '42803')
        self.assertEqual(cel.context, 'default')
        self.assertEqual(cel.channame, 'IAX2/assurancetourisk-durallo-16052')
        self.assertEqual(cel.appname, '')
        self.assertEqual(cel.appdata, '')
        self.assertEqual(cel.amaflags, '3')
        self.assertEqual(cel.accountcode, '')
        self.assertEqual(cel.peeraccount, '')
        self.assertEqual(cel.uniqueid, '1330331241.287')
        self.assertEqual(cel.linkedid, '1330331241.287')
        self.assertEqual(cel.userfield, '')
        self.assertEqual(cel.peer, '')


class TestCELWebService(unittest.TestCase):
    def setUp(self):
        ws_client = Mock()
        self._ws = CELWebService(ws_client)

    def test_search_by_id(self):
        id_beg = 22
        self._ws._ws_client.custom_request.return_value = '[]'

        self._ws.search_by_id(id_beg)

        self._ws._ws_client.custom_request.assert_called_once_with(self._ws._PATH,
                                                                   'act=searchid&idbeg=22')
