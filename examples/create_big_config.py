#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013-2014 Avencall
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

from xivo_ws import XivoServer, Agent, Context, ContextRange, Incall, Queue, \
    User, UserLine, QueueDestination

INTERNAL_CONTEXT_NAME = 'default'
INCALL_CONTEXT_NAME = 'from-extern'

NB_AGENTS = 0

NB_USERS = 250
NB_USERS_PROFILE_SUPERVISOR = 0
USER_START_NO = 10000

NB_QUEUES = 0
NB_AGENTS_PER_QUEUE = 1
QUEUE_START_NO = 1000

INCALL_START_NO = QUEUE_START_NO


def main():
    xivo_server = XivoServer('skaro', 'admin', 'proformatique')
    remove_all_incalls(xivo_server)
    remove_all_queues(xivo_server)
    remove_all_agents(xivo_server)
    remove_all_users(xivo_server)
    remove_contexts(xivo_server)
    create_contexts(xivo_server)
    create_users(xivo_server)
    create_agents(xivo_server)
    create_queues(xivo_server)
    create_incalls(xivo_server)


def remove_all_incalls(xivo_server):
    print 'Removing all incoming calls...'
    xivo_server.incalls.delete_all()


def remove_all_queues(xivo_server):
    print 'Removing all queues...'
    # XXX webi doesn't support delete_all for queue web service
    for queue in xivo_server.queues.list():
        xivo_server.queues.delete(queue.id)


def remove_all_agents(xivo_server):
    print 'Removing all agents...'
    xivo_server.agents.delete_all()


def remove_all_users(xivo_server):
    print 'Removing all users... '
    xivo_server.users.delete_all()


def remove_contexts(xivo_server):
    for context_name in [INTERNAL_CONTEXT_NAME, INCALL_CONTEXT_NAME]:
        print 'Removing context "%s"...' % context_name
        xivo_server.contexts.delete_if_exists(context_name)


def create_contexts(xivo_server):
    print 'Fetching an entity name...'
    entities = xivo_server.entities.list()
    entity_name = entities[0].name
    if len(entities) > 1:
        print 'NOTE: contexts will be associated to entity "%s"' % entity_name

    print 'Creating context "%s"...' % INTERNAL_CONTEXT_NAME
    context = Context()
    context.name = INTERNAL_CONTEXT_NAME
    context.display_name = context.name
    context.entity = entity_name
    context.type = Context.TYPE_INTERNAL
    context.users = [ContextRange(USER_START_NO, USER_START_NO + NB_USERS - 1)]
    if NB_QUEUES > 0:
        context.queues = [ContextRange(QUEUE_START_NO, QUEUE_START_NO + NB_QUEUES - 1)]
    xivo_server.contexts.add(context)

    print 'Creating context "%s"...' % INCALL_CONTEXT_NAME
    context = Context()
    context.name = INCALL_CONTEXT_NAME
    context.display_name = context.name
    context.entity = entity_name
    context.type = Context.TYPE_INCALL
    if NB_QUEUES > 0:
        context.incalls = [ContextRange(INCALL_START_NO, INCALL_START_NO + NB_QUEUES - 1,
                                        did_length=len(str(INCALL_START_NO)))]
    xivo_server.contexts.add(context)


def create_users(xivo_server):
    current_user_no = 0
    users = []
    print 'Preparing %s users with "agent" profile...' % NB_AGENTS
    for agent_no in xrange(NB_AGENTS):
        user = User()
        user.firstname = 'Agent %04d' % agent_no
        user.enable_client = True
        user.client_username = 'agent%s' % agent_no
        user.client_password = user.client_username
        user.client_profile = 'Agent'
        user.line = UserLine()
        user.line.context = INTERNAL_CONTEXT_NAME
        user.line.number = USER_START_NO + current_user_no
        users.append(user)
        current_user_no += 1

    print 'Preparing %s users with "supervisor" profile...' % NB_USERS_PROFILE_SUPERVISOR
    for supervisor_no in xrange(NB_USERS_PROFILE_SUPERVISOR):
        user = User()
        user.firstname = 'Supervisor %04d' % supervisor_no
        user.enable_client = True
        user.client_username = 'super%s' % supervisor_no
        user.client_password = user.client_username
        user.client_profile = 'Supervisor'
        user.line = UserLine()
        user.line.context = INTERNAL_CONTEXT_NAME
        user.line.number = USER_START_NO + current_user_no
        users.append(user)
        current_user_no += 1

    nb_remaining_users = max(NB_USERS - current_user_no, 0)
    print 'Preparing %s users with no profile...' % nb_remaining_users
    for user_no in xrange(nb_remaining_users):
        user = User()
        user.firstname = 'User %04d' % user_no
        user.line = UserLine()
        user.line.context = INTERNAL_CONTEXT_NAME
        user.line.number = USER_START_NO + current_user_no
        users.append(user)
        current_user_no += 1

    print 'Importing users...'
    xivo_server.users.import_(users)


def create_agents(xivo_server):
    print 'Fetching user IDs of agents...'
    user_list = xivo_server.users.search('Agent')
    user_by_firstname = dict((user.firstname, user.id) for user in user_list)

    print 'Creating %s agents...' % NB_AGENTS
    for agent_no in xrange(NB_AGENTS):
        agent = Agent()
        agent.firstname = 'Agent %04d' % agent_no
        agent.number = agent_no
        agent.context = INTERNAL_CONTEXT_NAME
        agent.users = [user_by_firstname[agent.firstname]]
        xivo_server.agents.add(agent)


def create_queues(xivo_server):
    print 'Fetching agent IDs...'
    agent_list = xivo_server.agents.list()
    agent_ids = sorted(agent.id for agent in agent_list)

    print 'Creating %s queues...' % NB_QUEUES
    agents_iterator = _subseq_iterator(agent_ids, NB_AGENTS_PER_QUEUE)
    for queue_no in xrange(NB_QUEUES):
        queue = Queue()
        queue.name = 'queue%04d' % queue_no
        queue.display_name = queue.name
        queue.number = QUEUE_START_NO + queue_no
        queue.context = INTERNAL_CONTEXT_NAME
        queue.agents = agents_iterator.next()
        xivo_server.queues.add(queue)


def _subseq_iterator(seq, n):
    """
    >>> it = _subseq_iterator([1,2,3], 2)
    >>> it.next()
    [1, 2]
    >>> it.next()
    [3, 1]
    >>> it.next()
    [2, 3]

    """
    start = 0
    length = len(seq)
    while True:
        end = start + n
        sub_seq = seq[start:end]
        while end > length:
            end -= length
            sub_seq.extend(seq[:end])
        yield sub_seq
        start = end


def create_incalls(xivo_server):
    print 'Fetching queues IDs...'
    queue_list = xivo_server.queues.list()
    queue_ids = sorted(queue.id for queue in queue_list)

    print 'Creating %s incalls...' % NB_QUEUES
    for incall_no in xrange(NB_QUEUES):
        incall = Incall()
        incall.number = INCALL_START_NO + incall_no
        incall.context = INCALL_CONTEXT_NAME
        incall.destination = QueueDestination(queue_ids[incall_no])
        xivo_server.incalls.add(incall)


if __name__ == '__main__':
    main()
