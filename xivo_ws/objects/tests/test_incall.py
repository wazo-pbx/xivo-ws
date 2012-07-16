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
from xivo_ws.destination import QueueDestination
from xivo_ws.objects.incall import Incall


class TestIncall(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'incall': {
                'exten': '502',
                'context': 'from-extern',
            },
            'dialaction': {
                'answer': {
                    'actiontype': 'queue',
                    'actionarg1': '8',
                    'actionarg2': '',
                }
            }
        }
        incall = Incall(number='502',
                        context='from-extern',
                        destination=QueueDestination(
                            queue_id='8'))

        obj_dict = incall.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "action": "user",
            "actionarg1": "37",
            "actionarg2": None,
            "commented": False,
            "context": "from-extern",
            "description": "",
            "destidentity": "alex-dev dév",
            "destination": "user",
            "exten": "501",
            "groupcontext": None,
            "groupname": None,
            "groupnumber": None,
            "id": "18",
            "identity": "501 (from-extern)",
            "linked": True,
            "meetmecontext": None,
            "meetmename": None,
            "meetmenumber": None,
            "preprocess_subroutine": None,
            "queuecontext": None,
            "queuename": None,
            "queuenumber": None,
            "userfirstname": "alex-dev",
            "userlastname": "dév",
            "voicemailcontext": None,
            "voicemailfullname": None,
            "voicemailmailbox": None,
            "voicemenucontext": None,
            "voicemenuname": None,
            "voicemenunumber": None
        }

        incall = Incall.from_list_obj_dict(obj_dict)

        self.assertEqual(18, incall.id)
        self.assertEqual('501', incall.number)
        self.assertEqual('from-extern', incall.context)
