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


class Context(AbstractObject):
    TYPE_INTERNAL = 'internal'
    TYPE_INCALL = 'incall'
    TYPE_OUTCALL = 'outcall'

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
            'name': self.name,
            'displayname': self.display_name,
            'entity': self.entity,
            'contexttype': self.type,
        }
        obj_dict['context'] = context

    def _to_contextinclude(self, obj_dict):
        if self.context_include:
            obj_dict['contextinclude'] = list(self.context_include)

    def _to_contextnumbers(self, obj_dict):
        contextnumbers = {}
        if self.users:
            contextnumbers['user'] = self._to_contextnumbers_value(self.users)
        if self.groups:
            contextnumbers['group'] = self._to_contextnumbers_value(self.groups)
        if self.queues:
            contextnumbers['queue'] = self._to_contextnumbers_value(self.queues)
        if self.conf_rooms:
            contextnumbers['meetme'] = self._to_contextnumbers_value(self.conf_rooms)
        if self.incalls:
            contextnumbers['incall'] = self._to_contextnumbers_value(self.incalls, include_didlength=True)
        if contextnumbers:
            obj_dict['contextnumbers'] = contextnumbers

    def _to_contextnumbers_value(self, list_, include_didlength=False):
        if include_didlength:
            return [{'numberbeg': context_range.start, 'numberend': context_range.end, 'didlength': context_range.did_length} for
                    context_range in list_]
        else:
            return [{'numberbeg': context_range.start, 'numberend': context_range.end} for
                    context_range in list_]

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_context(obj_dict['context'])
        obj._from_contextnumbers(obj_dict['contextnumbers'])
        return obj

    def _from_context(self, context):
        self.id = context['name']
        self.name = context['name']
        self.display_name = context['displayname']
        self.entity = context['entity']
        self.type = context['contexttype']

    def _from_contextnumbers(self, contextnumbers):
        if 'user' in contextnumbers:
            self.users = self._from_contextnumbers_value(contextnumbers['user'])
        if 'group' in contextnumbers:
            self.groups = self._from_contextnumbers_value(contextnumbers['group'])
        if 'queue' in contextnumbers:
            self.queues = self._from_contextnumbers_value(contextnumbers['queue'])
        if 'meetme' in contextnumbers:
            self.conf_rooms = self._from_contextnumbers_value(contextnumbers['meetme'])
        if 'incall' in contextnumbers:
            self.incalls = self._from_contextnumbers_value(contextnumbers['incall'], include_didlength=True)

    def _from_contextnumbers_value(self, list_, include_didlength=False):
        if include_didlength:
            return [ContextRange(self._to_int(entry['numberbeg']), self._to_int(entry['numberend']), self._to_int(entry['didlength'])) for
                    entry in list_]
        else:
            return [ContextRange(self._to_int(entry['numberbeg']), self._to_int(entry['numberend'])) for
                    entry in list_]

    def _to_int(self, number):
        try:
            return int(number)
        except ValueError:
            return ''

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

    def __repr__(self):
        return '<ContextRange (%s, %s, didlength=%s)>' % (self.start, self.end, self.did_length)


class ContextWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/system_management/context/'
    _OBJECT_CLASS = Context

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(ContextWebService, 'contexts')
# deprecated name
register_ws_class(ContextWebService, 'context')
