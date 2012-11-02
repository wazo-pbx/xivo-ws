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
from xivo_ws.objects.sccp_general_settings import SCCPGeneralSettings


class TestSCCPGeneralSettings(unittest.TestCase):

    def test_to_obj_dict(self):
        expected_obj_dict = {
            'directmedia' : 1,
            'dialtimeout' : 5,
            'language'    : 'en_US'
        }

        settings = SCCPGeneralSettings(
            directmedia=True,
            dialtimeout=5,
            language='en_US'
        )

        obj_dict = settings.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            'sccpgeneralsettings': {
                'directmedia' : 0,
                'dialtimeout' : 6,
                'language'    : 'fr_FR'
            }
        }

        obj = SCCPGeneralSettings.from_obj_dict(obj_dict)

        self.assertEqual(False, obj.directmedia)
        self.assertEqual(6, obj.dialtimeout)
        self.assertEqual('fr_FR', obj.language)
