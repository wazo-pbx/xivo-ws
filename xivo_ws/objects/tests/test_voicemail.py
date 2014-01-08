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
from xivo_ws.objects.voicemail import Voicemail


class TestVoicemail(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {'voicemail': {
                                        'mailbox': '1200',
                                        'fullname': 'Voicemail',
                                        'password': None,
                                        'email': None,
                                        'tz': None,
                                    }
                             }
        voicemail = Voicemail(mailbox='1200',
                        fullname='Voicemail')

        obj_dict = voicemail.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {'voicemail': {
                            "uniqueid": "1",
                            "mailbox": "1200",
                            "fullname": "Mailbox Name",
                            "password": "",
                            "email": "toto@lol.com",
                            "tz": "eu-fr",
                            }
                    }

        voicemail = Voicemail.from_obj_dict(obj_dict)

        self.assertEqual(1, voicemail.id)
        self.assertEqual('1200', voicemail.mailbox)
        self.assertEqual('Mailbox Name', voicemail.fullname)
        self.assertEqual('', voicemail.password)
        self.assertEqual('toto@lol.com', voicemail.email)
        self.assertEqual('eu-fr', voicemail.tz)

    def test_from_list_obj_dict(self):
        obj_dict = {"uniqueid": "1",
                    "mailbox": "1200",
                    "fullname": "Mailbox Name",
                    "password": "",
                    "email": "toto@lol.com",
                    "tz": "eu-fr",
                    }

        voicemail = Voicemail.from_list_obj_dict(obj_dict)

        self.assertEqual(1, voicemail.id)
        self.assertEqual('1200', voicemail.mailbox)
        self.assertEqual('Mailbox Name', voicemail.fullname)
        self.assertEqual('', voicemail.password)
        self.assertEqual('toto@lol.com', voicemail.email)
        self.assertEqual('eu-fr', voicemail.tz)
