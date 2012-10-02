from __future__ import unicode_literals

import unittest
import sys

from xivo_ws.objects.sccp_general_settings import SCCPGeneralSettings

class TestSCCPGeneralSettings(unittest.TestCase):

    def test_to_obj_dict_directmedia(self):

        expected_obj_dict = {
            'directmedia' : 1,
            'dialtimeout' : 5,
            'language'    : 'en_US'
        }

        settings = SCCPGeneralSettings(
            directmedia = True,
            dialtimeout = 5,
            language = 'en_US'
        )

        obj_dict = settings.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict_directmedia(self):

        obj_dict = {
            'directmedia' : 0,
            'dialtimeout' : 6,
            'language'    : 'fr_FR'
        }

        obj = SCCPGeneralSettings.from_obj_dict(obj_dict)

        self.assertEqual(False, obj.directmedia)
        self.assertEqual(6, obj.dialtimeout)
        self.assertEqual('fr_FR', obj.language)

