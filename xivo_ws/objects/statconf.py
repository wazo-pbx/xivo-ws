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


class Statconf(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('hour_start', required=True),
        Attribute('hour_end', required=True),
        Attribute('dbegcache', required=True),
        Attribute('dendcache', required=True, default=0),
        Attribute('default_delta', required=True, default=0),
        Attribute('timezone'),
        Attribute('period1', required=True, default='0-10'),
        Attribute('period2', default='10-20'),
        Attribute('period3', default='20-30'),
        Attribute('period4', default='30-40'),
        Attribute('period5', default='40'),
        Attribute('monday'),
        Attribute('tuesday'),
        Attribute('wednesday'),
        Attribute('thursday'),
        Attribute('friday'),
        Attribute('saturday'),
        Attribute('sunday'),
        Attribute('queue', default_factory=list),
        Attribute('queue_qos'),
        Attribute('agent', default_factory=list),
        Attribute('xivouser', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._add_stats_conf(obj_dict)
        self._add_queue(obj_dict)
        self._add_agent(obj_dict)
        self._add_xivouser(obj_dict)

    def _add_stats_conf(self, obj_dict):
        obj_dict['stats_conf'] = {
            'name': self.name,
            'hour_start': self.hour_start,
            'hour_end': self.hour_end,
            'dbegcache': self.dbegcache,
            'dendcache': self.dendcache,
            'default_delta': self.default_delta,
            'timezone': self.timezone,
            'period1': self.period1,
            'period2': self.period2,
            'period3': self.period3,
            'period4': self.period4,
            'period5': self.period5,
            'monday': self.monday,
            'tuesday': self.tuesday,
            'wednesday': self.wednesday,
            'thursday': self.thursday,
            'friday': self.friday,
            'saturday': self.saturday,
            'sunday': self.sunday,
        }

    def _add_queue(self, obj_dict):
        if self.queue:
            if not self.queue_qos:
                raise ValueError('You must set queue_qos')
            obj_dict['queue'] = list(self.queue)
            obj_dict['queue_qos'] = self.queue_qos

    def _add_agent(self, obj_dict):
        if self.agent:
            obj_dict['agent'] = list(self.agent)

    def _add_xivouser(self, obj_dict):
        if self.xivouser:
            obj_dict['xivouser'] = list(self.xivouser)

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.timezone = obj_dict['timezone']
        obj.hour_start = obj_dict['hour_start']
        obj.hour_end = obj_dict['hour_end']
        obj.dbegcache = obj_dict['dbegcache']
        obj.dendcache = obj_dict['dendcache']
        obj.default_delta = obj_dict['default_delta']
        obj.period1 = obj_dict['period1']
        obj.period2 = obj_dict['period2']
        obj.period3 = obj_dict['period3']
        obj.period4 = obj_dict['period4']
        obj.period5 = obj_dict['period5']
        obj.monday = obj_dict['monday']
        obj.tuesday = obj_dict['tuesday']
        obj.wednesday = obj_dict['wednesday']
        obj.thursday = obj_dict['thursday']
        obj.friday = obj_dict['friday']
        obj.saturday = obj_dict['saturday']
        obj.sunday = obj_dict['sunday']
        return obj


class StatconfWebService(AbstractWebService):
    _PATH = '/statistics/call_center/json.php/restricted/settings/configuration/'
    _OBJECT_CLASS = Statconf

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(StatconfWebService, 'statconfs')
