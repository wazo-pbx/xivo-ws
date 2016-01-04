# -*- coding: utf-8 -*-

# Copyright (C) 2012-2016 Avencall
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


class User(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('entity_id', required=True, default=1),
        Attribute('firstname', required=True),
        Attribute('lastname'),
        Attribute('language'),
        Attribute('agent_id'),
        Attribute('enable_client'),
        Attribute('client_username'),
        Attribute('client_password'),
        Attribute('client_profile'),
        Attribute('client_profile_id'),
        Attribute('enable_hint', default=True),
        Attribute('enable_transfer', default=True),
        Attribute('bsfilter', default='no'),
        Attribute('line'),
        Attribute('voicemail'),
        Attribute('mobile_number'),
    ]

    def _to_obj_dict(self, obj_dict):
        if self.voicemail is not None and self.language is None:
            raise ValueError('language must be set when adding voicemail')
        self._add_userfeatures(obj_dict)
        self._add_line(obj_dict)
        self._add_voicemail(obj_dict)
        self._add_dialaction(obj_dict)

    def _add_userfeatures(self, obj_dict):
        userfeatures = {
            'musiconhold': 'default',
            'entityid': self.entity_id,
            # TODO check why default values for enablexfer (and
            #      other that we don't see) aren't working
            'enablexfer': True,
            'firstname': self.firstname,
        }
        if self.lastname is not None:
            userfeatures['lastname'] = self.lastname
        if self.language is not None:
            userfeatures['language'] = self.language
        if self.enable_client is not None:
            userfeatures['enableclient'] = self.enable_client
        if self.client_username is not None:
            userfeatures['loginclient'] = self.client_username
        if self.client_password is not None:
            userfeatures['passwdclient'] = self.client_password
        if self.client_profile is not None:
            userfeatures['profileclient'] = self.client_profile
        elif self.client_profile_id is not None:
            userfeatures['cti_profile_id'] = self.client_profile_id
        if self.enable_hint is not None:
            userfeatures['enablehint'] = self.enable_hint
        if self.agent_id is not None:
            userfeatures['agentid'] = self.agent_id
        if self.bsfilter is not None:
            userfeatures['bsfilter'] = self.bsfilter
        if self.mobile_number is not None:
            userfeatures['mobilephonenumber'] = self.mobile_number
        obj_dict['userfeatures'] = userfeatures

    def _add_line(self, obj_dict):
        if self.line:
            self.line._add_line(obj_dict)

    def _add_voicemail(self, obj_dict):
        if self.voicemail:
            self.voicemail._add_voicemail(obj_dict)

    def _add_dialaction(self, obj_dict):
        dialaction = {
            'noanswer': {
                'actiontype': 'none',
            },
            'busy': {
                'actiontype': 'none',
            },
            'congestion': {
                'actiontype': 'none',
            },
            'chanunavail': {
                'actiontype': 'none',
            },
        }
        obj_dict['dialaction'] = dialaction

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.entity_id = obj_dict['entityid']
        obj.firstname = obj_dict['firstname']
        obj.lastname = obj_dict['lastname']
        obj.enable_client = obj_dict['enableclient']
        obj.client_username = obj_dict['loginclient']
        obj.client_password = obj_dict['passwdclient']
        obj.client_profile_id = obj_dict['cti_profile_id']
        obj.bsfilter = obj_dict['bsfilter']
        obj.enable_transfer = obj_dict['enablexfer']
        if obj_dict['agentid']:
            obj.agent_id = int(obj_dict['agentid'])
        obj.mobile_number = obj_dict['mobilephonenumber']
        return obj


class UserLine(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('protocol', default='sip', required=True),
        Attribute('context', required=True),
        Attribute('secret'),
        Attribute('number'),
        Attribute('device_id'),
        Attribute('device_slot'),
    ]

    def _add_line(self, obj_dict):
        if self.id is not None:
            linefeatures = {
                'id': [self.id]
            }
        else:
            self._check_required_attributes()
            linefeatures = {
                'protocol': [self.protocol],
                'context': [self.context],
                'number': [self.number],
                'secret': [self.secret]
            }
        if self.device_id is not None:
            linefeatures['device'] = [self.device_id]
        if self.device_slot is not None:
            linefeatures['num'] = [self.device_slot]
        obj_dict['linefeatures'] = linefeatures


class UserVoicemail(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('number', required=True),
        Attribute('context', required=True),
        Attribute('password'),
    ]

    def _add_voicemail(self, obj_dict):
        self._check_required_attributes()
        voicemail_dict = {
            'name': self.name,
            'number': self.number,
            'context': self.context
        }
        if self.password is not None:
            voicemail_dict['password'] = self.password
        obj_dict['voicemail'] = voicemail_dict


class UserWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/users/'
    _OBJECT_CLASS = User

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(UserWebService, 'users')
