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


class Queue(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('display_name', required=True),
        Attribute('number', required=True),
        Attribute('context', required=True),
        Attribute('ring_strategy', default='ringall'),
        Attribute('autopause', default=True),
        Attribute('reachability_timeout'),
        Attribute('maxlen', default=0),
        Attribute('agents', default_factory=list),
        Attribute('joinempty'),
        Attribute('leavewhenempty'),
        Attribute('waittime'),
        Attribute('waitratio'),
        Attribute('schedule_id'),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_queuefeatures(obj_dict)
        self._to_queue(obj_dict)
        self._to_dialaction(obj_dict)
        self._to_agent(obj_dict)
        self._to_schedule(obj_dict)

    def _to_queuefeatures(self, obj_dict):
        queuefeatures = {
            'timeout': '0',
            'hitting_caller': True,
            'transfer_user': True,
            'name': self.name,
            'displayname': self.display_name,
            'number': self.number,
            'context': self.context,
            'waittime': self.waittime,
            'waitratio': self.waitratio,
        }
        obj_dict['queuefeatures'] = queuefeatures

    def _to_queue(self, obj_dict):
        queue = {
            'musicclass': 'default',
            'min-announce-frequency': '60',
            'announce-position': 'yes',
            'announce-position-limit': '5',
            'timeoutpriority': 'app',
            'ringinuse': True,
            'autofill': True,
            'setqueueentryvar': True,
            'setqueuevar': True,
            'maxlen': self.maxlen,
            'joinempty': self.joinempty,
            'leavewhenempty': self.leavewhenempty,
            'strategy': self.ring_strategy,
            'autopause': self.autopause,
        }
        if self.reachability_timeout is not None:
            queue['timeout'] = self.reachability_timeout
        obj_dict['queue'] = queue

    def _to_dialaction(self, obj_dict):
        dialaction = {
            'noanswer': {
                'actiontype': 'none',
            },
            'busy': {
                'actiontype': 'none',
            },
            'congestion': {
                'actiontype': 'none',
            },
            'chanunavail': {
                'actiontype': 'none',
            },
            'qwaittime': {
                'actiontype': 'none',
            },
            'qwaitratio': {
                'actiontype': 'none',
            },
        }
        obj_dict['dialaction'] = dialaction

    def _to_agent(self, obj_dict):
        obj_dict['agent'] = list(self.agents)

    def _to_schedule(self, obj_dict):
        if self.schedule_id is not None:
            obj_dict['schedule_id'] = int(self.schedule_id)

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_queuefeatures(obj_dict['queuefeatures'])
        obj._from_queue(obj_dict['queue'])
        if 'schedule_id' in obj_dict:
            obj._from_schedule_id(obj_dict['schedule_id'])
        return obj

    def _from_queuefeatures(self, queuefeatures):
        self.id = int(queuefeatures['id'])
        self.name = queuefeatures['name']
        self.display_name = queuefeatures['displayname']
        self.number = queuefeatures['number']
        self.context = queuefeatures['context']
        self.waittime = queuefeatures['waittime']
        self.waitratio = queuefeatures['waitratio']

    def _from_queue(self, queue):
        self.maxlen = queue['maxlen']
        self.joinempty = queue['joinempty']
        self.leavewhenempty = queue['leavewhenempty']

    def _from_schedule_id(self, schedule_id):
        self.schedule_id = int(schedule_id)

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_queuefeatures(obj_dict)
        return obj


class QueueWebService(AbstractWebService):
    _PATH = '/callcenter/json.php/restricted/settings/queues/'
    _OBJECT_CLASS = Queue

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(QueueWebService, 'queues')
# deprecated name
register_ws_class(QueueWebService, 'queue')
