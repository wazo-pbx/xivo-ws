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
from xivo_ws.objects.schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {'schedule': {
                                'name': 'huit_a_midi',
                                'timezone': 'America/Montreal',
                                'fallback_action': 'endcall:hangup',
                                'fallback_actionid': None,
                                'fallback_actionargs': '',
                                'description': '',
                                'commented': 0,
                              },
                             'dialaction': {
                                 'schedule_fallback': {
                                        "actiontype": None,
                                        "action": None,
                                        "endcall": {
                                            "action": None,
                                            "actionarg1": None,
                                            "actionarg2": None
                                        },
                                    }
                             },
                             'opened': [],
                             'closed': []
                             }
        schedule = Schedule(name='huit_a_midi',
                        timezone='America/Montreal',
                        fallback_action='endcall:hangup',
                        fallback_actionid=None,
                        fallback_actionargs='',
                        description='',
                        commented=0)

        obj_dict = schedule.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {'schedule': {
                        'id': '1',
                        'name': 'huit_a_midi',
                        'timezone': 'America/Montreal',
                        'fallback_action': 'endcall:hangup',
                        'fallback_actionid': None,
                        'fallback_actionargs': '',
                        'description': '',
                        'commented': 0,
                      },
                     'dialaction': {
                         'schedule_fallback': {
                                "actiontype": None,
                                "action": None,
                                "endcall": {
                                    "action": None,
                                    "actionarg1": None,
                                    "actionarg2": None
                                },
                            }
                     },
                     'opened': False,
                     'closed': False
                     }

        schedule = Schedule.from_obj_dict(obj_dict)

        self.assertEqual(1, schedule.id)
        self.assertEqual('huit_a_midi', schedule.name)
        self.assertEqual('America/Montreal', schedule.timezone)
        self.assertEqual('endcall:hangup', schedule.fallback_action)
        self.assertEqual(None, schedule.fallback_actionid)
        self.assertEqual('', schedule.fallback_actionargs)
        self.assertEqual('', schedule.description)
        self.assertEqual(0, schedule.commented)

    def test_from_list_obj_dict(self):
        obj_dict = {'id': '1',
                    'name': 'huit_a_midi',
                    'timezone': 'America/Montreal',
                    'fallback_action': 'endcall:hangup',
                    'fallback_actionid': None,
                    'fallback_actionargs': '',
                    'description': '',
                    'commented': 0,
                    }

        schedule = Schedule.from_list_obj_dict(obj_dict)

        self.assertEqual(1, schedule.id)
        self.assertEqual('huit_a_midi', schedule.name)
        self.assertEqual('America/Montreal', schedule.timezone)
        self.assertEqual('endcall:hangup', schedule.fallback_action)
        self.assertEqual(None, schedule.fallback_actionid)
        self.assertEqual('', schedule.fallback_actionargs)
        self.assertEqual('', schedule.description)
        self.assertEqual(0, schedule.commented)
