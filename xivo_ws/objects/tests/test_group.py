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
from xivo_ws.objects.group import Group, GroupWebService
from mock import Mock


class TestGroup(unittest.TestCase):

    def test_to_obj_dict(self):
        expected_obj_dict = {
            'groupfeatures': {
                'name': 'huge',
                'number': '2034',
                'context': 'default',
                'timeout': '0'
                },
            'queue': {},
            'user': [1, 2, 3]
        }
        group = Group(name='huge',
                      number='2034',
                      context='default',
                      user_ids=[1, 2, 3])

        obj_dict = group.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            'groupfeatures': {
                'id': '1',
                'name': 'huge',
                'number': '2034',
                'context': 'default',
                'timeout': '0'
                },
            'queue': {},
            'user': [
                     {
                        "queue_name": "huge",
                        "interface": "SIP/imm1zf",
                        "penalty": "0",
                        "call-limit": "0",
                        "paused": None,
                        "commented": False,
                        "usertype": "user",
                        "userid": 6733,
                        "channel": "SIP",
                        "category": "group",
                        "skills": "user-6733",
                        "state_interface": ""
                    }
            ]
        }

        group = Group.from_obj_dict(obj_dict)

        self.assertEqual(1, group.id)
        self.assertEqual('huge', group.name)
        self.assertEqual('2034', group.number)
        self.assertEqual('default', group.context)
        self.assertEqual([6733], group.user_ids)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "category": "group",
            "commented": False,
            "context": "default",
            "deleted": False,
            "id": "8",
            "identity": "axelgroup (2060@default)",
            "name": "axelgroup",
            "nb_qmember": "1",
            "number": "2060",
            "preprocess_subroutine": None,
            "timeout": "0",
            "transfer_call": "0",
            "transfer_user": "0",
            "write_caller": "0",
            "write_calling": "0"
        }

        group = Group.from_list_obj_dict(obj_dict)

        self.assertEqual(8, group.id)
        self.assertEqual('axelgroup', group.name)
        self.assertEqual('2060', group.number)
        self.assertEqual('default', group.context)


class TestGroupWebService(unittest.TestCase):

    def test_search_by_number_using_integer(self):
        search_return_value = [Group(id=42, number='1010')]
        group_ws = self._new_group_ws_with_mocked_search(search_return_value)

        groups = group_ws.search_by_number(1010)

        self.assertEqual(search_return_value, groups)

    def _new_group_ws_with_mocked_search(self, search_return_value):
        group_ws = GroupWebService(None)
        group_ws.search = Mock()
        group_ws.search.return_value = search_return_value
        return group_ws

    def test_search_by_name_using_integer(self):
        search_return_value = [Group(id=42, name='1010')]
        group_ws = self._new_group_ws_with_mocked_search(search_return_value)

        groups = group_ws.search_by_name(1010)

        self.assertEqual(search_return_value, groups)
