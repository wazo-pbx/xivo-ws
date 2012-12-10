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


class CTIProfile(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name'),
    ]

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        return obj


class CTIProfileWebService(AbstractWebService):
    _PATH = '/cti/json.php/restricted/profiles'
    _OBJECT_CLASS = CTIProfile

    _ACTIONS = [
        Actions.LIST,
    ]

register_ws_class(CTIProfileWebService, 'cti_profiles')
