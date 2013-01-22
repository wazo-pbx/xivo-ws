# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 Avencall
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


class ConfRoom(AbstractObject):

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('number', required=True),
        Attribute('context', required=True),
    ]

    def _to_obj_dict(self, obj_dict):
        self._add_meetmefeatures(obj_dict)
        self._add_meetmeroom(obj_dict)

    def _add_meetmefeatures(self, obj_dict):
        obj_dict['meetmefeatures'] = {
            'name': self.name,
            'confno': self.number,
            'context': self.context,
            'maxusers': '0',
            'admin_typefrom': 'none',
            'user_mode': 'all',
            'user_announcejoinleave': 'no',
            'user_musiconhold': 'default',
        }

    def _add_meetmeroom(self, obj_dict):
        obj_dict['meetmeroom'] = {
            'confno': self.number
        }

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_meetmefeatures(obj_dict['meetmefeatures'])
        return obj

    def _from_meetmefeatures(self, meetmefeatures):
        self.id = int(meetmefeatures['id'])
        self.name = meetmefeatures['name']
        self.number = meetmefeatures['confno']
        self.context = meetmefeatures['context']

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_meetmefeatures(obj_dict)
        return obj


class ConfRoomWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/meetme/'
    _OBJECT_CLASS = ConfRoom

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_name(self, name):
        name = unicode(name)
        confrooms = self.search(name)
        return [confroom for confroom in confrooms if confroom.name == name]

    def search_by_number(self, number):
        number = unicode(number)
        confrooms = self.search(number)
        return [confroom for confroom in confrooms if confroom.number == number]


register_ws_class(ConfRoomWebService, 'confrooms')
