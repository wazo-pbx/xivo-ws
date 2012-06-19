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
from xivo_ws.objects.common.attribute import Attribute


class TestAttribute(unittest.TestCase):
    def test_attribute_with_name_only(self):
        attr = Attribute('foo')

        self.assertEqual('foo', attr.name)
        self.assertEqual(None, attr.get_default())
        self.assertEqual(False, attr.required)

    def test_attribute_with_default(self):
        attr = Attribute('foo', default=u'foobar')

        self.assertEqual(u'foobar', attr.get_default())

    def test_attribute_with_default_factory(self):
        attr = Attribute('foo', default_factory=list)

        self.assertEqual([], attr.get_default())

    def test_attribute_with_required(self):
        attr = Attribute('foo', required=True)

        self.assertTrue(attr.required)
