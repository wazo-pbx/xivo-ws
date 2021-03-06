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


class CustomTrunk(AbstractObject):

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('interface', required=True),
        Attribute('protocol', default='custom'),
        Attribute('protocolid'),
        Attribute('registerid'),
        Attribute('registercommented'),
        Attribute('context'),
        Attribute('intfsuffix'),
        Attribute('category'),
        Attribute('registerid'),
        Attribute('description'),
        Attribute('commented')
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_protocol(obj_dict)
        self._to_trunkfeatures(obj_dict)

    def _to_protocol(self, obj_dict):
        protocol = {
            'name': self.name,
            'context': self.context,
            'interface': self.interface,
            'protocol': self.protocol,
        }
        obj_dict['protocol'] = protocol

    def _to_trunkfeatures(self, obj_dict):
        trunkfeatures = {
            'protocolid': self.protocolid,
            'registerid': self.registerid,
            'registercommented': self.registercommented,
            'description': self.description,
        }
        obj_dict['trunkfeatures'] = trunkfeatures

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.interface = obj_dict['interface']
        return obj


class CustomTrunkWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/trunk_management/custom/'
    _OBJECT_CLASS = CustomTrunk

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_name(self, name):
        name = unicode(name)
        custom_trunks = self.search(name)
        return [custom_trunk for custom_trunk in custom_trunks if
                custom_trunk.name == name]


register_ws_class(CustomTrunkWebService, 'custom_trunks')
