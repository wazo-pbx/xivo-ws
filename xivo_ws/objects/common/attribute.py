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


class Attribute(object):
    _UNSPECIFIED = object()

    def __init__(self, name, default=_UNSPECIFIED, default_factory=_UNSPECIFIED,
                 required=False):
        self.name = name
        self.required = required
        self._default_factory = self._build_default_factory(default, default_factory)

    def _build_default_factory(self, default, default_factory):
        if default is self._UNSPECIFIED:
            if default_factory is self._UNSPECIFIED:
                return _StaticDefaultFactory(None)
            else:
                return default_factory
        else:
            if default_factory is self._UNSPECIFIED:
                return _StaticDefaultFactory(default)
            else:
                raise Exception('must not specify both default and default_factory')

    def get_default(self):
        return self._default_factory()


class _StaticDefaultFactory(object):
    __slots__ = ['_value']

    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value
