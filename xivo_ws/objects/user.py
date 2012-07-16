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

from xivo_ws.objects.common import Attribute, AbstractObject, Actions, AbstractWebService
from xivo_ws.registry import register_ws_class


class User(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('firstname', required=True),
        Attribute('lastname'),
        Attribute('enable_client'),
        Attribute('client_username'),
        Attribute('client_password'),
        Attribute('client_profile'),
        Attribute('entity_id', required=True, default=1),
        Attribute('line'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_userfeatures(obj_dict)
        self._to_linefeatures(obj_dict)
        self._to_dialaction(obj_dict)

    def _to_userfeatures(self, obj_dict):
        userfeatures = {
            'musiconhold': 'default',
            'entityid': self.entity_id,
            # TODO check why default values for enablehint and enablexfer (and
            #      other that we don't see) aren't working
            'enablehint': True,
            'enablexfer': True,
            'firstname': self.firstname,
        }
        if self.lastname is not None:
            userfeatures['lastname'] = self.lastname
        if self.enable_client is not None:
            userfeatures['enableclient'] = self.enable_client
        if self.client_username is not None:
            userfeatures['loginclient'] = self.client_username
        if self.client_password is not None:
            userfeatures['passwdclient'] = self.client_password
        if self.client_profile is not None:
            userfeatures['profileclient'] = self.client_profile
        obj_dict['userfeatures'] = userfeatures

    def _to_linefeatures(self, obj_dict):
        if self.line:
            self.line._to_linefeatures(obj_dict)

    def _to_dialaction(self, obj_dict):
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
        obj.id = obj_dict['id']
        obj.firstname = obj_dict['firstname']
        obj.lastname = obj_dict['lastname']
        return obj


class UserLine(AbstractObject):
    _ATTRIBUTES = [
        Attribute('protocol', default='sip'),
        Attribute('context'),
        Attribute('number'),
    ]

    def _to_linefeatures(self, obj_dict):
        if self.protocol is None:
            raise ValueError('protocol must be given')
        if self.context is None:
            raise ValueError('context must be given')
        linefeatures = {
            'protocol': [self.protocol],
            'context': [self.context],
            'number': [self.number],
        }
        obj_dict['linefeatures'] = linefeatures


class UserWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/users/'
    _OBJECT_CLASS = User

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(UserWebService, 'user')
