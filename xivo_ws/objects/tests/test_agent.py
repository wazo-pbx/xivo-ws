# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 Avencall
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
from xivo_ws.objects.agent import Agent


class TestAgent(unittest.TestCase):
    def test_new_agent_with_no_attribute(self):
        agent = Agent()

        self.assertEqual(None, agent.id)
        self.assertEqual(None, agent.firstname)
        self.assertEqual(None, agent.lastname)
        self.assertEqual(None, agent.number)
        self.assertEqual(None, agent.context)
        self.assertEqual([], agent.users)

    def test_new_agent_with_all_attributes(self):
        agent = Agent(id=1,
                      firstname='First',
                      lastname='Last',
                      number='555',
                      context='default',
                      users=[1, 2])

        self.assertEqual(1, agent.id)
        self.assertEqual('First', agent.firstname)
        self.assertEqual('Last', agent.lastname)
        self.assertEqual('555', agent.number)
        self.assertEqual('default', agent.context)
        self.assertEqual([1, 2], agent.users)

    def test_to_obj_dict_with_minimum(self):
        expected_obj_dict = {
            'agentfeatures': {
                'numgroup': '1',
                'autologoff': '0',
                'firstname': 'First',
                'number': '555',
                'context': 'default',
            },
            'user-select': [],
        }
        agent = Agent(firstname='First',
                      number='555',
                      context='default')

        obj_dict = agent.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_with_full(self):
        expected_obj_dict = {
            'agentfeatures': {
                'numgroup': '1',
                'autologoff': '0',
                'firstname': 'First',
                'number': '555',
                'context': 'default',
                'lastname': 'Last',
                'passwd': 'password123',
            },
            'user-select': [1, 2],
        }
        agent = Agent(id=1,
                      firstname='First',
                      lastname='Last',
                      password='password123',
                      number='555',
                      context='default',
                      users=[1, 2])

        obj_dict = agent.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            "agentfeatures": {
                "autologoff": "0",
                "commented": False,
                "context": "default",
                "description": "",
                "firstname": "Agent",
                "fullname": "Agent 2",
                "group": None,
                "id": 3,
                "identity": "Agent 2 (2@default)",
                "language": "",
                "lastname": "2",
                "number": "2",
                "numgroup": "1",
                "passwd": "",
            },
            "agentgroup": {
                "commented": False,
                "deletable": False,
                "deleted": False,
                "description": "",
                "groupid": "1",
                "groups": "",
                "id": "1",
                "name": "default"
            },
            "queuemember": [
                {
                    "call-limit": "0",
                    "category": "queue",
                    "channel": "Agent",
                    "commented": False,
                    "interface": "Agent/2",
                    "paused": None,
                    "penalty": "0",
                    "queue_name": "test1023",
                    "queuefeaturesid": "44",
                    "skills": "agent-3",
                    "state_interface": "",
                    "userid": 3,
                    "usertype": "agent"
                }
            ],
            "queueskills": [],
            "usermember": [
                {
                    "agentid": "3",
                    "bsfilter": "no",
                    "callerid": "\"User 2\"",
                    "callrecord": False,
                    "commented": False,
                    "description": "",
                    "destbusy": "",
                    "destrna": "",
                    "destunc": "",
                    "enableautomon": False,
                    "enablebusy": False,
                    "enableclient": True,
                    "enablednd": False,
                    "enablehint": True,
                    "enablerna": False,
                    "enableunc": False,
                    "enablevoicemail": False,
                    "enablexfer": False,
                    "entityid": 1,
                    "firstname": "User",
                    "fullname": "User 2",
                    "id": 5,
                    "identity": "User 2",
                    "incallfilter": False,
                    "language": None,
                    "lastname": "2",
                    "loginclient": "user2",
                    "mobilephonenumber": "",
                    "musiconhold": "default",
                    "outcallerid": "default",
                    "passwdclient": "user2",
                    "pictureid": None,
                    "preprocess_subroutine": None,
                    "profileclient": "client",
                    "rightcallcode": "",
                    "ringextern": "",
                    "ringforward": "",
                    "ringgroup": "",
                    "ringintern": "",
                    "ringseconds": "30",
                    "simultcalls": "5",
                    "timezone": "",
                    "userfield": "",
                    "voicemailid": None,
                    "voicemailtype": None
                }
            ]
        }

        agent = Agent.from_obj_dict(obj_dict)

        self.assertEqual(3, agent.id)
        self.assertEqual('Agent', agent.firstname)
        self.assertEqual('2', agent.lastname)
        self.assertEqual('2', agent.number)
        self.assertEqual('default', agent.context)
        self.assertEqual([5], agent.users)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'commented': None,
            'context': 'default',
            'firstname': 'Agent',
            'id': 1,
            'language': '',
            'lastname': '1',
            'number': '*1',
            'passwd': 'password123',
        }

        agent = Agent.from_list_obj_dict(obj_dict)

        self.assertEqual(1, agent.id)
        self.assertEqual('Agent', agent.firstname)
        self.assertEqual('1', agent.lastname)
        self.assertEqual('password123', agent.password)
        self.assertEqual('*1', agent.number)
        self.assertEqual('default', agent.context)
