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


class IAXTrunk(AbstractObject):
    TYPE_PEER = 'peer'
    TYPE_USER = 'user'
    TYPE_FRIEND = 'friend'

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('username'),
        Attribute('secret'),
        Attribute('context', required=True),
        Attribute('host'),
        Attribute('type', default=TYPE_PEER),
        Attribute('description'),
        Attribute('requirecalltoken', default='auto')
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_protocol(obj_dict)
        self._to_trunkfeatures(obj_dict)

    def _to_protocol(self, obj_dict):
        protocol = {
            'name': self.name,
            'context': self.context,
            'type': self.type,
        }
        if self.username is not None:
            protocol['username'] = self.username
        if self.secret is not None:
            protocol['secret'] = self.secret
        if self.host is None:
            protocol['host-type'] = 'dynamic'
        else:
            protocol.update({
                'host-type': 'static',
                'host-static': self.host,
            })
        if self.requirecalltoken is not None:
            protocol['requirecalltoken'] = self.requirecalltoken
        obj_dict['protocol'] = protocol

    def _to_trunkfeatures(self, obj_dict):
        trunkfeatures = {
            'description': self.description
        }
        obj_dict['trunkfeatures'] = trunkfeatures

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        return obj


class IAXTrunkWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/trunk_management/iax/'
    _OBJECT_CLASS = IAXTrunk

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.SEARCH,
        Actions.LIST,
    ]


register_ws_class(IAXTrunkWebService, 'iax_trunks')
# deprecated name
register_ws_class(IAXTrunkWebService, 'iax_trunk')
