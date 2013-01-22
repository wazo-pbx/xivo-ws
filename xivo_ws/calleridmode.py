# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 Avencall
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


class CallerIDMode(object):

    def __init__(self, mode, value):
        self.mode = mode
        self.value = value

    def to_obj_dict(self):
        obj_dict = {
            'mode': self.mode,
            'callerdisplay': self.value,
        }
        return obj_dict


def PrependCallerIDMode(value):
    return CallerIDMode('prepend', value)


def OverwriteCallerIDMode(value):
    return CallerIDMode('overwrite', value)


def AppendCallerIDMode(value):
    return CallerIDMode('append', value)
