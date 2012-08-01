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


class Outcall(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('context', required=True),
        Attribute('trunks', default_factory=list),
        Attribute('extens', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        if not self.trunks:
            raise ValueError('at least 1 trunk must be specified')
        self._to_outcall(obj_dict)
        self._to_outcalltrunk(obj_dict)
        self._to_dialpattern(obj_dict)

    def _to_outcall(self, obj_dict):
        outcall = {
            'name': self.name,
            'context': self.context,
        }
        obj_dict['outcall'] = outcall

    def _to_outcalltrunk(self, obj_dict):
        obj_dict['outcalltrunk'] = list(self.trunks)

    def _to_dialpattern(self, obj_dict):
        if self.extens:
            # reverse and add a needed but meaningless one at the end of the list
            extens = list(reversed(self.extens))
            extens.append(OutcallExten(''))
            obj_dict['dialpattern'] = {
                'id': ['0' for _ in extens],
                'externprefix': ['' for _ in extens],
                'prefix': ['' for _ in extens],
                'exten': [exten.exten for exten in extens],
                'stripnum': [exten.stripnum for exten in extens],
                'callerid': ['' for _ in extens],
            }

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        return obj


class OutcallExten(object):
    def __init__(self, exten=None, stripnum=0):
        self.exten = exten
        self.stripnum = stripnum


class OutcallWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/call_management/outcall/'
    _OBJECT_CLASS = Outcall

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
    ]


register_ws_class(OutcallWebService, 'outcalls')
# deprecated name
register_ws_class(OutcallWebService, 'outcall')
