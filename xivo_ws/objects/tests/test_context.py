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

import unittest
from xivo_ws.objects.context import Context, ContextRange


class TestContext(unittest.TestCase):
    def test_new_context_with_no_attribute(self):
        context = Context()

        self.assertEqual(None, context.id)
        self.assertEqual(None, context.name)
        self.assertEqual(None, context.display_name)
        self.assertEqual(None, context.entity)
        self.assertEqual(Context.TYPE_INCALL, context.type)
        self.assertEqual([], context.context_include)
        self.assertEqual([], context.users)
        self.assertEqual([], context.groups)
        self.assertEqual([], context.queues)
        self.assertEqual([], context.conf_rooms)
        self.assertEqual([], context.incalls)

    def test_new_context_with_all_attributes(self):
        context = Context(id='default',
                          name='default',
                          display_name='Default',
                          entity='entity',
                          type=Context.TYPE_INTERNAL,
                          context_include=['to-extern'],
                          users=[ContextRange(100, 199)],
                          groups=[ContextRange(200, 209)],
                          queues=[ContextRange(210, 219)],
                          conf_rooms=[ContextRange(220, 229)],
                          incalls=[ContextRange(230, 239, did_length=3)])

        self.assertEqual('default', context.id)
        self.assertEqual('default', context.name)
        self.assertEqual('Default', context.display_name)
        self.assertEqual('entity', context.entity)
        self.assertEqual(Context.TYPE_INTERNAL, context.type)
        self.assertEqual(['to-extern'], context.context_include)
        self.assertEqual([ContextRange(100, 199)], context.users)
        self.assertEqual([ContextRange(200, 209)], context.groups)
        self.assertEqual([ContextRange(210, 219)], context.queues)
        self.assertEqual([ContextRange(220, 229)], context.conf_rooms)
        self.assertEqual([ContextRange(230, 239, did_length=3)], context.incalls)

    def test_to_obj_dict_with_minimum(self):
        expected_obj_dict = {
            'context': {
                'name': 'default',
                'displayname': 'Default',
                'entity': 'entity',
                'contexttype': 'internal',
            },
        }
        context = Context(name='default',
                          display_name='Default',
                          entity='entity',
                          type=Context.TYPE_INTERNAL)

        obj_dict = context.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_with_full(self):
        expected_obj_dict = {
            'context': {
                'name': 'default',
                'displayname': 'Default',
                'entity': 'entity',
                'contexttype': 'internal',
            },
            'contextinclude': ['to-extern'],
            'contextnumbers': {
                'user': [{'numberbeg': 100, 'numberend': 199}],
                'group': [{'numberbeg': 200, 'numberend': 209}],
                'queue': [{'numberbeg': 210, 'numberend': 219}],
                'meetme': [{'numberbeg': 220, 'numberend': 229}],
                'incall': [{'numberbeg': 230, 'numberend': 239, 'didlength': 3}],
            },
        }
        context = Context(id='default',
                          name='default',
                          display_name='Default',
                          entity='entity',
                          type=Context.TYPE_INTERNAL,
                          context_include=['to-extern'],
                          users=[ContextRange(100, 199)],
                          groups=[ContextRange(200, 209)],
                          queues=[ContextRange(210, 219)],
                          conf_rooms=[ContextRange(220, 229)],
                          incalls=[ContextRange(230, 239, did_length=3)])

        obj_dict = context.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            "context": {
                "commented": False,
                "contexttype": "internal",
                "description": "",
                "displayname": "Default",
                "entity": "entite",
                "identity": "Default (default)",
                "name": "default"
            },
            "contextinclude": [
                {
                    "context": "default",
                    "include": "to-extern",
                    "priority": "0"
                }
            ],
            "contextmember": {
                "agent": [
                    {
                        "context": "default",
                        "type": "agent",
                        "typeval": "1",
                        "varname": "context"
                    },
                    {
                        "context": "default",
                        "type": "agent",
                        "typeval": "3",
                        "varname": "context"
                    }
                ]
            },
            "contextnumbers": {
                "group": [
                    {
                        "context": "default",
                        "didlength": "0",
                        "numberbeg": "1010",
                        "numberend": "1019",
                        "type": "group"
                    }
                ],
                "queue": [
                    {
                        "context": "default",
                        "didlength": "0",
                        "numberbeg": "1020",
                        "numberend": "1029",
                        "type": "queue"
                    }
                ],
                "user": [
                    {
                        "context": "default",
                        "didlength": "0",
                        "numberbeg": "1000",
                        "numberend": "1009",
                        "type": "user"
                    }
                ]
            },
            "contextnummember": {
                "group": [
                    {
                        "context": "default",
                        "number": "1010",
                        "type": "group",
                        "typeval": "3"
                    },
                    {
                        "context": "default",
                        "number": "1012",
                        "type": "group",
                        "typeval": "4"
                    }
                ],
                "queue": [
                    {
                        "context": "default",
                        "number": "1020",
                        "type": "queue",
                        "typeval": "1"
                    },
                    {
                        "context": "default",
                        "number": "1021",
                        "type": "queue",
                        "typeval": "2"
                    },
                    {
                        "context": "default",
                        "number": "1022",
                        "type": "queue",
                        "typeval": "35"
                    },
                    {
                        "context": "default",
                        "number": "1023",
                        "type": "queue",
                        "typeval": "44"
                    }
                ],
                "user": [
                    {
                        "context": "default",
                        "number": "1001",
                        "type": "user",
                        "typeval": "4"
                    },
                    {
                        "context": "default",
                        "number": "1002",
                        "type": "user",
                        "typeval": "5"
                    },
                    {
                        "context": "default",
                        "number": "1003",
                        "type": "user",
                        "typeval": "14"
                    }
                ]
            },
            "contexttype": {
                "commented": False,
                "deletable": False,
                "description": "",
                "id": 1,
                "name": "internal"
            },
            "deletable": False,
            "deletablemember": False,
            "deletablenumber": False
        }

        context = Context.from_obj_dict(obj_dict)

        self.assertEqual('default', context.id)
        self.assertEqual('default', context.name)
        self.assertEqual('Default', context.display_name)
        self.assertEqual('entite', context.entity)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "context": {
                "commented": False,
                "contexttype": "internal",
                "description": "",
                "displayname": "Default",
                "entity": "entite",
                "entityid": "1",
                "identity": "Default (default)",
                "name": "default"
            },
            "contextinclude": {
                "context": "default",
                "include": "to-extern",
                "priority": "0"
            },
            "contextnumbers": [
                {
                    "context": "default",
                    "didlength": "0",
                    "numberbeg": "1000",
                    "numberend": "1009",
                    "type": "user"
                },
                {
                    "context": "default",
                    "didlength": "0",
                    "numberbeg": "1010",
                    "numberend": "1019",
                    "type": "group"
                },
                {
                    "context": "default",
                    "didlength": "0",
                    "numberbeg": "1020",
                    "numberend": "1029",
                    "type": "queue"
                }
            ],
            "contexttype": {
                "commented": False,
                "deletable": False,
                "description": "",
                "id": 1,
                "name": "internal"
            },
            "deletable": False
        }

        context = Context.from_list_obj_dict(obj_dict)

        self.assertEqual('default', context.id)
        self.assertEqual('default', context.name)
        self.assertEqual('Default', context.display_name)
        self.assertEqual('entite', context.entity)
