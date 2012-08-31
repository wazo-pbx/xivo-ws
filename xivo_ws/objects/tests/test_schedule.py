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
                                'description': ''
                              },
                             'dialaction': {
                                 'schedule_fallback': {
                                        "actiontype": 'endcall',
                                        "action": 'hangup'
                                    }
                             },
                             'opened': [
                                        {'hours': '08:00-12:00',
                                         'weekdays': '1-5',
                                         'monthdays': '1-31',
                                         'months': '1-12'
                                        }
                                    ],
                             'closed': []
                             }
        opened = [
                {
                    "hours": "08:00-12:00",
                    "weekdays": "1-5",
                    "monthdays": "1-31",
                    "months": "1-12",
                }
            ]
        schedule = Schedule(name='huit_a_midi',
                        timezone='America/Montreal',
                        fallback_action='endcall:hangup',
                        description='',
                        opened=opened,
                        closed=[])

        obj_dict = schedule.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_with_no_dialaction(self):
        expected_obj_dict = {'schedule': {
                                'name': 'test',
                                'timezone': 'America/Montreal',
                                'description': ''
                              },
                             'dialaction': {
                                 'schedule_fallback': {
                                        "actiontype": 'none'
                                    }
                             },
                             'opened': [
                                        {'hours': '08:00-12:00',
                                         'weekdays': '1-5',
                                         'monthdays': '1-31',
                                         'months': '1-12'
                                        }
                                    ],
                             'closed': []
                             }
        opened = [
                {
                    "hours": "08:00-12:00",
                    "weekdays": "1-5",
                    "monthdays": "1-31",
                    "months": "1-12",
                }
            ]
        schedule = Schedule(name='test',
                        timezone='America/Montreal',
                        fallback_action=None,
                        description='',
                        opened=opened,
                        closed=[])

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
                     'opened': [
                                {
                                "id": 1,
                                "schedule_id": 1,
                                "mode": "opened",
                                "hours": "08:00-12:00",
                                "weekdays": "1-5",
                                "monthdays": "1-31",
                                "months": "1-12",
                                "action": None,
                                "actionid": None,
                                "actionargs": None,
                                "commented": False

                                }
                     ],
                     'closed': False
                     }
        expected_opened = [
                {
                    "id": 1,
                    "schedule_id": 1,
                    "mode": 'opened',
                    "hours": "08:00-12:00",
                    "weekdays": "1-5",
                    "monthdays": "1-31",
                    "months": "1-12",
                    "action": None,
                    "actionid": None,
                    "actionargs": None,
                    "commented": False
                }
            ]

        schedule = Schedule.from_obj_dict(obj_dict)

        self.assertEqual(1, schedule.id)
        self.assertEqual('huit_a_midi', schedule.name)
        self.assertEqual('America/Montreal', schedule.timezone)
        self.assertEqual('endcall:hangup', schedule.fallback_action)
        self.assertEqual('', schedule.description)
        self.assertEqual(expected_opened, schedule.opened)

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
        self.assertEqual('', schedule.description)
