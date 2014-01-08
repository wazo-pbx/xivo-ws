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

from xivo_ws.objects.common import Attribute, AbstractObject, Actions, AbstractWebService
from xivo_ws.registry import register_ws_class


class Voicemail(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('mailbox', required=True),
        Attribute('fullname', required=True),
        Attribute('password'),
        Attribute('email'),
        Attribute('tz'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_voicemail(obj_dict)

    def _to_voicemail(self, obj_dict):
        voicemail = {
            'mailbox': self.mailbox,
            'fullname': self.fullname,
            'password': self.password,
            'email': self.email,
            'tz': self.tz,
        }
        obj_dict['voicemail'] = voicemail

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_voicemail(obj_dict['voicemail'])
        return obj

    def _from_voicemail(self, voicemail):
        self.id = int(voicemail['uniqueid'])
        self.mailbox = voicemail['mailbox']
        self.fullname = voicemail['fullname']
        self.password = voicemail['password']
        self.email = voicemail['email']
        self.tz = voicemail['tz']

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_voicemail(obj_dict)
        return obj


class VoicemailWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/voicemail/'
    _OBJECT_CLASS = Voicemail

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_number(self, number):
        number = unicode(number)
        voicemails = self.search(number)
        return [voicemail for voicemail in voicemails if voicemail.mailbox == number]


register_ws_class(VoicemailWebService, 'voicemails')
