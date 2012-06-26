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

from xivo_ws.objects.common import Attribute, AbstractObject, Actions, AbstractWebService
from xivo_ws.registry import register_ws_class


class Line(AbstractObject):
    PROTOCOL_SIP = 'sip'

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('protocol', required=True)
    ]

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_linefeatures(obj_dict['linefeatures'])
        return obj

    def _from_linefeatures(self, linefeatures):
        self.id = linefeatures['id']
        self.protocol = linefeatures['protocol']

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_linefeatures(obj_dict)
        return obj


class LineWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/lines/'
    _WS_OBJECT = Line

    _ACTIONS = [
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]


register_ws_class(LineWebService, 'line')
