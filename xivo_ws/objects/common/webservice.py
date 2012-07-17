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


from types import MethodType
from xivo_ws.exception import WebServiceRequestError


class _ActionDescriptor(object):
    def __init__(self, name, fun):
        self._name = name
        self._fun = fun

    def __get__(self, instance, owner):
        if self._name in owner._ACTIONS:
            return MethodType(self._fun, instance, owner)
        else:
            raise AttributeError(self._name)


def _action(name):
    def decorator(fun):
        return _ActionDescriptor(name, fun)
    return decorator


class Actions(object):
    ADD = 'add'
    DELETE = 'delete'
    DELETE_ALL = 'delete_all'
    EDIT = 'edit'
    LIST = 'list'
    SEARCH = 'search'
    VIEW = 'view'


class AbstractWebService(object):
    # TODO add a hook system (?), to be able to follow the progression among other
    #      things
    def __init__(self, ws_client):
        self._ws_client = ws_client

    @_action(Actions.ADD)
    def add(self, obj):
        obj_dict = obj.to_obj_dict()
        return self._ws_client.add(self._PATH, obj_dict)

    @_action(Actions.ADD)
    def mass_add(self, objs):
        for obj in objs:
            self.add(obj)

    def raw_add(self, obj_dict):
        self._ws_client.add(self._PATH, obj_dict)

    @_action(Actions.DELETE)
    def delete(self, obj_id):
        self._ws_client.delete(self._PATH, obj_id)

    @_action(Actions.DELETE)
    def delete_if_exists(self, obj_id):
        try:
            self.delete(obj_id)
        except WebServiceRequestError as e:
            if e.code != 404:
                raise

    def raw_delete(self, obj_id):
        self._ws_client.delete(self._PATH, obj_id)

    @_action(Actions.DELETE_ALL)
    def delete_all(self):
        self._ws_client.delete_all(self._PATH)

    def raw_delete_all(self):
        self._ws_client.delete_all(self._PATH)

    @_action(Actions.EDIT)
    def edit(self, obj):
        obj_dict = obj.to_obj_dict()
        self._ws_client.edit(self._PATH, obj.id, obj_dict)

    def raw_edit(self, obj_id, obj_dict):
        self._ws_client.edit(self._PATH, obj_id, obj_dict)

    @_action(Actions.LIST)
    def list(self):
        obj_dict_list = self._ws_client.list(self._PATH)
        return [self._OBJECT_CLASS.from_list_obj_dict(obj_dict) for
                obj_dict in obj_dict_list]

    def raw_list(self):
        return self._ws_client.list(self._PATH)

    @_action(Actions.SEARCH)
    def search(self, search_pattern):
        obj_dict_list = self._ws_client.search(self._PATH, search_pattern)
        return [self._OBJECT_CLASS.from_list_obj_dict(obj_dict) for
                obj_dict in obj_dict_list]

    def raw_search(self, search_pattern):
        return self._ws_client.search(self._PATH, search_pattern)

    @_action(Actions.VIEW)
    def view(self, obj_id):
        obj_dict = self._ws_client.view(self._PATH, obj_id)
        return self._OBJECT_CLASS.from_obj_dict(obj_dict)

    def raw_view(self, obj_id):
        return self._ws_client.view(self._PATH, obj_id)
