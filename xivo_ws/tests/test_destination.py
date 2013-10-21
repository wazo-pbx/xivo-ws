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
from xivo_ws.destination import QueueDestination, GroupDestination, UserDestination, VoicemailDestination


class TestGroupDestination(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'actiontype': 'group',
            'actionarg1': '1',
            'actionarg2': '',
        }
        dest = GroupDestination(group_id='1')

        obj_dict = dest.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)


class TestQueueDestination(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'actiontype': 'queue',
            'actionarg1': '1',
            'actionarg2': '',
        }
        dest = QueueDestination(queue_id='1')

        obj_dict = dest.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)


class TestUserDestination(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'actiontype': 'user',
            'actionarg1': '1',
            'actionarg2': '',
        }
        dest = UserDestination(user_id='1')

        obj_dict = dest.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)


class TestVoicemailDestination(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'actiontype': 'voicemail',
            'actionarg1': '1',
            'actionarg2': '',
        }
        dest = VoicemailDestination(voicemail_id='1')

        obj_dict = dest.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)
