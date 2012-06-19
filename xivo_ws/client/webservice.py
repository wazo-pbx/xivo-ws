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
import logging
from urllib import quote_plus

logger = logging.getLogger(__name__)


class WebServiceClient(object):
    _POST_HEADERS = {u'Content-Type': u'application/json'}

    def __init__(self, http_client):
        self._http_client = http_client

    def add(self, path, obj_dict):
        query = u'act=add'
        self._do_post_request(path, query, obj_dict)

    def _do_post_request(self, path, query, obj_dict):
        path_and_query = self._compute_path_and_query(path, query)
        request_content = json.dumps(obj_dict)
        response_content = self._http_client.post(path_and_query, request_content,
                                                     self._POST_HEADERS)
        return response_content

    def _do_get_request(self, path, query):
        path_and_query = self._compute_path_and_query(path, query)
        response_content = self._http_client.get(path_and_query)
        return response_content

    def _compute_path_and_query(self, path, query):
        return u'%s?%s' % (path, query)

    def delete(self, path, obj_id):
        query = u'act=delete&id=%s' % quote_plus(unicode(obj_id))
        self._do_get_request(path, query)

    def edit(self, path, obj_id, obj_dict):
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
        query = u'act=search&search=%s' % quote_plus(unicode(search_pattern))
        return self._do_list_or_search_request(path, query)

    def view(self, path, obj_id):
        query = u'act=view&id=%s' % quote_plus(unicode(obj_id))
        response_content = self._do_get_request(path, query)
        obj_dict = json.loads(response_content)
        return obj_dict


class DebugWebServiceClientDecorator(object):
    def __init__(self, ws_client):
        self._ws_client = ws_client

    def __getattr__(self, name):
        return getattr(self._ws_client, name)

    def add(self, path, obj_dict):
        logger.debug('HTTP request (agent) obj_dict:\n%s', self._format_obj_dict(obj_dict))
        self._ws_client.add(path, obj_dict)

    def edit(self, path, obj_id, obj_dict):
        logger.debug('HTTP request (edit) obj_dict:\n%s', self._format_obj_dict(obj_dict))
        self._ws_client.edit(path, obj_id, obj_dict)

    def list(self, path):
        obj_dict = self._ws_client.list(path)
        logger.debug('HTTP response (list) obj_dict:\n%s', self._format_obj_dict(obj_dict))
        return obj_dict

    def search(self, path, search_pattern):
        obj_dict = self._ws_client.search(path, search_pattern)
        logger.debug('HTTP response (search) obj_dict:\n%s', self._format_obj_dict(obj_dict))
        return obj_dict

    def view(self, path, obj_id):
        obj_dict = self._ws_client.view(path, obj_id)
        logger.debug('HTTP response (view) obj_dict:\n%s', self._format_obj_dict(obj_dict))
        return obj_dict

    def _format_obj_dict(self, obj_dict):
        return json.dumps(obj_dict, indent=4, sort_keys=True)
