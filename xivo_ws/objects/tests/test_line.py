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

from __future__ import unicode_literals

import unittest
from xivo_ws.objects.line import Line


class TestLine(unittest.TestCase):
    def test_new_line_with_no_attribute_in_constructor(self):
        line = Line()

        self.assertEqual(None, line.id)
        self.assertEqual(None, line.protocol)

    def test_from_obj_dict(self):
        obj_dict = {
            "contextnummember": {
                "context": "default",
                "number": "1001",
                "type": "user",
                "typeval": "4"
            },
            "extenumbers": {
                "context": "default",
                "exten": "1001",
                "extenbrut": "1001",
                "extenhash": "dd01903921ea24941c26a48f2cec24e0bb0e8cc7",
                "id": 53,
                "type": "user",
                "typeval": "4"
            },
            "linefeatures": {
                "commented": False,
                "config": "",
                "configregistrar": "default",
                "context": "default",
                "description": "",
                "device": "1",
                "encryption": False,
                "id": 4,
                "iduserfeatures": 4,
                "internal": False,
                "ipfrom": "192.168.11.106",
                "line_num": 0,
                "name": "iibybz",
                "num": 1,
                "number": "1001",
                "protocol": "sip",
                "protocolid": 4,
                "provisioningid": 111011,
                "rules_group": "",
                "rules_order": 1,
                "rules_time": "30",
                "rules_type": ""
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
                "context": "default",
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
                "mailbox": None,
                "maxcallbitrate": None,
                "maxforwards": None,
                "md5secret": "",
                "mohinterpret": None,
                "mohsuggest": None,
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

    def test_from_list_obj_dict(self):
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
            "context": "default",
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
            "iduserfeatures": 4,
            "ignoresdpversion": None,
            "initialized": False,
            "insecure": None,
            "internal": False,
            "ipaddr": "",
            "ipfrom": "192.168.11.106",
            "language": None,
            "lastms": "",
            "line_num": 0,
            "mailbox": None,
            "maxcallbitrate": None,
            "maxforwards": None,
            "md5secret": "",
            "mohinterpret": None,
            "mohsuggest": None,
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
            "rules_group": "",
            "rules_order": 1,
            "rules_time": "30",
            "rules_type": "",
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
