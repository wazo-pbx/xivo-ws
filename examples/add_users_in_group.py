#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, print_function

from xivo_ws import XivoServer, User, UserLine, Group

'''
Simple script to add NB_USER in group GROUP_NAME with line number starting at NUMBER_START
with name starting with FIRSTNAME_PREFIX and ending with a number.

Lines and group will be in context CONTEXT
'''

FIRSTNAME_PREFIX = 'ZZZZZ '
CONTEXT = 'default'
NB_USER = 10
NUMBER_START = 11000
GROUP_NAME = 'huge'
GROUP_NUMBER = 2034


def add():
    xivo_server = XivoServer('skaro-rc', 'admin', 'superpass')
    for i in range(NB_USER):
        print('Creating user %s...' % i)
        u = User(firstname='%s%s' % (FIRSTNAME_PREFIX, i))
        u.line = UserLine(context=CONTEXT, number=i + NUMBER_START)
        xivo_server.users.add(u)
    user_ids = [user.id for user in xivo_server.users.search(FIRSTNAME_PREFIX)]
    print('Adding users to group: %s' % user_ids)
    group = Group(name=GROUP_NAME, number=GROUP_NUMBER, context=CONTEXT, user_ids=user_ids)
    xivo_server.groups.add(group)


def delete():
    xivo_server = XivoServer('skaro-rc', 'admin', 'superpass')
    user_ids = [user.id for user in xivo_server.users.search(FIRSTNAME_PREFIX)]
    for user_id in user_ids:
        print('deleting user %s...' % user_id)
        xivo_server.users.delete(user_id)
    group_id = [group.id for group in xivo_server.groups.search(GROUP_NAME)][0]
    print('Deleting group %s' % GROUP_NAME)
    xivo_server.groups.delete(group_id)


if __name__ == '__main__':
    add()
    # delete()
