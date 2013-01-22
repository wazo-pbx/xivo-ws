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
from xivo_ws.objects.outcall import Outcall, OutcallExten


class TestOutcall(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'outcall': {
                'name': 'foobar',
                'context': 'to-extern',
            },
            'outcalltrunk': [1, 2],
            'dialpattern': {
                'id': ['0', '0', ''],
                'externprefix': ['', '', ''],
                'prefix': ['', '', ''],
                'exten': ['456', '123', ''],
                'stripnum': [0, 1, ''],
                'callerid': ['Bar', 'Foo', ''],
            },
        }
        outcall = Outcall()
        outcall.name = 'foobar'
        outcall.context = 'to-extern'
        outcall.trunks = [1, 2]
        outcall.extens = [OutcallExten(exten='123', stripnum=1, caller_id='Foo'),
                          OutcallExten(exten='456', stripnum=0, caller_id='Bar')]

        obj_dict = outcall.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'commented': False,
            'context': 'to-extern',
            'description': '',
            'hangupringtime': '0',
            'id': '2',
            'identity': 'out-testload (to-extern)',
            'internal': '0',
            'name': 'out-testload',
            'preprocess_subroutine': None,
            'useenum': '0',
        }

        outcall = Outcall.from_list_obj_dict(obj_dict)

        self.assertEqual(outcall.id, 2)
        self.assertEqual(outcall.name, 'out-testload')
