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

from xivo_ws import XivoServer, Entity


ENTITIES = [
    Entity(name='entity1'),
    Entity(name='entity2'),
    Entity(name='entity3'),
]


def main():
    xivo_server = XivoServer('192.168.1.100', 'admin', 'password')
    delete_outcalls(xivo_server)
    delete_trunks(xivo_server)
    delete_contexts(xivo_server)
    delete_entities(xivo_server)


def delete_outcalls(xivo_server):
    print 'Deleting outcalls...'
    outcall_list = xivo_server.outcalls.list()
    outcall_by_name = dict((outcall.name, outcall.id) for outcall in outcall_list)
    for entity in ENTITIES:
        outcall_name = '%s-out' % entity.name
        outcall_id = outcall_by_name[outcall_name]
        xivo_server.outcalls.delete(outcall_id)


def delete_trunks(xivo_server):
    print 'Deleting SIP trunks...'
    trunk_list = xivo_server.sip_trunks.list()
    trunk_by_name = dict((trunk.name, trunk.id) for trunk in trunk_list)
    for entity in ENTITIES:
        # primary
        trunk_name = '%s-call-manager' % entity.name
        trunk_id = trunk_by_name[trunk_name]
        xivo_server.sip_trunks.delete(trunk_id)
        # backup
        trunk_name = '%s-sub-call-manager' % entity.name
        trunk_id = trunk_by_name[trunk_name]
        xivo_server.sip_trunks.delete(trunk_id)


def delete_contexts(xivo_server):
    print 'Deleting contexts...'
    for entity in ENTITIES:
        # outcall
        context_id = '%s-to-extern' % entity.name
        xivo_server.contexts.delete(context_id)
        # internal
        context_id = '%s-default' % entity.name
        xivo_server.contexts.delete(context_id)
        # incall
        context_id = '%s-from-extern' % entity.name
        xivo_server.contexts.delete(context_id)


def delete_entities(xivo_server):
    print 'Deleting entities...'
    entity_list = xivo_server.entities.list()
    entity_by_name = dict((entity.name, entity.id) for entity in entity_list)
    for entity in ENTITIES:
        entity_id = entity_by_name[entity.name]
        xivo_server.entities.delete(entity_id)


main()
