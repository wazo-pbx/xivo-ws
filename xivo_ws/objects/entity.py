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


class Entity(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('display_name', required=True),
    ]

    def _to_obj_dict(self, obj_dict):
        obj_dict[u'name'] = self.name
        obj_dict[u'displayname'] = self.display_name

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_entity(obj_dict)
        return obj

    def _from_entity(self, entity):
        self.id = int(entity[u'id'])
        self.name = entity[u'name']
        self.display_name = entity[u'displayname']

    from_list_obj_dict = from_obj_dict


class EntityWebService(AbstractWebService):
    _PATH = u'/xivo/configuration/json.php/restricted/manage/entity/'
    _OBJECT_CLASS = Entity

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(EntityWebService, 'entity')
