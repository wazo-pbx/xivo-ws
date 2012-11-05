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
from xivo_ws.objects.queueskillrules import QueueSkillRules


class TestQueueSkillRules(unittest.TestCase):

    def test_to_obj_dict(self):
        expected_obj_dict = {
            'name': 'test_rule',
            'rule': ["anthropology > 70"]
        }
        skill = QueueSkillRules(name='test_rule',
                        rule=["anthropology > 70"])

        obj_dict = skill.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            'id': '1',
            'name': 'test_rule',
            'rule': ["anthropology > 70"]
        }

        skill = QueueSkillRules.from_obj_dict(obj_dict)

        self.assertEqual(1, skill.id)
        self.assertEqual('test_rule', skill.name)
        self.assertEqual(["anthropology > 70"], skill.rule)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'id': '1',
            'name': 'test_rule',
            'rule': ["anthropology > 70"]
        }

        skill = QueueSkillRules.from_obj_dict(obj_dict)

        self.assertEqual(1, skill.id)
        self.assertEqual('test_rule', skill.name)
        self.assertEqual(["anthropology > 70"], skill.rule)
