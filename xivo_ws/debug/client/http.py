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

import logging
from time import time

logger = logging.getLogger(__name__)


class DebugHTTPClientDecorator(object):

    def __init__(self, http_client):
        self._http_client = http_client

    def get(self, path_and_query, headers=None):
        content = self._http_client.get(path_and_query, headers)
        self._log_response_body(content)
        return content

    def post(self, path_and_query, data, headers=None):
        self._log_request_body(data)
        content = self._http_client.post(path_and_query, data, headers)
        self._log_response_body(content)
        return content

    def _log_request_body(self, content):
        if content:
            logger.debug('HTTP request body:\n%s', content)
        else:
            logger.debug('HTTP request body is empty')

    def _log_response_body(self, content):
        if content:
            logger.debug('HTTP response body:\n%s', content)
        else:
            logger.debug('HTTP response body is empty')


class TimingHTTPClientDecorator(object):

    def __init__(self, http_client):
        self._http_client = http_client

    def get(self, *args, **kwargs):
        return self._time_http_request(self._http_client.get, args, kwargs)

    def _time_http_request(self, fun, args, kwargs):
        start_time = time()
        try:
            return fun(*args, **kwargs)
        finally:
            total_time = time() - start_time
            logger.debug('HTTP request/response took %.3f s' % total_time)

    def post(self, *args, **kwargs):
        return self._time_http_request(self._http_client.post, args, kwargs)
