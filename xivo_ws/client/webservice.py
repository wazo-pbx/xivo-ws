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

import json
from urllib import quote_plus

from xivo_ws.exception import WebServiceRequestError


_CHECK_WS_PATH = u'/xivo/configuration/json.php/restricted/check/'


class WebServiceClient(object):

    _JSON_POST_HEADERS = {u'Content-Type': u'application/json'}

    def __init__(self, http_client):
        self._http_client = http_client

    def add(self, path, obj_dict):
        query = u'act=add'
        object_id = self._do_post_request(path, query, obj_dict)
        return self._clean_add_return(object_id)

    def _clean_add_return(self, return_string):
        cleaned_string = self._remove_trailing_eol(return_string)
        cleaned_string = self._remove_double_quotes(cleaned_string)
        return cleaned_string

    def _remove_trailing_eol(self, string):
        return string.rstrip()

    def _remove_double_quotes(self, string):
        return string.translate(None, '"')

    def _do_post_request(self, path, query, obj_dict):
        path_and_query = self._compute_path_and_query(path, query)
        request_content = json.dumps(obj_dict)
        response_content = self._http_client.post(path_and_query, request_content,
                                                  self._JSON_POST_HEADERS)
        return response_content

    def _do_get_request(self, path, query):
        path_and_query = self._compute_path_and_query(path, query)
        response_content = self._http_client.get(path_and_query)
        return response_content

    def _compute_path_and_query(self, path, query):
        if query:
            return u'%s?%s' % (path, query)
        else:
            return path

    def delete(self, path, obj_id):
        query = u'act=delete&id=%s' % quote_plus(unicode(obj_id))
        self._do_get_request(path, query)

    def delete_all(self, path):
        query = u'act=deleteall'
        self._do_get_request(path, query)

    def edit(self, path, obj_id, obj_dict):
        if obj_id is None:
            self._edit(path, obj_dict)
        else:
            self._edit_with_id(path, obj_id, obj_dict)

    def _edit(self, path, obj_dict):
        query = u'act=edit'
        self._do_post_request(path, query, obj_dict)

    def _edit_with_id(self, path, obj_id, obj_dict):
        query = u'act=edit&id=%s' % quote_plus(unicode(obj_id))
        self._do_post_request(path, query, obj_dict)

    def list(self, path):
        query = u'act=list'
        return self._do_list_or_search_request(path, query)

    def _do_list_or_search_request(self, path, query):
        response_content = self._do_get_request(path, query)
        if response_content:
            obj_dict_list = json.loads(response_content)
        else:
            obj_dict_list = []
        return obj_dict_list

    def search(self, path, search_pattern):
        query = u'act=search&search=%s' % quote_plus(search_pattern.encode('utf8'))
        return self._do_list_or_search_request(path, query)

    def view(self, path, obj_id=None):
        query = u'act=view'
        if obj_id is not None:
            query += "&id=%s" % quote_plus(unicode(obj_id))
        response_content = self._do_get_request(path, query)
        obj_dict = json.loads(response_content)
        return obj_dict

    def custom_request(self, path, query, data=None):
        if data is None:
            return self._do_get_request(path, query)
        else:
            path_and_query = self._compute_path_and_query(path, query)
            response_content = self._http_client.post(path_and_query, data)
            return response_content

    def check_ws(self):
        try:
            self._do_get_request(_CHECK_WS_PATH, '')
        except WebServiceRequestError:
            return False
        else:
            return True
