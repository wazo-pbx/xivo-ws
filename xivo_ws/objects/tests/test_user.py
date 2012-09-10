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
from mock import Mock
from xivo_ws.objects.user import User, UserLine, UserVoicemail, UserWebService, _ImportContentGenerator


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
                'profileclient': 'agent',
                "agentid": 1,
            },
            'linefeatures': {
                'protocol': ['sip'],
                'context': ['default'],
                'number': [1000],
                'device': [42],
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
            'voicemail-option': 'add',
            'voicemail': {
                'fullname': 'jack johnson',
                'mailbox': 1000,
                'password': 'qwerty',
            }
        }
        user = User(firstname='Jack',
                    lastname='Johnson',
                    language='en_US',
                    enable_client=True,
                    client_username='jack',
                    client_password='jack',
                    client_profile='agent',
                    entity_id=2,
                    agent_id=1,
                    enable_hint=True,
                    line=UserLine(number=1000, context='default', device_id=42),
                    voicemail=UserVoicemail(number=1000, name='jack johnson', password='qwerty'))

        obj_dict = user.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'id': 4,
            'entityid': 2,
            'firstname': 'Jack',
            'lastname': 'Johnson',
            "voicemailtype": 'asterisk',
            "voicemailid": 5,
            "agentid": 1,
            "pictureid": None,
            "callerid": "\"Jack Johnson\"",
            "ringseconds": "30",
            "simultcalls": "5",
            "enableclient": False,
            "loginclient": "",
            "passwdclient": "",
            "profileclient": "client",
            "enablehint": True,
            "enablevoicemail": False,
            "enablexfer": True,
            "enableautomon": False,
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
            "mobilephonenumber": "",
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
            "alarmclock": "",
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
        self.assertEqual(user.agent_id, 1)
        self.assertEqual(user.voicemail.id, 5)


class TestImportContentGenerator(unittest.TestCase):
    def test_header(self):
        expected_result = 'entityid|firstname|lastname|language|enableclient|username|password|profileclient|enablehint|phonenumber|context|protocol|voicemailname|voicemailmailbox|voicemailpassword'
        generator = _ImportContentGenerator()

        self.assertEqual(expected_result, generator._rows[0])

    def test_one_minimal_user(self):
        generator = _ImportContentGenerator()
        user = User(firstname='John')

        generator.add_users([user])

        self.assertEqual('1|John|||||||1||||||', generator._rows[1])

    def test_one_full_user(self):
        generator = _ImportContentGenerator()
        user = User(firstname='John F',
                    lastname='Jackson',
                    language='fr_FR',
                    enable_client=True,
                    client_username='user',
                    client_password='pass',
                    client_profile='client',
                    entity_id=2,
                    enable_hint=True,
                    line=UserLine(number=123, context='default', protocol='sip'),
                    voicemail=UserVoicemail(number=1000, name='John F Jackson', password='qwerty'))

        generator.add_users([user])

        self.assertEqual('2|John F|Jackson|fr_FR|1|user|pass|client|1|123|default|sip|John F Jackson|1000|qwerty', generator._rows[1])


class TestUserWebService(unittest.TestCase):
    def setUp(self):
        ws_client = Mock()
        self._ws = UserWebService(ws_client)

    def test_import(self):
        expected_content = b"""\
entityid|firstname|lastname|enableclient|username|password|profileclient|enablehint|phonenumber|context|protocol
1|John||||||1|||
1|Jack|Johnson|||||1|||
"""
        users = [User(firstname='John'), User(firstname='Jack', lastname='Johnson')]

        self._ws.import_(users)

        self._ws._ws_client.custom_request.assert_called_once_with(
                    self._ws._PATH, 'act=import', expected_content)
