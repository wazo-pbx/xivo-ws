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
        Attribute('ring_strategy', default=u'ringall'),
        Attribute('autopause', default=True),
        Attribute('reachability_timeout'),
        Attribute('agents', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_queuefeatures(obj_dict)
        self._to_queue(obj_dict)
        self._to_dialaction(obj_dict)
        self._to_agent(obj_dict)

    def _to_queuefeatures(self, obj_dict):
        queuefeatures = {
            u'timeout': u'0',
            u'hitting_caller': True,
            u'transfer_user': True,
            u'name': self.name,
            u'displayname': self.display_name,
            u'number': self.number,
            u'context': self.context,
        }
        obj_dict[u'queuefeatures'] = queuefeatures

    def _to_queue(self, obj_dict):
        queue = {
            u'musicclass': u'default',
            u'min-announce-frequency': u'60',
            u'announce-position': u'yes',
            u'announce-position-limit': u'5',
            u'timeoutpriority': u'app',
            u'ringinuse': True,
            u'autofill': True,
            u'setqueueentryvar': True,
            u'setqueuevar': True,
        }
        queue[u'strategy'] = self.ring_strategy
        if self.reachability_timeout is not None:
            queue[u'timeout'] = self.reachability_timeout
        queue[u'autopause'] = self.autopause
        obj_dict[u'queue'] = queue

    def _to_dialaction(self, obj_dict):
        dialaction = {
            u'noanswer': {
                u'actiontype': u'none',
            },
            u'busy': {
                u'actiontype': u'none',
            },
            u'congestion': {
                u'actiontype': u'none',
            },
            u'chanunavail': {
                u'actiontype': u'none',
            },
            u'qctipresence': {
                u'actiontype': u'none',
            },
            u'qnonctipresence': {
                u'actiontype': u'none',
            },
            u'qwaittime': {
                u'actiontype': u'none',
            },
            u'qwaitratio': {
                u'actiontype': u'none',
            },
        }
        obj_dict[u'dialaction'] = dialaction

    def _to_agent(self, obj_dict):
        obj_dict[u'agent'] = list(self.agents)

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_queuefeatures(obj_dict[u'queuefeatures'])
        return obj

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_queuefeatures(obj_dict)
        return obj

    def _from_queuefeatures(self, queuefeatures):
        self.id = int(queuefeatures[u'id'])
        self.name = queuefeatures[u'name']
        self.display_name = queuefeatures[u'displayname']
        self.number = queuefeatures[u'number']
        self.context = queuefeatures[u'context']


class QueueWebService(AbstractWebService):
    _PATH = u'/callcenter/json.php/restricted/settings/queues/'
    _OBJECT_CLASS = Queue

    _ACTIONS = [
        Actions.ADD,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(QueueWebService, 'queue')
