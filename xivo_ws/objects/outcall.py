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

from operator import itemgetter
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
        self._add_outcall(obj_dict)
        self._add_outcalltrunk(obj_dict)
        self._add_dialpattern(obj_dict)

    def _add_outcall(self, obj_dict):
        obj_dict['outcall'] = {
            'name': self.name,
            'context': self.context,
        }

    def _add_outcalltrunk(self, obj_dict):
        obj_dict['outcalltrunk'] = list(self.trunks)

    def _add_dialpattern(self, obj_dict):
        if self.extens:
            exten_dicts = [exten.to_obj_dict() for exten in reversed(self.extens)]
            dialpattern = {}
            for key in exten_dicts[0]:
                dialpattern[key] = map(itemgetter(key), exten_dicts)
                dialpattern[key].append('')
            obj_dict['dialpattern'] = dialpattern

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.context = obj_dict['context']
        return obj


class OutcallExten(AbstractObject):
    _ATTRIBUTES = [
        Attribute('exten', required=True),
        Attribute('stripnum', default=0, required=True),
        Attribute('caller_id', default='', required=True),
    ]

    def _to_obj_dict(self, obj_dict):
        obj_dict.update({
            'id': '0',
            'externprefix': '',
            'prefix': '',
            'exten': self.exten,
            'stripnum': self.stripnum,
            'callerid': self.caller_id,
        })


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
