#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from xivo_ws import XivoServer, Group

GROUPNAME = 'groupe_%s%s'
CONTEXT = 'default'
DID_START = 6050
DID_STOP = 6059
XIVO_ADDR = '192.168.18.120'
WSUSER = 'admin'
WSPWD = 'adminpass'


# Builds a group list from a group basename and a DID range to get :
# level0 groups (just below DID) as group_DID
# level1 groups (NoAnswer destination for level0 group) as group_DID_deb1
# level2 groups (NoAnswer destination for level1 group) as group_DID_deb2
# one level3 group named group3 (Last NoAnswer destination for [level2 or level1])
# grouplist is like :
## (group3)
## (group_DID1, group_DID1_deb1, group_DID1_deb2)
## {...}
## (group_DIDn, group_DIDn_deb1, group_DIDn_deb2)

def build_groups_list(start, end, basename):
    grouplist = ['group3']
    for i in xrange(start, end):
        groups = [basename % (i, ''),
                  basename % (i, '_deb1'),
                  basename % (i, '_deb2')]
        grouplist.append(groups)
    return grouplist


# Creates groups in XiVO Configuration from a group list of group names (best way to say it ?)
def create_groups(context, grouplist, xivoserver):
    xivo_server = XivoServer(xivoserver, WSUSER, WSPWD)
    for l in grouplist :
        for g in l:
            group = Group(name=g, number='', context=context)
            xivo_server.group.add(group)


grouplist = build_groups_list(DID_START, DID_STOP + 1, GROUPNAME)
create_groups(CONTEXT, grouplist, XIVO_ADDR)
