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

class AbstractObject(object):
    def __init__(self, **kwargs):
        for attribute in self._ATTRIBUTES:
            value = kwargs.get(attribute.name, attribute.get_default())
            setattr(self, attribute.name, value)

    def to_obj_dict(self):
        self._check_required_attributes()

        obj_dict = {}
        self._to_obj_dict(obj_dict)
        return obj_dict

    def _check_required_attributes(self):
        for attribute in self._ATTRIBUTES:
            if attribute.required and getattr(self, attribute.name) is None:
                raise ValueError('%s must be given' % attribute.name)

    def _to_obj_dict(self, obj_dict):
        raise NotImplementedError()

    @classmethod
    def from_obj_dict(cls, obj_dict):
        raise NotImplementedError()

    @classmethod
    def from_list_obj_dict(cls, obj_dict):
        raise NotImplementedError()
