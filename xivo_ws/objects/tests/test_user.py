# -*- coding: utf-8 -*-

# Copyright (C) 2012-2016 Avencall
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
from xivo_ws.objects.user import User, UserLine, UserVoicemail, UserWebService


class TestUser(unittest.TestCase):

    def test_to_obj_dict(self):
        expected_obj_dict = {
            'userfeatures': {
                'musiconhold': 'default',
                'entityid': 2,
                'enablehint': True,
                'enablexfer': True,
                'firstname': 'Jack',
                'lastname': 'Johnson',
                'language': 'en_US',
                'enableclient': True,
                'loginclient': 'jack',
                'passwdclient': 'jack',
                'profileclient': 'Agent',
                'bsfilter': 'no',
                'agentid': 1,
                'mobilephonenumber': '5555555555',
            },
            'linefeatures': {
                'protocol': ['sip'],
                'context': ['default'],
                'number': [1000],
                'device': [42],
                'num': [2],
                'secret': ['toto']
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
            },
            'voicemail': {
                'name': 'jack johnson',
                'number': 1000,
                'password': 'qwerty',
                'context': 'default',
            }
        }
        user = User(firstname='Jack',
                    lastname='Johnson',
                    language='en_US',
                    enable_client=True,
                    client_username='jack',
                    client_password='jack',
                    client_profile='Agent',
                    bsfilter='no',
                    entity_id=2,
                    agent_id=1,
                    enable_hint=True,
                    line=UserLine(number=1000, context='default', device_id=42, device_slot=2, secret='toto'),
                    voicemail=UserVoicemail(number=1000, name='jack johnson', password='qwerty', context='default'),
                    mobile_number='5555555555')

        obj_dict = user.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_with_existing_line(self):
        expected_obj_dict = {
            'userfeatures': {
                'musiconhold': 'default',
                'entityid': 2,
                'enablehint': True,
                'enablexfer': True,
                'firstname': 'Jack',
                'lastname': 'Johnson',
                'language': 'en_US',
                'enableclient': True,
                'loginclient': 'jack',
                'passwdclient': 'jack',
                'profileclient': 'Agent',
                'bsfilter': 'boss',
                'agentid': 1,
                'mobilephonenumber': '5555555555',
            },
            'linefeatures': {
                'id': ['23']
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
                }
            }
        }
        user = User(firstname='Jack',
                    lastname='Johnson',
                    language='en_US',
                    enable_client=True,
                    client_username='jack',
                    client_password='jack',
                    client_profile='Agent',
                    bsfilter='boss',
                    entity_id=2,
                    agent_id=1,
                    enable_hint=True,
                    line=UserLine(id='23'),
                    mobile_number='5555555555')

        obj_dict = user.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_with_profile_id(self):
        expected_obj_dict = {
            'userfeatures': {
                'musiconhold': 'default',
                'entityid': 2,
                'enablehint': True,
                'enablexfer': True,
                'firstname': 'Jack',
                'lastname': 'Johnson',
                'language': 'en_US',
                'enableclient': True,
                'loginclient': 'jack',
                'passwdclient': 'jack',
                'cti_profile_id': 5,
                'bsfilter': 'no',
                'agentid': 1,
                'mobilephonenumber': '5555555555',

            },
            'linefeatures': {
                'id': ['23']
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
                }
            }
        }
        user = User(firstname='Jack',
                    lastname='Johnson',
                    language='en_US',
                    enable_client=True,
                    client_username='jack',
                    client_password='jack',
                    client_profile_id=5,
                    entity_id=2,
                    bsfilter='no',
                    agent_id=1,
                    enable_hint=True,
                    line=UserLine(id='23'),
                    mobile_number='5555555555')

        obj_dict = user.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'id': 4,
            'entityid': 2,
            'firstname': 'Jack',
            'lastname': 'Johnson',
            "agentid": 1,
            "pictureid": None,
            "callerid": "\"Jack Johnson\"",
            "ringseconds": "30",
            "simultcalls": "5",
            "enableclient": False,
            "loginclient": "jack",
            "passwdclient": "johnson",
            "cti_profile_id": "5",
            "enablehint": True,
            "enablevoicemail": False,
            "enablexfer": True,
            "enableonlinerec": False,
            "callrecord": False,
            "incallfilter": False,
            "enablednd": False,
            "enableunc": False,
            "destunc": "",
            "enablerna": False,
            "destrna": "",
            "enablebusy": False,
            "destbusy": "",
            "musiconhold": "default",
            "outcallerid": "default",
            "mobilephonenumber": "5555555555",
            "userfield": "",
            "bsfilter": "no",
            "preprocess_subroutine": None,
            "timezone": "",
            "language": None,
            "ringintern": "",
            "ringextern": "",
            "ringgroup": "",
            "ringforward": "",
            "rightcallcode": "",
            "pitch": None,
            "pitchdirection": None,
            "commented": False,
            "description": "",
            "fullname": "Jack Johnson",
            "identity": "Jack Johnson"
        }

        user = User.from_list_obj_dict(obj_dict)

        self.assertEqual(user.id, 4)
        self.assertEqual(user.entity_id, 2)
        self.assertEqual(user.firstname, 'Jack')
        self.assertEqual(user.lastname, 'Johnson')
        self.assertEqual(user.enable_client, False)
        self.assertEqual(user.client_username, 'jack')
        self.assertEqual(user.client_password, 'johnson')
        self.assertEqual(user.client_profile_id, '5')
        self.assertEqual(user.agent_id, 1)
        self.assertEqual(user.mobile_number, '5555555555')


class TestUserWebService(unittest.TestCase):
    def setUp(self):
        ws_client = Mock()
        self._ws = UserWebService(ws_client)
