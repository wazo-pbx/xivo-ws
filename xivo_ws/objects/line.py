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
    PROTOCOL_CUSTOM = 'custom'
    PROTOCOL_SCCP = 'sccp'

    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('protocol', required=True),
        Attribute('name', required=True),
        Attribute('number'),
        Attribute('type'),
        Attribute('username'),
        Attribute('secret', default='', required=True),
        Attribute('context', default='default', required=True),
        Attribute('language'),
        Attribute('mailbox'),
        Attribute('host'),
        Attribute('port'),
        Attribute('setvar')
    ]

    def _to_obj_dict(self, obj_dict):
        self._add_protocol(obj_dict)

    def _add_protocol(self, obj_dict):
        protocol = {
            'protocol': self.protocol,
            'name': self.name,
            'secret': self.secret,
            'context': self.context,
        }
        obj_dict['protocol'] = protocol

    def _from_linefeatures(self, linefeatures):
        self.id = linefeatures['id']
        self.protocol = linefeatures['protocol']
        self.number = linefeatures['number']

    def _from_protocol(self, protocol_name, protocol):
        if protocol_name == self.PROTOCOL_SIP:
            self._from_sip_protocol(protocol)
        elif protocol_name == self.PROTOCOL_CUSTOM:
            self._from_custom_protocol(protocol)
        elif protocol_name == self.PROTOCOL_SCCP:
            self._from_sccp_protocol(protocol)

    def _from_sip_protocol(self, protocol):
        self.name = protocol['name']
        self.type = protocol['type']
        self.username = protocol['username']
        self.secret = protocol['secret']
        self.context = protocol['context']
        self.language = protocol['language']
        self.mailbox = protocol['mailbox']
        self.host = protocol['host']
        self.port = protocol['port']
        self.setvar = protocol['setvar']

    def _from_custom_protocol(self, protocol):
        self.name = protocol['name']
        self.interface = protocol['interface']

    def _from_sccp_protocol(self, protocol):
        self.name = protocol['name']

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj._from_linefeatures(obj_dict['linefeatures'])
        obj._from_protocol(obj.protocol, obj_dict['protocol'])
        return obj

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = obj_dict['id']
        obj.protocol = obj_dict['protocol']
        obj.number = obj_dict['number']
        obj._from_protocol(obj.protocol, obj_dict)
        return obj


class LineWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/lines/'
    _OBJECT_CLASS = Line

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_number(self, number):
        number = str(number)
        lines = self.search(number)
        return [line for line in lines if line.number == number]


register_ws_class(LineWebService, 'lines')
# deprecated name
register_ws_class(LineWebService, 'line')
