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
from xivo_ws.objects.line import Line


class TestLine(unittest.TestCase):
    def test_from_obj_dict_sip(self):
        obj_dict = {
            "linefeatures": {
                "commented": False,
                "config": "",
                "configregistrar": "default",
                "context": "custom_context",
                "description": "",
                "device": "1",
                "encryption": False,
                "id": 4,
                "internal": False,
                "ipfrom": "192.168.11.106",
                "name": "iibybz",
                "num": 1,
                "number": "1001",
                "protocol": "sip",
                "protocolid": 4,
                "provisioningid": 111011
            },
            "protocol": {
                "accountcode": None,
                "allow": None,
                "allowoverlap": None,
                "allowsubscribe": None,
                "allowtransfer": None,
                "amaflags": "default",
                "autoframing": None,
                "buggymwi": None,
                "busylevel": None,
                "call-limit": "10",
                "callbackextension": None,
                "callcounter": None,
                "callerid": "\"User 1\" <1001>",
                "callgroup": "1",
                "callingpres": None,
                "category": "user",
                "cid_number": None,
                "commented": False,
                "contactdeny": None,
                "contactpermit": None,
                "context": "custom_context",
                "defaultip": None,
                "deny": None,
                "directmedia": None,
                "disallow": None,
                "disallowed_methods": None,
                "dtmfmode": None,
                "encryption": None,
                "fromdomain": None,
                "fromuser": None,
                "fullcontact": None,
                "fullname": None,
                "g726nonstandard": None,
                "host": "dynamic",
                "id": 4,
                "identity": "SIP/iibybz",
                "ignoresdpversion": None,
                "initialized": False,
                "insecure": None,
                "ipaddr": "",
                "language": None,
                "lastms": "",
                "maxcallbitrate": None,
                "maxforwards": None,
                "md5secret": "",
                "mohinterpret": None,
                "name": "iibybz",
                "nat": None,
                "outboundproxy": None,
                "parkinglot": None,
                "permit": None,
                "pickupgroup": "1",
                "port": None,
                "progressinband": None,
                "promiscredir": None,
                "protocol": "sip",
                "qualify": None,
                "qualifyfreq": None,
                "regexten": None,
                "registertrying": None,
                "regseconds": "0",
                "regserver": None,
                "remotesecret": None,
                "rfc2833compensate": None,
                "rtpholdtimeout": None,
                "rtpkeepalive": None,
                "rtptimeout": None,
                "secret": "KL5LKY",
                "sendrpid": None,
                "session-expires": None,
                "session-minse": None,
                "session-refresher": None,
                "session-timers": None,
                "setvar": "XIVO_USERID=4",
                "snom_aoc_enabled": None,
                "subscribecontext": None,
                "subscribemwi": "0",
                "t38pt_udptl": None,
                "t38pt_usertpsource": None,
                "textsupport": None,
                "timerb": None,
                "timert1": None,
                "transport": None,
                "trustrpid": None,
                "type": "friend",
                "unsolicited_mailbox": None,
                "use_q850_reason": None,
                "useclientcode": None,
                "usereqphone": None,
                "username": None,
                "videosupport": None,
                "vmexten": None
            },
            "usermacro": {
                "app": "GoSub",
                "appdata": "user,s,1(4,4,,)",
                "commented": False,
                "context": "default",
                "exten": "1001",
                "id": "51",
                "name": "",
                "priority": "1"
            }
        }

        line = Line.from_obj_dict(obj_dict)

        self.assertEqual(4, line.id)
        self.assertEqual(Line.PROTOCOL_SIP, line.protocol)
        self.assertEqual('iibybz', line.name)
        self.assertEqual('1001', line.number)
        self.assertEqual('custom_context', line.context)

    def test_from_obj_dict_custom(self):
        obj_dict = {
            "linefeatures": {
                "commented": False,
                "config": "",
                "configregistrar": "default",
                "context": "custom_context",
                "description": "",
                "device": "",
                "encryption": False,
                "id": 270,
                "internal": False,
                "ipfrom": "10.32.0.1",
                "name": "dahdi/g0",
                "num": 0,
                "number": "",
                "protocol": "custom",
                "protocolid": 66,
                "provisioningid": 0
            },
            "protocol": {
                "category": "user",
                "commented": False,
                "context": "custom_context",
                "id": 66,
                "identity": "CUSTOM/",
                "initialized": True,
                "interface": "dahdi/g0",
                "intfsuffix": "",
                "name": None,
                "protocol": "custom"
            },
            "usermacro": False
        }

        line = Line.from_obj_dict(obj_dict)

        self.assertEqual(270, line.id)
        self.assertEqual(Line.PROTOCOL_CUSTOM, line.protocol)
        self.assertEqual('', line.number)
        self.assertEqual('custom_context', line.context)
        self.assertEqual(None, line.user_id)

    def test_from_obj_dict_sccp(self):
        obj_dict = {
            "linefeatures": {
                "commented": False,
                "config": "",
                "configregistrar": "default",
                "context": "custom_context",
                "description": "",
                "device": "11",
                "encryption": False,
                "id": 150,
                "internal": False,
                "ipfrom": "10.32.0.1",
                "name": "101",
                "num": 1,
                "number": "101",
                "protocol": "sccp",
                "protocolid": 3,
                "provisioningid": 0
            },
            "protocol": {
                "cid_name": "User 1",
                "cid_num": "101",
                "commented": "0",
                "context": "custom_context",
                "id": 3,
                "name": "101",
                "protocol": "sccp"
            },
            "usermacro": {
                "app": "GoSub",
                "appdata": "user,s,1(37,150,,)",
                "commented": False,
                "context": "default",
                "exten": "101",
                "id": "113",
                "name": "",
                "priority": "1"
            }
        }

        line = Line.from_obj_dict(obj_dict)

        self.assertEqual(150, line.id)
        self.assertEqual(Line.PROTOCOL_SCCP, line.protocol)
        self.assertEqual('101', line.name)
        self.assertEqual('101', line.number)
        self.assertEqual('custom_context', line.context)

    def test_from_list_obj_dict_sip(self):
        obj_dict = {
            "accountcode": None,
            "allow": None,
            "allowoverlap": None,
            "allowsubscribe": None,
            "allowtransfer": None,
            "amaflags": "default",
            "autoframing": None,
            "buggymwi": None,
            "busylevel": None,
            "call-limit": "10",
            "callbackextension": None,
            "callcounter": None,
            "callerid": "\"User 1\" <1001>",
            "callgroup": "1",
            "callingpres": None,
            "category": "user",
            "cid_number": None,
            "commented": False,
            "config": "",
            "configregistrar": "default",
            "contactdeny": None,
            "contactpermit": None,
            "context": "custom_context",
            "defaultip": None,
            "deny": None,
            "description": "",
            "device": "1",
            "directmedia": None,
            "disallow": None,
            "disallowed_methods": None,
            "dtmfmode": None,
            "encryption": False,
            "fromdomain": None,
            "fromuser": None,
            "fullname": None,
            "g726nonstandard": None,
            "host": "dynamic",
            "id": 4,
            "identity": "SIP/iibybz",
            "ignoresdpversion": None,
            "initialized": False,
            "insecure": None,
            "internal": False,
            "ipaddr": "",
            "ipfrom": "192.168.11.106",
            "language": None,
            "lastms": "",
            "maxcallbitrate": None,
            "maxforwards": None,
            "md5secret": "",
            "mohinterpret": None,
            "name": "iibybz",
            "nat": None,
            "num": 1,
            "number": "1001",
            "outboundproxy": None,
            "parkinglot": None,
            "permit": None,
            "pickupgroup": "1",
            "port": None,
            "progressinband": None,
            "promiscredir": None,
            "protocol": "sip",
            "protocolid": 4,
            "provisioningid": 111011,
            "qualify": None,
            "qualifyfreq": None,
            "regexten": None,
            "registertrying": None,
            "regseconds": "0",
            "regserver": None,
            "remotesecret": None,
            "rfc2833compensate": None,
            "rtpholdtimeout": None,
            "rtpkeepalive": None,
            "rtptimeout": None,
            "secret": "KL5LKY",
            "sendrpid": None,
            "session-expires": None,
            "session-minse": None,
            "session-refresher": None,
            "session-timers": None,
            "setvar": "XIVO_USERID=4",
            "snom_aoc_enabled": None,
            "subscribecontext": None,
            "subscribemwi": "0",
            "t38pt_udptl": None,
            "t38pt_usertpsource": None,
            "textsupport": None,
            "timerb": None,
            "timert1": None,
            "transport": None,
            "trustrpid": None,
            "type": "friend",
            "unsolicited_mailbox": None,
            "use_q850_reason": None,
            "useclientcode": None,
            "usereqphone": None,
            "useridentity": "User 1",
            "username": None,
            "videosupport": None,
            "vmexten": None
        }

        line = Line.from_list_obj_dict(obj_dict)

        self.assertEqual(4, line.id)
        self.assertEqual(Line.PROTOCOL_SIP, line.protocol)
        self.assertEqual('iibybz', line.name)
        self.assertEqual('1001', line.number)
        self.assertEqual('custom_context', line.context)

    def test_from_list_obj_dict_custom(self):
        obj_dict = {
            "commented": False,
            "config": "",
            "configregistrar": "default",
            "context": "custom_context",
            "description": "",
            "device": "",
            "encryption": False,
            "id": 331,
            "identity": "dahdi/g22",
            "initialized": True,
            "interface": "dahdi/g22",
            "internal": False,
            "ipfrom": "10.32.0.1",
            "name": "dahdi/g22",
            "num": 0,
            "number": "",
            "protocol": "custom",
            "protocolid": 92,
            "provisioningid": 0,
            "useridentity": "-"
        }

        line = Line.from_list_obj_dict(obj_dict)

        self.assertEqual(331, line.id)
        self.assertEqual(Line.PROTOCOL_CUSTOM, line.protocol)
        self.assertEqual('dahdi/g22', line.name)
        self.assertEqual('', line.number)
        self.assertEqual('custom_context', line.context)
        self.assertEqual(None, line.user_id)

    def test_from_list_obj_dict_sccp(self):
        obj_dict = {
            "cid_name": "User 1",
            "cid_num": "101",
            "commented": False,
            "config": "",
            "configregistrar": "default",
            "context": "custom_context",
            "description": "",
            "device": "11",
            "encryption": False,
            "id": 150,
            "identity": "SCCP/101",
            "initialized": True,
            "internal": False,
            "ipfrom": "10.32.0.1",
            "name": "101",
            "num": 1,
            "number": "101",
            "protocol": "sccp",
            "protocolid": 3,
            "provisioningid": 0,
            "useridentity": "User 1"
        }

        line = Line.from_list_obj_dict(obj_dict)

        self.assertEqual(150, line.id)
        self.assertEqual(Line.PROTOCOL_SCCP, line.protocol)
        self.assertEqual('101', line.name)
        self.assertEqual('101', line.number)
        self.assertEqual('custom_context', line.context)
