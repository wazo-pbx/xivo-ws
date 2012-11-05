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


class Agent(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('firstname', required=True),
        Attribute('lastname'),
        Attribute('password'),
        Attribute('number', required=True),
        Attribute('context', required=True),
        Attribute('wrapuptime', required=True, default='0'),
        Attribute('users', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        self._to_agentfeatures(obj_dict)
        self._to_userselect(obj_dict)

    def _to_agentfeatures(self, obj_dict):
        agentfeatures = {
            'numgroup': '1',
            'autologoff': '0',
            'firstname': self.firstname,
            'number': self.number,
            'context': self.context,
            'wrapuptime': self.wrapuptime
        }
        if self.lastname is not None:
            agentfeatures['lastname'] = self.lastname
        if self.password is not None:
            agentfeatures['passwd'] = self.password
        obj_dict['agentfeatures'] = agentfeatures

    def _to_userselect(self, obj_dict):
        obj_dict['user-select'] = list(self.users)

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_agentfeatures(obj_dict['agentfeatures'])
        obj._from_usermember(obj_dict['usermember'])
        return obj

    def _from_agentfeatures(self, agentfeatures):
        self.id = agentfeatures['id']
        self.firstname = agentfeatures['firstname']
        self.lastname = agentfeatures['lastname']
        self.password = agentfeatures['passwd']
        self.number = agentfeatures['number']
        self.context = agentfeatures['context']
        if 'wrapuptime' in agentfeatures:
            self.wrapuptime = agentfeatures['wrapuptime']

    def _from_usermember(self, usermember):
        if usermember:
            self.users = [user['id'] for user in usermember]

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_agentfeatures(obj_dict)
        return obj


class AgentWebService(AbstractWebService):
    _PATH = '/callcenter/json.php/restricted/settings/agents/'
    _OBJECT_CLASS = Agent

    _ACTIONS = [
        Actions.ADD,
        Actions.EDIT,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_number(self, number):
        number = unicode(number)
        agents = self.search(number)
        return [agent for agent in agents if agent.number == number]

    def find_one_by_number(self, number):
        agents = self.search_by_number(number)
        nb_agents = len(agents)
        if nb_agents == 1:
            return agents[0]
        elif nb_agents == 0:
            raise Exception('no agent with number %s' % number)
        else:
            raise Exception('%d agents with number %s' % (nb_agents, number))


register_ws_class(AgentWebService, 'agents')
