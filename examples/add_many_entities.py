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

from xivo_ws import XivoServer, Entity, Context, ContextRange, SIPTrunk, \
    Outcall, OutcallExten


ENTITIES = [
    Entity(name='entity1', display_name='Entity1'),
    Entity(name='entity2', display_name='Entity2'),
    Entity(name='entity3', display_name='Entity3'),
]


def main():
    xivo_server = XivoServer('192.168.1.100', 'admin', 'password')
    add_entities(xivo_server)
    add_contexts(xivo_server)
    add_trunks(xivo_server)
    add_outcalls(xivo_server)


def add_entities(xivo_server):
    print 'Adding entities...'
    for entity in ENTITIES:
        xivo_server.entities.add(entity)


def add_contexts(xivo_server):
    print 'Adding contexts...'
    for entity in ENTITIES:
        outcall_context_name = '%s-to-extern' % entity.name
        # outcall context
        context = Context()
        context.entity = entity.name
        context.name = outcall_context_name
        context.display_name = '%s - to-extern' % entity.display_name
        context.type = Context.TYPE_OUTCALL
        xivo_server.contexts.add(context)
        # internal context
        context = Context()
        context.entity = entity.name
        context.name = '%s-default' % entity.name
        context.display_name = '%s - default' % entity.display_name
        context.type = Context.TYPE_INTERNAL
        context.context_include = [outcall_context_name]
        context.users = [ContextRange(1000, 1099)]
        xivo_server.contexts.add(context)
        # incall context
        context = Context()
        context.entity = entity.name
        context.name = '%s-from-extern' % entity.name
        context.display_name = '%s - from-extern' % entity.display_name
        context.type = Context.TYPE_INCALL
        xivo_server.contexts.add(context)


def add_trunks(xivo_server):
    print 'Adding SIP trunks...'
    for entity in ENTITIES:
        # primary
        sip_trunk = SIPTrunk()
        sip_trunk.name = '%s-call-manager' % entity.name
        sip_trunk.context = '%s-from-extern' % entity.name
        sip_trunk.host = '10.54.4.10'
        xivo_server.sip_trunks.add(sip_trunk)
        # backup
        sip_trunk = SIPTrunk()
        sip_trunk.name = '%s-sub-call-manager' % entity.name
        sip_trunk.context = '%s-from-extern' % entity.name
        sip_trunk.host = '10.74.4.10'
        xivo_server.sip_trunks.add(sip_trunk)


def add_outcalls(xivo_server):
    print 'Adding outcalls...'
    trunk_list = xivo_server.sip_trunks.list()
    trunk_by_name = dict((trunk.name, trunk.id) for trunk in trunk_list)
    for entity in ENTITIES:
        outcall = Outcall()
        outcall.name = '%s-out' % entity.name
        outcall.context = '%s-to-extern' % entity.name
        outcall.extens = [
            OutcallExten(exten='NXXNXXXXXX'),
            OutcallExten(exten='911'),
            OutcallExten(exten='9911'),
        ]
        outcall.trunks = [
            trunk_by_name['%s-call-manager' % entity.name],
            trunk_by_name['%s-sub-call-manager' % entity.name]
        ]
        xivo_server.outcalls.add(outcall)


main()
