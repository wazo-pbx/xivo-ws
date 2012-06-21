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


class Incall(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('number', required=True),
        Attribute('context', required=True),
        Attribute('destination', required=True),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_incall(obj_dict)
        self._to_dialaction(obj_dict)

    def _to_incall(self, obj_dict):
        incall = {
            u'exten': self.number,
            u'context': self.context,
        }
        obj_dict[u'incall'] = incall

    def _to_dialaction(self, obj_dict):
        self.destination._to_dialaction(obj_dict)

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict[u'id'])
        obj.number = obj_dict[u'exten']
        obj.context = obj_dict[u'context']
        return obj


class IncallQueueDestination(object):
    def __init__(self, queue_id):
        self.queue_id = queue_id

    def _to_dialaction(self, obj_dict):
        dialaction = {
            u'answer': {
                u'actiontype': u'queue',
                u'actionarg1': self.queue_id,
                u'actionarg2': u'',
            }
        }
        obj_dict['dialaction'] = dialaction


class IncallWebService(AbstractWebService):
    _PATH = u'/service/ipbx/json.php/restricted/call_management/incall/'
    _OBJECT_CLASS = Incall

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(IncallWebService, 'incall')
