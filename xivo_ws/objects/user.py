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
        Attribute('line'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_userfeatures(obj_dict)
        self._to_linefeatures(obj_dict)
        self._to_dialaction(obj_dict)

    def _to_userfeatures(self, obj_dict):
        userfeatures = {
            u'musiconhold': u'default',
            u'entityid': 1,
            # TODO check why default values for enablehint and enablexfer (and
            #      other that we don't see) aren't working
            u'enablehint': True,
            u'enablexfer': True,
            u'firstname': self.firstname,
        }
        if self.lastname is not None:
            userfeatures[u'lastname'] = self.lastname
        if self.enable_client is not None:
            userfeatures[u'enableclient'] = self.enable_client
        if self.client_username is not None:
            userfeatures[u'loginclient'] = self.client_username
        if self.client_password is not None:
            userfeatures[u'passwdclient'] = self.client_password
        if self.client_profile is not None:
            userfeatures[u'profileclient'] = self.client_profile
        obj_dict[u'userfeatures'] = userfeatures

    def _to_linefeatures(self, obj_dict):
        if self.line:
            self.line._to_linefeatures(obj_dict)

    def _to_dialaction(self, obj_dict):
        dialaction = {
            u'noanswer': {
                u'actiontype': 'none',
            },
            u'busy': {
                u'actiontype': 'none',
            },
            u'congestion': {
                u'actiontype': 'none',
            },
            u'chanunavail': {
                u'actiontype': 'none',
            },
        }
        obj_dict[u'dialaction'] = dialaction

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_userfeatures(obj_dict)
        return obj

    def _from_userfeatures(self, userfeatures):
        self.id = userfeatures[u'id']
        self.firstname = userfeatures[u'firstname']
        self.lastname = userfeatures[u'lastname']


class UserLine(AbstractObject):
    _ATTRIBUTES = [
        Attribute('protocol', default=u'sip'),
        Attribute('context'),
        Attribute('number'),
    ]

    def _to_linefeatures(self, obj_dict):
        if self.protocol is None:
            raise ValueError(u'protocol must be given')
        if self.context is None:
            raise ValueError(u'context must be given')
        linefeatures = {
            u'protocol': [self.protocol],
            u'context': [self.context],
            u'number': [self.number],
        }
        obj_dict[u'linefeatures'] = linefeatures


class UserWebService(AbstractWebService):
    _PATH = u'/service/ipbx/json.php/restricted/pbx_settings/users/'
    _OBJECT_CLASS = User

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(UserWebService, 'user')
