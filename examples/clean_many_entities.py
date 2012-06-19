#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from xivo_ws import XivoServer, Entity, Context, ContextRange, SIPTrunk, \
    Outcall, OutcallExten


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
    outcall_list = xivo_server.outcall.list()
    outcall_by_name = dict((outcall.name, outcall.id) for outcall in outcall_list)
    for entity in ENTITIES:
        outcall_name = '%s-out' % entity.name
        outcall_id = outcall_by_name[outcall_name]
        xivo_server.outcall.delete(outcall_id)


def delete_trunks(xivo_server):
    print 'Deleting SIP trunks...'
    trunk_list = xivo_server.sip_trunk.list()
    trunk_by_name = dict((trunk.name, trunk.id) for trunk in trunk_list)
    for entity in ENTITIES:
        # primary
        trunk_name = '%s-call-manager' % entity.name
        trunk_id = trunk_by_name[trunk_name]
        xivo_server.sip_trunk.delete(trunk_id)
        # backup
        trunk_name = '%s-sub-call-manager' % entity.name
        trunk_id = trunk_by_name[trunk_name]
        xivo_server.sip_trunk.delete(trunk_id)


def delete_contexts(xivo_server):
    print 'Deleting contexts...'
    for entity in ENTITIES:
        # outcall
        context_id = '%s-to-extern' % entity.name
        xivo_server.context.delete(context_id)
        # internal
        context_id = '%s-default' % entity.name
        xivo_server.context.delete(context_id)
        # incall
        context_id = '%s-from-extern' % entity.name
        xivo_server.context.delete(context_id)


def delete_entities(xivo_server):
    print 'Deleting entities...'
    entity_list = xivo_server.entity.list()
    entity_by_name = dict((entity.name, entity.id) for entity in entity_list)
    for entity in ENTITIES:
        entity_id = entity_by_name[entity.name]
        xivo_server.entity.delete(entity_id)


main()
