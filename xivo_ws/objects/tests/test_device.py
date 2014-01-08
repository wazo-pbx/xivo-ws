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

from __future__ import unicode_literals

import unittest
from xivo_ws.objects.device import Device


class TestDevice(unittest.TestCase):

    def test_from_obj_dict(self):
        obj_dict = {
            'id': 'b986267beb494f88a8882cfe2e82f68f',
            'ip': '10.34.1.28',
            'mac': '00:08:5d:23:74:29',
            'model': '6731i',
            'plugin': 'xivo-aastra-3.2.2.1136',
            'vendor': 'Aastra',
            'version': '3.2.2.1136',
            'status': 'not_configured',
            'template_id': 'defaultconfigdevice'
        }

        device = Device.from_obj_dict(obj_dict)

        self.assertEqual(obj_dict['id'], device.id)
        self.assertEqual(obj_dict['status'], device.status)
        self.assertEqual(obj_dict['template_id'], device.template_id)
        self.assertEqual(obj_dict['mac'], device.mac)
        self.assertEqual(obj_dict['ip'], device.ip)
        self.assertEqual(obj_dict['plugin'], device.plugin)
        self.assertEqual(obj_dict['model'], device.model)
        self.assertEqual(obj_dict['version'], device.version)
        self.assertEqual(obj_dict['vendor'], device.vendor)

    def test_from_list_obj_dict(self):
        obj_dict = {
            'description': '',
            'id': 'b986267beb494f88a8882cfe2e82f68f',
            'ip': '10.34.1.28',
            'mac': '00:08:5d:23:74:29',
            'model': '6731i',
            'plugin': 'xivo-aastra-3.2.2.1136',
            'proto': '',
            'sn': '',
            'vendor': 'Aastra',
            'version': '3.2.2.1136',
            'status': 'not_configured',
            'template_id': 'defaultconfigdevice'
        }

        device = Device.from_list_obj_dict(obj_dict)

        self.assertEqual(obj_dict['id'], device.id)
        self.assertEqual(obj_dict['status'], device.status)
        self.assertEqual(obj_dict['template_id'], device.template_id)
        self.assertEqual(obj_dict['mac'], device.mac)
        self.assertEqual(obj_dict['ip'], device.ip)
        self.assertEqual(obj_dict['plugin'], device.plugin)
        self.assertEqual(obj_dict['model'], device.model)
        self.assertEqual(obj_dict['version'], device.version)
        self.assertEqual(obj_dict['vendor'], device.vendor)
