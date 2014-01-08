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
from xivo_ws.objects.cti_profile import CTIProfile


class TestCTIProfile(unittest.TestCase):
    def test_from_list_obj_dict(self):
        obj_dict = {
            "id": 6,
            "name": "profile-name",
            "presence_id": "1",
            "phonehints_id": "1",
            "deletable": True,
        }

        cti_profile = CTIProfile.from_list_obj_dict(obj_dict)

        self.assertEqual(cti_profile.id, 6)
        self.assertEqual(cti_profile.name, "profile-name")
