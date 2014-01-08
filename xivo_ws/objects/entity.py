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


class Entity(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('display_name', required=True),
    ]

    def _to_obj_dict(self, obj_dict):
        obj_dict['name'] = self.name
        obj_dict['displayname'] = self.display_name

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.display_name = obj_dict['displayname']
        return obj

    from_list_obj_dict = from_obj_dict


class EntityWebService(AbstractWebService):
    _PATH = '/xivo/configuration/json.php/restricted/manage/entity/'
    _OBJECT_CLASS = Entity

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_name(self, name):
        name = unicode(name)
        entities = self.search(name)
        return [entity for entity in entities if entity.name == name]


register_ws_class(EntityWebService, 'entities')
