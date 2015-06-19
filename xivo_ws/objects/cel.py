# -*- coding: utf-8 -*-

# Copyright (C) 2012-2014 Avencall
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

import json

from xivo_ws.objects.common import Attribute, AbstractObject, AbstractWebService
from xivo_ws.registry import register_ws_class


class CEL(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('eventtype'),
        Attribute('eventtime'),
        Attribute('userdeftype'),
        Attribute('cid_name'),
        Attribute('cid_num'),
        Attribute('cid_ani'),
        Attribute('cid_rdnis'),
        Attribute('cid_dnid'),
        Attribute('exten'),
        Attribute('context'),
        Attribute('channame'),
        Attribute('appname'),
        Attribute('appdata'),
        Attribute('amaflags'),
        Attribute('accountcode'),
        Attribute('peeraccount'),
        Attribute('uniqueid'),
        Attribute('linkedid'),
        Attribute('userfield'),
        Attribute('peer'),
    ]

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = obj_dict['id']
        obj.eventtype = obj_dict['eventtype']
        obj.eventtime = obj_dict['eventtime']
        obj.userdeftype = obj_dict['userdeftype']
        obj.cid_name = obj_dict['cid_name']
        obj.cid_num = obj_dict['cid_num']
        obj.cid_ani = obj_dict['cid_ani']
        obj.cid_rdnis = obj_dict['cid_rdnis']
        obj.cid_dnid = obj_dict['cid_dnid']
        obj.exten = obj_dict['exten']
        obj.context = obj_dict['context']
        obj.channame = obj_dict['channame']
        obj.appname = obj_dict['appname']
        obj.appdata = obj_dict['appdata']
        obj.amaflags = obj_dict['amaflags']
        obj.accountcode = obj_dict['accountcode']
        obj.peeraccount = obj_dict['peeraccount']
        obj.uniqueid = obj_dict['uniqueid']
        obj.linkedid = obj_dict['linkedid']
        obj.userfield = obj_dict['userfield']
        obj.peer = obj_dict['peer']
        return obj


class CELWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/call_management/cel/'
    _OBJECT_CLASS = CEL

    _ACTIONS = [
    ]

    def search_by_id(self, id_beg):
        query_string = 'act=searchid&idbeg=%s' % id_beg
        response = self._ws_client.custom_request(self._PATH, query_string)
        return [CEL.from_list_obj_dict(cel) for cel in json.loads(response)]


register_ws_class(CELWebService, 'cels')
