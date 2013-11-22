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

import logging
import urllib2
from base64 import b64encode
from xivo_ws.exception import WebServiceRequestError, WebServiceError
from xivo_ws.version import version

logger = logging.getLogger(__name__)


class HTTPClient(object):

    _USER_AGENT = u'xivo-ws/%s' % version

    def __init__(self, host, username=None, password=None,
                 force_http=False, xdebug_eclipse=False):
        self._scheme_and_host = self._compute_scheme_and_host(host, force_http)
        self._opener = self._new_opener(username, password)
        self._xdebug_eclipse = xdebug_eclipse

    def _compute_scheme_and_host(self, host, force_http):
        scheme = self._compute_scheme(host, force_http)
        return u'%s://%s' % (scheme, host)

    def _compute_scheme(self, host, force_http):
        if force_http or host in [u'localhost', u'127.0.0.1']:
            return u'http'
        else:
            return u'https'

    def _new_opener(self, username, password):
        handlers = []
        if username is not None and password is not None:
            pwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
            pwd_manager.add_password(None, self._scheme_and_host, username, password)
            handlers.append(_PreemptiveHTTPBasicAuthHandler(pwd_manager))
        return urllib2.build_opener(*handlers)

    def get(self, path_and_query, headers=None):
        return self._do_request(path_and_query, None, headers)

    def _do_request(self, path_and_query, data, headers):
        request = self._new_request(path_and_query, data, headers)
        logger.debug(u'HTTP %s %s %s', request.get_method(), request.get_full_url(), data)
        try:
            fobj = self._opener.open(request)
        except urllib2.HTTPError as e:
            logger.debug(u'HTTP %s %s', e.code, e.msg)
            raise WebServiceRequestError(e.code, e.msg, request.get_full_url())
        except urllib2.URLError as e:
            logger.debug(u'Error while requesting: %s', e)
            raise WebServiceError(e)
        else:
            try:
                logger.debug(u'HTTP %s %s', fobj.code, fobj.msg)
                return fobj.read()
            finally:
                fobj.close()

    def _new_request(self, path_and_query, data, headers):
        if headers is None:
            headers = {}
        url = self._compute_url(path_and_query)
        request = urllib2.Request(url, data, headers)
        request.add_header(u'User-Agent', self._USER_AGENT)
        if self._xdebug_eclipse:
            request.add_header(u'Cookie', u'XDEBUG_SESSION=ECLIPSE_DBGP')
        return request

    def _compute_url(self, path_and_query):
        return u'%s%s' % (self._scheme_and_host, path_and_query)

    def post(self, path_and_query, data, headers=None):
        return self._do_request(path_and_query, data, headers)


class _PreemptiveHTTPBasicAuthHandler(urllib2.BaseHandler):

    def __init__(self, password_mgr):
        self._password_mgr = password_mgr

    def http_request(self, req):
        uri = req.get_full_url()
        user, pwd = self._password_mgr.find_user_password(None, uri)
        if pwd is not None:
            raw = '%s:%s' % (user, pwd)
            auth = 'Basic %s' % b64encode(raw).rstrip()
            req.add_unredirected_header('Authorization', auth)
        return req

    https_request = http_request
