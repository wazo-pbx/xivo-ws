# -*- coding: utf-8 -*-

# Copyright (C) 2012-2014 Avencall
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
from xivo_ws.objects.statconf import Statconf


class TestStatconf(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'stats_conf': {
                'name': 'conf_1',
                'hour_start': '08:00',
                'hour_end': '20:00',
                'dbegcache': '2012-01',
                'dendcache': 0,
                'default_delta': 0,
                'timezone': None,
                'period1': '0-10',
                'period2': '10-20',
                'period3': '20-30',
                'period4': '30-40',
                'period5': '40',
                'monday': True,
                'tuesday': None,
                'wednesday': None,
                'thursday': None,
                'friday': None,
                'saturday': None,
                'sunday': None
            }
        }
        stat_conf = Statconf(name='conf_1',
                        hour_start='08:00',
                        hour_end='20:00',
                        dbegcache='2012-01',
                        monday=True)

        obj_dict = stat_conf.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'id': '1',
            'name': 'conf_1',
            'hour_start': '08:00',
            'hour_end': '20:00',
            'dbegcache': '2012-01',
            'dendcache': 0,
            'default_delta': 0,
            'timezone': None,
            'period1': '0-10',
            'period2': '10-20',
            'period3': '20-30',
            'period4': '30-40',
            'period5': '40',
            'monday': True,
            'tuesday': None,
            'wednesday': None,
            'thursday': None,
            'friday': None,
            'saturday': None,
            'sunday': None
        }

        stat_conf = Statconf.from_list_obj_dict(obj_dict)

        self.assertEqual(1, stat_conf.id)
        self.assertEqual('conf_1', stat_conf.name)
        self.assertEqual('0-10', stat_conf.period1)
        self.assertEqual(True, stat_conf.monday)
        self.assertEqual(None, stat_conf.wednesday)
