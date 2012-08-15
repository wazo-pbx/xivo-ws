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

from itertools import chain
from xivo_ws.objects.common import Attribute, AbstractObject, Actions, AbstractWebService
from xivo_ws.registry import register_ws_class


class User(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('firstname', required=True),
        Attribute('lastname'),
        Attribute('language'),
        Attribute('enable_client'),
        Attribute('client_username'),
        Attribute('client_password'),
        Attribute('client_profile'),
        Attribute('entity_id', required=True, default=1),
        Attribute('enable_hint', default=True),
        Attribute('line'),
        Attribute('voicemail'),
    ]

    def _to_obj_dict(self, obj_dict):
        if self.voicemail is not None and self.language is None:
            raise ValueError('language must be set when adding voicemail')
        self._add_userfeatures(obj_dict)
        self._add_line(obj_dict)
        self._add_voicemail(obj_dict)
        self._add_dialaction(obj_dict)

    def _add_userfeatures(self, obj_dict):
        userfeatures = {
            'musiconhold': 'default',
            'entityid': self.entity_id,
            # TODO check why default values for enablexfer (and
            #      other that we don't see) aren't working
            'enablexfer': True,
            'firstname': self.firstname,
        }
        if self.lastname is not None:
            userfeatures['lastname'] = self.lastname
        if self.language is not None:
            userfeatures['language'] = self.language
        if self.enable_client is not None:
            userfeatures['enableclient'] = self.enable_client
        if self.client_username is not None:
            userfeatures['loginclient'] = self.client_username
        if self.client_password is not None:
            userfeatures['passwdclient'] = self.client_password
        if self.client_profile is not None:
            userfeatures['profileclient'] = self.client_profile
        if self.enable_hint is not None:
            userfeatures['enablehint'] = self.enable_hint
        obj_dict['userfeatures'] = userfeatures

    def _add_line(self, obj_dict):
        if self.line:
            self.line._add_line(obj_dict)

    def _add_voicemail(self, obj_dict):
        if self.voicemail:
            self.voicemail._add_voicemail(obj_dict)

    def _add_dialaction(self, obj_dict):
        dialaction = {
            'noanswer': {
                'actiontype': 'none',
            },
            'busy': {
                'actiontype': 'none',
            },
            'congestion': {
                'actiontype': 'none',
            },
            'chanunavail': {
                'actiontype': 'none',
            },
        }
        obj_dict['dialaction'] = dialaction

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        obj = cls()
        obj.id = obj_dict['id']
        obj.entity_id = obj_dict['entityid']
        obj.firstname = obj_dict['firstname']
        obj.lastname = obj_dict['lastname']
        if obj_dict['voicemailid']:
            obj.voicemail = UserVoicemail()
            obj.voicemail.id = obj_dict['voicemailid']
        return obj


class UserLine(AbstractObject):
    _ATTRIBUTES = [
        Attribute('protocol', default='sip', required=True),
        Attribute('context', required=True),
        Attribute('number'),
        Attribute('device_id'),
    ]

    def _add_line(self, obj_dict):
        self._check_required_attributes()
        linefeatures = {
            'protocol': [self.protocol],
            'context': [self.context],
            'number': [self.number],
        }
        if self.device_id is not None:
            linefeatures['device'] = [self.device_id]
        obj_dict['linefeatures'] = linefeatures


class UserVoicemail(AbstractObject):
    _ATTRIBUTES = [
        Attribute('id'),
        Attribute('name', required=True),
        Attribute('number', required=True),
    ]

    def _add_voicemail(self, obj_dict):
        self._check_required_attributes()
        voicemail_dict = {
            'fullname': self.name,
            'mailbox': self.number
        }
        obj_dict['voicemail'] = voicemail_dict
        obj_dict['voicemail-option'] = 'add'


class _ImportContentGenerator(object):
    _COLUMNS = [
        # (attr_name, column_name, map function)
        ('entity_id', 'entityid', None),
        ('firstname', 'firstname', None),
        ('lastname', 'lastname', None),
        ('enable_client', 'enableclient', int),
        ('client_username', 'username', None),
        ('client_password', 'password', None),
        ('client_profile', 'profileclient', None),
        ('enable_hint', 'enablehint', int),
    ]
    _LINE_COLUMNS = [
        ('number', 'phonenumber'),
        ('context', 'context'),
        ('protocol', 'protocol'),
    ]

    def __init__(self):
        self._rows = []
        self._add_header()

    def _add_header(self):
        header = '|'.join(column[1] for column in chain(self._COLUMNS, self._LINE_COLUMNS))
        self._rows.append(header)

    def add_users(self, users):
        for user in users:
            self._rows.append(self._user_to_row(user))

    def _user_to_row(self, user):
        elements = []
        for attribute_name, _, map_function in self._COLUMNS:
            attribute = getattr(user, attribute_name)
            if attribute is None:
                elements.append('')
            else:
                if map_function is not None:
                    attribute = map_function(attribute)
                elements.append(unicode(attribute))
        line = user.line
        for attribute_name, _ in self._LINE_COLUMNS:
            if line is None:
                elements.append('')
            else:
                attribute = getattr(line, attribute_name)
                if attribute is None:
                    elements.append('')
                else:
                    elements.append(unicode(attribute))
        return '|'.join(elements)

    def get_content(self):
        unicode_content = '\n'.join(chain(self._rows, ['']))
        return unicode_content.encode('UTF-8')


class UserWebService(AbstractWebService):
    _PATH = '/service/ipbx/json.php/restricted/pbx_settings/users/'
    _OBJECT_CLASS = User

    _ACTIONS = [
        Actions.ADD,
        Actions.DELETE,
        Actions.DELETE_ALL,
        Actions.LIST,
        Actions.SEARCH,
    ]

    def import_(self, users):
        content = self._generate_import_content(users)
        self._ws_client.custom_request(self._PATH, 'act=import', content)

    def _generate_import_content(self, users):
        generator = _ImportContentGenerator()
        generator.add_users(users)
        return generator.get_content()


register_ws_class(UserWebService, 'users')
# deprecated name
register_ws_class(UserWebService, 'user')
