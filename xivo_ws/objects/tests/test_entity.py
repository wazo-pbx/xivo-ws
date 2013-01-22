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

import unittest
from xivo_ws.objects.entity import Entity


class TestEntity(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'name': 'entity',
            'displayname': 'Entity',
        }
        entity = Entity(name='entity',
                        display_name='Entity')

        obj_dict = entity.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            "address1": "",
            "address2": "",
            "city": "",
            "country": "",
            "dcreate": "1330285876",
            "description": "",
            "disable": False,
            "displayname": "Entity",
            "email": "",
            "faxnumber": "",
            "id": "1",
            "identity": "Entity (entity)",
            "name": "entity",
            "phonenumber": "",
            "state": "",
            "url": "",
            "zipcode": ""
        }

        entity = Entity.from_obj_dict(obj_dict)

        self.assertEqual(1, entity.id)
        self.assertEqual('entity', entity.name)
        self.assertEqual('Entity', entity.display_name)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "address1": "",
            "address2": "",
            "city": "",
            "country": "",
            "dcreate": "1330285876",
            "description": "",
            "disable": False,
            "displayname": "Entity",
            "email": "",
            "faxnumber": "",
            "id": "1",
            "identity": "Entity (entity)",
            "name": "entity",
            "phonenumber": "",
            "state": "",
            "url": "",
            "zipcode": ""
        }

        entity = Entity.from_obj_dict(obj_dict)

        self.assertEqual(1, entity.id)
        self.assertEqual('entity', entity.name)
        self.assertEqual('Entity', entity.display_name)
