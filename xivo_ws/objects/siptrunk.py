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


class SIPTrunk(AbstractObject):
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
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_protocol(obj_dict)
        self._to_trunkfeatures(obj_dict)

    def _to_protocol(self, obj_dict):
        protocol = {
            'transport': 'udp',
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
        obj_dict['protocol'] = protocol

    def _to_trunkfeatures(self, obj_dict):
        obj_dict['trunkfeatures'] = {}

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        return obj


class SIPTrunkWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/trunk_management/sip/'
    _OBJECT_CLASS = SIPTrunk

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
    ]

    def search_by_name(self, name):
        name = unicode(name)
        sip_trunks = self.search(name)
        return [sip_trunk for sip_trunk in sip_trunks if sip_trunk.name == name]


register_ws_class(SIPTrunkWebService, 'sip_trunks')
