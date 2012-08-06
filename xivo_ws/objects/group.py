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


class Group(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('number'),
        Attribute('context', required=True),
        Attribute('user_ids', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._add_groupfeatures(obj_dict)
        self._add_queue(obj_dict)
        self._add_user(obj_dict)

    def _add_groupfeatures(self, obj_dict):
        groupfeatures = {
            'name': self.name,
            'context': self.context,
            'timeout': '0'
        }
        if self.number is not None:
            groupfeatures['number'] = self.number
        obj_dict['groupfeatures'] = groupfeatures

    def _add_queue(self, obj_dict):
        obj_dict['queue'] = {}

    def _add_user(self, obj_dict):
        obj_dict['user'] = list(self.user_ids)

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.number = obj_dict['number']
        obj.context = obj_dict['context']
        return obj


class GroupWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/groups/'
    _OBJECT_CLASS = Group

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
    ]

    def search_by_number(self, number):
        number = str(number)
        groups = self.search(number)
        return [group for group in groups if group.number == number]

    def search_by_name(self, name):
        name = str(name)
        groups = self.search(name)
        return [group for group in groups if group.name == name]


register_ws_class(GroupWebService, 'groups')
# deprecated name
register_ws_class(GroupWebService, 'group')
