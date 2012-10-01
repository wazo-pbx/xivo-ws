from __future__ import unicode_literals

import unittest
import sys

from xivo_ws.objects.sccp_general_settings import SCCPGeneralSettings

class TestSCCPGeneralSettings(unittest.TestCase):

    def test_to_obj_dict_directmedia(self):

        expected_obj_dict = {
            'directmedia' : 1
        }

        obj_dict = SCCPGeneralSettings(directmedia = True).to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict_directmedia(self):

        obj_dict = {
            'directmedia' : 1
        }

        obj = SCCPGeneralSettings.from_obj_dict(obj_dict)

        self.assertEqual(True, obj.directmedia)

