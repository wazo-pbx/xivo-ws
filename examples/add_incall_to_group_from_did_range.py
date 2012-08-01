#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from xivo_ws import XivoServer, Incall, GroupDestination

CONTEXT = 'from-extern'
DID_START = 6050
DID_STOP = 6099
GROUPPATTERN = 'groupe_%s'
XIVO_ADDR = '192.168.18.120'
WSUSER = 'admin'
WSPWD = 'adminpass'

# Goal : add several incall rules (DID) redirecting to existing groups matchine names like group_DID
# DID given through a range
# group basename as generic input
#
# 1st we look for the group in XiVO configuration through WebServices (to catch group ID)
# 2nd we create an incoming call rule with the DID in a given context redirecting to the found group (with its ID)

def build_incall_to_group(xivoserver, start, end, basename, context):
    xivo_server = XivoServer(xivoserver, WSUSER, WSPWD)

    group_list = xivo_server.groups.list()
    group_by_name = dict((group.name, group.id) for group in group_list)

    for i in xrange(start, end):
        group_name = basename % i
        group_id = group_by_name.get(group_name)

        print group_id

        if group_id:
            incallda = GroupDestination(group_id)
            incall = Incall(number=i, context=context, destination=incallda)
            print 'Adding Incall %s going to Group : %s (id = %s)' % (i, basename % i, group_id)
            xivo_server.incalls.add(incall)


build_incall_to_group(XIVO_ADDR, DID_START, DID_STOP + 1, GROUPPATTERN, CONTEXT)
