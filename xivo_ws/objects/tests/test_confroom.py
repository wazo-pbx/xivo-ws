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
from xivo_ws.objects.confroom import ConfRoom


class TestConfRooms(unittest.TestCase):

    def test_to_obj_dict(self):
        expected_obj_dict = {
            'meetmefeatures': {
                'name': 'foobar',
                'confno': '1234',
                'context': 'service',
                'maxusers': '0',
                'admin_typefrom': 'none',
                'user_mode': 'all',
                'user_announcejoinleave': 'no',
                'user_musiconhold': 'default',
            },
            'meetmeroom': {
                'confno': '1234',
            }
        }
        confroom = ConfRoom(name='foobar',
                            number='1234',
                            context='service')

        obj_dict = confroom.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            "meetmefeatures": {
                "admin_announcejoinleave": "no",
                "admin_announceusercount": False,
                "admin_closeconflastmarkedexit": False,
                "admin_enableexitcontext": False,
                "admin_exitcontext": None,
                "admin_externalid": None,
                "admin_identification": "pin",
                "admin_initiallymuted": False,
                "admin_internalid": None,
                "admin_mode": "all",
                "admin_moderationmode": False,
                "admin_musiconhold": None,
                "admin_poundexit": False,
                "admin_quiet": False,
                "admin_starmenu": False,
                "admin_typefrom": "none",
                "closeconfdurationexceeded": "0",
                "commented": "0",
                "confno": "4000",
                "context": "default",
                "description": "",
                "durationm": None,
                "emailbody": "Hello %{FULLNAME}$s,\nYou have been invited to join %{CONFNAME}$s conference room.\n\n* Date : %{CONFDATE}$s\n* Duration : %{CONFDURATION}$s minutes\n* Room number : %{CONFNUMBER}$s\n* PIN : %{CONFPIN}$s\n\nThanks.\n\n-- XiVO Conference Room --",
                "emailfrom": "no-reply+meetme@wazo.community",
                "emailfromname": "XIVO PBX",
                "emailsubject": "[XiVO] Invitation to join a conference room",
                "id": 8,
                "identity": "blue (4000@default)",
                "maxusers": "0",
                "meetmeid": 14,
                "name": "blue",
                "nbuserstartdeductduration": None,
                "noplaymsgfirstenter": False,
                "preprocess_subroutine": None,
                "record": False,
                "startdate": None,
                "talkerdetection": True,
                "talkeroptimization": True,
                "timeannounceclose": None,
                "user_announcejoinleave": "no",
                "user_announceusercount": False,
                "user_enableexitcontext": False,
                "user_exitcontext": None,
                "user_hiddencalls": False,
                "user_initiallymuted": False,
                "user_mode": "all",
                "user_musiconhold": "default",
                "user_poundexit": False,
                "user_quiet": False,
                "user_starmenu": False
            },
            "meetmeguest": False,
            "meetmeroom": {
                "cat_metric": "1",
                "category": "rooms",
                "commented": False,
                "confno": "4000",
                "filename": "meetme.conf",
                "id": 14,
                "pin": "",
                "pinadmin": "",
                "var_metric": "0",
                "var_name": "conf",
                "var_val": "4000"
            }
        }

        confroom = ConfRoom.from_obj_dict(obj_dict)

        self.assertEqual(8, confroom.id)
        self.assertEqual('blue', confroom.name)
        self.assertEqual('4000', confroom.number)
        self.assertEqual('default', confroom.context)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "admin_announcejoinleave": "no",
            "admin_announceusercount": "0",
            "admin_closeconflastmarkedexit": "0",
            "admin_enableexitcontext": "0",
            "admin_exitcontext": None,
            "admin_externalid": None,
            "admin_identification": "pin",
            "admin_initiallymuted": "0",
            "admin_internalid": None,
            "admin_mode": "all",
            "admin_moderationmode": "0",
            "admin_musiconhold": None,
            "admin_poundexit": "0",
            "admin_quiet": "0",
            "admin_starmenu": "0",
            "admin_typefrom": "none",
            "closeconfdurationexceeded": "0",
            "commented": False,
            "confno": "4000",
            "context": "default",
            "description": "",
            "durationm": None,
            "emailbody": "Hello %{FULLNAME}$s,\nYou have been invited to join %{CONFNAME}$s conference room.\n\n* Date : %{CONFDATE}$s\n* Duration : %{CONFDURATION}$s minutes\n* Room number : %{CONFNUMBER}$s\n* PIN : %{CONFPIN}$s\n\nThanks.\n\n-- XiVO Conference Room --",
            "emailfrom": "no-reply+meetme@wazo.community",
            "emailfromname": "XIVO PBX",
            "emailsubject": "[XiVO] Invitation to join a conference room",
            "id": "8",
            "identity": "blue (4000@default)",
            "maxusers": "0",
            "meetmeid": "14",
            "name": "blue",
            "nbuserstartdeductduration": None,
            "noplaymsgfirstenter": "0",
            "pin": "",
            "pinadmin": "",
            "preprocess_subroutine": None,
            "record": "0",
            "startdate": None,
            "talkerdetection": "1",
            "talkeroptimization": "1",
            "timeannounceclose": None,
            "user_announcejoinleave": "no",
            "user_announceusercount": "0",
            "user_enableexitcontext": "0",
            "user_exitcontext": None,
            "user_hiddencalls": "0",
            "user_initiallymuted": "0",
            "user_mode": "all",
            "user_musiconhold": "default",
            "user_poundexit": "0",
            "user_quiet": "0",
            "user_starmenu": "0"
        }

        confroom = ConfRoom.from_list_obj_dict(obj_dict)

        self.assertEqual(8, confroom.id)
        self.assertEqual('blue', confroom.name)
        self.assertEqual('4000', confroom.number)
        self.assertEqual('default', confroom.context)
