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

from __future__ import unicode_literals

import unittest
from xivo_ws.objects.user import User, UserLine


class TestUser(unittest.TestCase):
    maxDiff = None
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'userfeatures': {
                'musiconhold': 'default',
                'entityid': 1,
                'enablehint': True,
                'enablexfer': True,
                'firstname': 'Jack',
                'lastname': 'Johnson',
                'enableclient': True,
                'loginclient': 'jack',
                'passwdclient': 'jack',
                'profileclient': 'agent',
            },
            'linefeatures': {
                'protocol': ['sip'],
                'context': ['default'],
                'number': [1000],
            },
            'dialaction': {
                'noanswer': {
                    'actiontype': 'none',
                },
                'busy': {
                    'actiontype': 'none',
                },
                'congestion': {
                    'actiontype': 'none',
                },
                'chanunavail': {
                    'actiontype': 'none',
                },
            }
        }
        user = User(firstname='Jack',
                    lastname='Johnson',
                    enable_client=True,
                    client_username='jack',
                    client_password='jack',
                    client_profile='agent',
                    line=UserLine(number=1000, context='default'))

        obj_dict = user.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)
