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

from xivo_ws.objects.common import Attribute, AbstractObject, Actions, AbstractWebService
from xivo_ws.registry import register_ws_class


class QueueSkillRules(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('rule', default_factory=list),
    ]

    def _to_obj_dict(self, obj_dict):
        obj_dict['name'] = self.name
        obj_dict['rule'] = self.rule

    @classmethod
    def from_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = int(obj_dict['id'])
        obj.name = obj_dict['name']
        obj.rule = obj_dict['rule']
        return obj

    from_list_obj_dict = from_obj_dict


class QueueSkillRulesWebService(AbstractWebService):
    _PATH = '/callcenter/json.php/restricted/settings/queueskillrules/'
    _OBJECT_CLASS = QueueSkillRules

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.LIST,
        Actions.SEARCH,
        Actions.VIEW,
    ]

    def search_by_name(self, name):
        name = unicode(name)
        queueskillrules = self.search(name)
        return [queueskillrule for queueskillrule in queueskillrules if queueskillrule.name == name]


register_ws_class(QueueSkillRulesWebService, 'queueskillrules')
