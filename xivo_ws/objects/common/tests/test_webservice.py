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

import unittest
from xivo_ws.objects.common import AbstractWebService, Actions
from mock import Mock


class TestNewWebService(unittest.TestCase):
    def _new_ws_object(self, actions):
        class ConcreteWebService(AbstractWebService):
            _PATH = u'/foo'
            _OBJECT_CLASS = Mock()

            _ACTIONS = actions

        return ConcreteWebService(Mock())

    def test_with_no_actions(self):
        obj = self._new_ws_object([])

        for name in ['add', 'mass_add']:
            try:
                getattr(obj, name)
            except AttributeError:
                pass
            else:
                self.fail('should have raised error on attribute %s' % name)

    def test_with_all_actions(self):
        obj = self._new_ws_object([Actions.ADD])

        obj.add
        obj.mass_add
