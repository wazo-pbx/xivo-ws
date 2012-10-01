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


def convert_directmedia(value):
    if value.isdigit():
        return bool(int(value))
    elif value in ["yes", "no"]:
        return value == "yes"


class SCCPGeneralSettings(AbstractObject):
    _ATTRIBUTES = [
        Attribute('directmedia', required=True),
        Attribute('dialtimeout', required=True),
        Attribute('language', required=True)
    ]

    def _to_obj_dict(self, obj_dict):
        obj_dict['directmedia'] = int(self.directmedia)
        obj_dict['dialtimeout'] = int(self.dialtimeout)
        obj_dict['language'] = unicode(self.language)

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj.directmedia = convert_directmedia(obj_dict['directmedia'])
        obj.dialtimeout = int(obj_dict['dialtimeout'])
        obj.language = unicode(obj_dict['language'])
        return obj


class SCCPGeneralSettingsWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/general_settings/sccp/'
    _OBJECT_CLASS = SCCPGeneralSettings

    _ACTIONS = [
        Actions.EDIT,
        Actions.VIEW,
    ]

register_ws_class(SCCPGeneralSettingsWebService, 'sccp_general_settings')
