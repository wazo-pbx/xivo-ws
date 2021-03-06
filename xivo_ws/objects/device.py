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


class Device(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('ip'),
        Attribute('mac'),
        Attribute('plugin'),
        Attribute('vendor'),
        Attribute('model'),
        Attribute('version'),
        Attribute('status'),
        Attribute('template_id')
    ]

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_device(obj_dict)
        return obj

    def _from_device(self, device):
        self.id = device.get('id')
        self.ip = device.get('ip')
        self.mac = device.get('mac')
        self.plugin = device.get('plugin')
        self.vendor = device.get('vendor')
        self.model = device.get('model')
        self.version = device.get('version')
        self.status = device.get('status')
        self.template_id = device.get('template_id')

    from_list_obj_dict = from_obj_dict


class DeviceWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/devices/'
    _OBJECT_CLASS = Device

    _ACTIONS = [
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(DeviceWebService, 'devices')
