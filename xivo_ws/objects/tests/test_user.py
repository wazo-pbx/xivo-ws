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

import unittest
from xivo_ws.objects.user import User, UserLine


class TestUser(unittest.TestCase):
    def test_raise_error_if_firstname_is_none(self):
        user = User()

        self.assertRaises(ValueError, user.to_obj_dict)

    def test_doesnt_raise_if_firstname_is_provided(self):
        user = User()
        user.firstname = u'Alice'

        user.to_obj_dict()

    def test_id_is_none_after_init(self):
        user = User()

        self.assertEqual(None, user.id)

    def test_unspecified_fields_are_not_mapped_to_obj_dict(self):
        user = User()
        user.firstname = u'John'

        obj_dict = user.to_obj_dict()

        self.assertTrue(u'lastname' not in obj_dict[u'userfeatures'])

    def test_fields_are_mapped_correctly(self):
        user = User()
        user.firstname = u'Jack'
        user.lastname = u'Johnson'
        user.enable_client = True
        user.client_username = u'jack'
        user.client_password = u'jack'
        user.client_profile = u'agent'
        user.line = UserLine()
        user.line.number = 1000
        user.line.context = u'default'

        obj_dict = user.to_obj_dict()
        self.assertEqual(user.firstname, obj_dict[u'userfeatures'][u'firstname'])
        self.assertEqual(user.lastname, obj_dict[u'userfeatures'][u'lastname'])
        self.assertEqual(user.enable_client, obj_dict[u'userfeatures'][u'enableclient'])
        self.assertEqual(user.client_username, obj_dict[u'userfeatures'][u'loginclient'])
        self.assertEqual(user.client_password, obj_dict[u'userfeatures'][u'passwdclient'])
        self.assertEqual(user.client_profile, obj_dict[u'userfeatures'][u'profileclient'])
        self.assertEqual(user.line.number, int(obj_dict[u'linefeatures'][u'number'][0]))
