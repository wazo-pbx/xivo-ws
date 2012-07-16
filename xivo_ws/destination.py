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


class GroupDestination(object):
    def __init__(self, group_id):
        self.group_id = group_id

    def to_obj_dict(self):
        obj_dict = {
            'actiontype': 'group',
            'actionarg1': self.group_id,
            'actionarg2': '',
        }
        return obj_dict


class QueueDestination(object):
    def __init__(self, queue_id):
        self.queue_id = queue_id

    def to_obj_dict(self):
        obj_dict = {
            'actiontype': 'queue',
            'actionarg1': self.queue_id,
            'actionarg2': '',
        }
        return obj_dict
