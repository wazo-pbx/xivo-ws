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
from xivo_ws.objects.group import Group


class TestGroup(unittest.TestCase):

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

    def test_to_obj_dict(self):
        expected = {
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

        self.assertEqual(expected, obj_dict)
