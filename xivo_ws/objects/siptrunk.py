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


class SIPTrunk(AbstractObject):
    TYPE_OUTGOING = u'peer'
    TYPE_INCOMING_OUTGOING = u'friend'

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('username'),
        Attribute('secret'),
        Attribute('context', required=True),
        Attribute('host'),
        Attribute('type'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_protocol(obj_dict)
        self._to_trunkfeatures(obj_dict)

    def _to_protocol(self, obj_dict):
        protocol = {
            u'transport': u'udp',
            u'name': self.name,
            u'context': self.context,
        }
        if self.username is not None:
            protocol[u'username'] = self.username
        if self.secret is not None:
            protocol[u'secret'] = self.secret
        if self.host is None:
            protocol[u'host-type'] = u'dynamic'
        else:
            protocol.update({
                u'host-type': u'static',
                u'host-static': self.host,
            })
        if self.type is not None:
            protocol[u'type'] = self.type
        obj_dict[u'protocol'] = protocol

    def _to_trunkfeatures(self, obj_dict):
        trunkfeatures = {}
        obj_dict[u'trunkfeatures'] = trunkfeatures

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_trunkfeatures(obj_dict)
        return obj

    def _from_trunkfeatures(self, trunkfeatures):
        self.id = trunkfeatures[u'id']
        self.name = trunkfeatures[u'name']


class SIPTrunkWebService(AbstractWebService):
    _PATH = u'/service/ipbx/json.php/restricted/trunk_management/sip/'
    _OBJECT_CLASS = SIPTrunk

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(SIPTrunkWebService, 'sip_trunk')
