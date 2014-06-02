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


class Schedule(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('entity_id'),
        Attribute('name', required=True),
        Attribute('timezone', required=True),
        Attribute('fallback_action'),
        Attribute('description'),
        Attribute('opened', default_factory=list),
        Attribute('closed', default_factory=list),
    ]

    def __eq__(self, other):
        if self.name != other.name or self.timezone != other.timezone:
            return False

        return _same_hours(self.opened, other.opened) and _same_hours(self.closed, other.closed)

    def _to_obj_dict(self, obj_dict):
        self._to_schedule(obj_dict)
        self._to_dialaction(obj_dict)
        self._to_closed(obj_dict)
        self._to_opened(obj_dict)

    def _to_schedule(self, obj_dict):
        schedule = {
            'entity_id': self.entity_id,
            'name': self.name,
            'timezone': self.timezone,
            'description': self.description,
        }
        obj_dict['schedule'] = schedule

    def _to_dialaction(self, obj_dict):
        if self.fallback_action is None:
            dialaction = {
                'schedule_fallback': {
                        "actiontype": 'none'
                }
            }
        else:
            dialaction = {
                'schedule_fallback': {
                        "actiontype": self.fallback_action.split(':')[0],
                        "action": self.fallback_action.split(':')[1]
                }
            }
        obj_dict['dialaction'] = dialaction

    def _to_opened(self, obj_dict):
        obj_dict['opened'] = list(self.opened)

    def _to_closed(self, obj_dict):
        obj_dict['closed'] = list(self.closed)

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_schedule(obj_dict['schedule'])
        obj._from_opened(obj_dict['opened'])
        obj._from_closed(obj_dict['closed'])
        return obj

    def _from_schedule(self, schedule):
        self.id = int(schedule['id'])
        self.entity_id = int(schedule['entity_id'])
        self.name = schedule['name']
        self.timezone = schedule['timezone']
        self.fallback_action = schedule['fallback_action']
        self.description = schedule['description']

    def _from_closed(self, closed):
        self.closed = closed

    def _from_opened(self, opened):
        self.opened = opened

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_schedule(obj_dict)
        return obj


class ScheduleWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/call_management/schedule/'
    _OBJECT_CLASS = Schedule

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.VIEW,
    ]


def _same_hours(lefts, rights):
    if not lefts and not rights:
        return True

    if len(lefts) != len(rights):
        return False

    fields = ['hours', 'months', 'monthdays', 'weekdays']
    for i in xrange(len(lefts)):
        left, right = lefts[i], rights[i]
        for field in fields:
            if left[field] != right[field]:
                return False
    return True


register_ws_class(ScheduleWebService, 'schedules')
