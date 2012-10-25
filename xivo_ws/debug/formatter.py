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

import json
import pprint
import re


class JSONFormatter(object):
    def format(self, obj_dict):
        return json.dumps(obj_dict, indent=4, sort_keys=True)


class PprintFormatter(object):
    def format(self, obj_dict):
        return pprint.pformat(obj_dict)


class PythonFormatter(object):
    _REGEX_FALSE = re.compile(ur'\bfalse\b')
    _REGEX_TRUE = re.compile(ur'\btrue\b')
    _REGEX_NULL = re.compile(ur'\bnull\b')

    def __init__(self):
        self._json_formatter = JSONFormatter()

    def format(self, obj_dict):
        fmted_string = self._json_formatter.format(obj_dict)
        fmted_string = self._REGEX_FALSE.sub(u'False', fmted_string)
        fmted_string = self._REGEX_TRUE.sub(u'True', fmted_string)
        fmted_string = self._REGEX_NULL.sub(u'None', fmted_string)
        return fmted_string
