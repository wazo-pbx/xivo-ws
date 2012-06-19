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
import urllib2
from mock import MagicMock
from xivo_ws.client.http import HTTPClient
from xivo_ws.exception import WebServiceRequestError


class TestHTTPClient(unittest.TestCase):
    def _new_http_client_with_mocked_opener(self, host):
        http_client = HTTPClient(host)
        http_client._opener = MagicMock()
        return http_client

    def test_scheme_is_http_when_host_is_localhost(self):
        http_client = HTTPClient(u'localhost')

        self.assertTrue(http_client._scheme_and_host.startswith(u'http://'))

    def test_scheme_is_http_when_host_is_127_0_0_1(self):
        http_client = HTTPClient(u'127.0.0.1')

        self.assertTrue(http_client._scheme_and_host.startswith(u'http://'))

    def test_scheme_is_https_when_host_is_not_localhost(self):
        http_client = HTTPClient(u'example.org')

        self.assertTrue(http_client._scheme_and_host.startswith(u'https://'))

    def test_constructor_doesnt_crash_on_username_and_password(self):
        HTTPClient(u'example.org', u'foo', u'bar')

    def test_get_calls_opener_correctly(self):
        http_client = self._new_http_client_with_mocked_opener(u'example.org')

        http_client.get(u'/foo?act=bar')

        self.assertEqual(u'https://example.org/foo?act=bar',
                         http_client._opener.open.call_args[0][0].get_full_url())

    def test_post_calls_opener_correctly(self):
        http_client = self._new_http_client_with_mocked_opener(u'example.org')

        http_client.post(u'/foo?act=bar', 'foobar')

        self.assertEqual(u'https://example.org/foo?act=bar',
                         http_client._opener.open.call_args[0][0].get_full_url())
        self.assertEqual('foobar',
                         http_client._opener.open.call_args[0][0].get_data())

    def test_http_error_are_wrapped(self):
        http_client = self._new_http_client_with_mocked_opener(u'example.org')
        http_client._opener.open.side_effect = urllib2.HTTPError(None, 404, 'Not Found', None, None)

        try:
            http_client.get(u'/foo')
        except WebServiceRequestError as e:
            self.assertEqual(404, e.code)
            self.assertEqual('Not Found', e.msg)
        else:
            self.fail('exception not raised')
