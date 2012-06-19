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


class Context(AbstractObject):
    TYPE_INTERNAL = u'internal'
    TYPE_INCALL = u'incall'
    TYPE_OUTCALL = u'outcall'

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('display_name', required=True),
        Attribute('entity', required=True),
        Attribute('type', default=TYPE_INCALL, required=True),
        Attribute('context_include', default_factory=list),
        Attribute('users', default_factory=list),
        Attribute('groups', default_factory=list),
        Attribute('queues', default_factory=list),
        Attribute('conf_rooms', default_factory=list),
        Attribute('incalls', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_context(obj_dict)
        self._to_contextinclude(obj_dict)
        self._to_contextnumbers(obj_dict)

    def _to_context(self, obj_dict):
        context = {
            u'name': self.name,
            u'displayname': self.display_name,
            u'entity': self.entity,
            u'contexttype': self.type,
        }
        obj_dict[u'context'] = context

    def _to_contextinclude(self, obj_dict):
        if self.context_include:
            obj_dict[u'contextinclude'] = list(self.context_include)

    def _to_contextnumbers(self, obj_dict):
        contextnumbers = {}
        if self.users:
            contextnumbers[u'user'] = self._to_contextnumbers_value(self.users)
        if self.groups:
            contextnumbers[u'group'] = self._to_contextnumbers_value(self.groups)
        if self.queues:
            contextnumbers[u'queue'] = self._to_contextnumbers_value(self.queues)
        if self.conf_rooms:
            contextnumbers[u'meetme'] = self._to_contextnumbers_value(self.conf_rooms)
        if self.incalls:
            contextnumbers[u'incall'] = self._to_contextnumbers_value(self.incalls, include_didlength=True)
        if contextnumbers:
            obj_dict[u'contextnumbers'] = contextnumbers

    def _to_contextnumbers_value(self, list_, include_didlength=False):
        if include_didlength:
            return [{u'numberbeg': context_range.start, u'numberend': context_range.end, u'didlength': context_range.did_length} for
                    context_range in list_]
        else:
            return [{u'numberbeg': context_range.start, u'numberend': context_range.end} for
                    context_range in list_]

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_context(obj_dict[u'context'])
        return obj

    def _from_context(self, context):
        self.id = context[u'name']
        self.name = context[u'name']
        self.display_name = context[u'displayname']
        self.entity = context[u'entity']

    from_list_obj_dict = from_obj_dict


class ContextRange(object):
    def __init__(self, start=None, end=None, did_length=0):
        self.start = start
        self.end = end
        self.did_length = did_length

    def __eq__(self, other):
        return (self.start == other.start and
                self.end == other.end and
                self.did_length == other.did_length)

    def __ne__(self, other):
        return not self.__eq__(other)


class ContextWebService(AbstractWebService):
    _PATH = u'/service/ipbx/json.php/restricted/system_management/context/'
    _OBJECT_CLASS = Context

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(ContextWebService, 'context')
