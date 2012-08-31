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


class Schedule(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('timezone', required=True),
        Attribute('fallback_action'),
        Attribute('fallback_actionid'),
        Attribute('fallback_actionargs'),
        Attribute('description'),
        Attribute('commented'),
        Attribute('opened', default_factory=list),
        Attribute('closed', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_schedule(obj_dict)
        self._to_dialaction(obj_dict)
        self._to_closed(obj_dict)
        self._to_opened(obj_dict)

    def _to_schedule(self, obj_dict):
        schedule = {
            'name': self.name,
            'timezone': self.timezone,
            'fallback_action': self.fallback_action,
            'fallback_actionid': self.fallback_actionid,
            'fallback_actionargs': self.fallback_actionargs,
            'description': self.description,
            'commented': self.commented,
        }
        obj_dict['schedule'] = schedule

    def _to_dialaction(self, obj_dict):
        dialaction = {
            'schedule_fallback': {
                    "actiontype": None,
                    "action": None,
                    "endcall": {
                        "action": None,
                        "actionarg1": None,
                        "actionarg2": None
                    },
            },
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
        self.name = schedule['name']
        self.timezone = schedule['timezone']
        self.fallback_action = schedule['fallback_action']
        self.fallback_actionid = schedule['fallback_actionid']
        self.fallback_actionargs = schedule['fallback_actionargs']
        self.description = schedule['description']
        self.commented = schedule['commented']

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
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(ScheduleWebService, 'schedules')
# deprecated name
register_ws_class(ScheduleWebService, 'schedule')
