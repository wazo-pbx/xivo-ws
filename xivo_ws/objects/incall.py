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


class Incall(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('number', required=True),
        Attribute('context', required=True),
        Attribute('destination', required=True),
        Attribute('caller_id_mode'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._add_incall(obj_dict)
        self._add_dialaction(obj_dict)
        self._add_caller_id_mode(obj_dict)

    def _add_incall(self, obj_dict):
        obj_dict['incall'] = {
            'exten': self.number,
            'context': self.context,
        }

    def _add_dialaction(self, obj_dict):
        obj_dict['dialaction'] = {
            'answer': self.destination.to_obj_dict()
        }

    def _add_caller_id_mode(self, obj_dict):
        if self.caller_id_mode:
            obj_dict['callerid'] = self.caller_id_mode.to_obj_dict()

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.number = obj_dict['exten']
        obj.context = obj_dict['context']
        return obj


class IncallWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/call_management/incall/'
    _OBJECT_CLASS = Incall

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
    ]

    def search_by_number(self, number):
        number = unicode(number)
        incalls = self.search(number)
        return [incall for incall in incalls if incall.number == number]


register_ws_class(IncallWebService, 'incalls')
