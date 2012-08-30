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
from xivo_ws.objects.queue import Queue


class TestQueue(unittest.TestCase):
    def test_to_obj_dict(self):
        expected_obj_dict = {
            'queuefeatures': {
                'timeout': '0',
                'hitting_caller': True,
                'transfer_user': True,
                'name': 'foo',
                'displayname': 'Foo bar',
                'number': '555',
                'context': 'default',
                'waittime': 5,
                'waitratio': 100,
            },
            'queue': {
                'musicclass': 'default',
                'min-announce-frequency': '60',
                'announce-position': 'yes',
                'announce-position-limit': '5',
                'timeoutpriority': 'app',
                'ringinuse': True,
                'autofill': True,
                'setqueueentryvar': True,
                'setqueuevar': True,
                'strategy': 'linear',
                'maxlen': 0,
                'joinempty': 'unavailable',
                'leavewhenempty': 'unavailable, pause',
                'timeout': 30,
                'autopause': False,
            },
            'dialaction': {
                'noanswer': {
                    'actiontype': 'none',
                },
                'busy': {
                    'actiontype': 'none',
                },
                'congestion': {
                    'actiontype': 'none',
                },
                'chanunavail': {
                    'actiontype': 'none',
                },
                'qwaittime': {
                    'actiontype': 'none',
                },
                'qwaitratio': {
                    'actiontype': 'none',
                },
            },
            'agent': [1, 2],
            'schedule_id': 1
        }
        queue = Queue(id=1,
                      name='foo',
                      display_name='Foo bar',
                      number='555',
                      context='default',
                      ring_strategy='linear',
                      maxlen=0,
                      joinempty='unavailable',
                      leavewhenempty='unavailable, pause',
                      autopause=False,
                      reachability_timeout=30,
                      waittime=5,
                      waitratio=100,
                      agents=[1, 2],
                      schedule_id=1)

        obj_dict = queue.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = {
            "agent": False,
            "callerid": {
                "callerdisplay": "",
                "mode": None,
                "type": "queue",
                "typeval": "35"
            },
            "dialaction": {
                "busy": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "busy",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                },
                "chanunavail": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "chanunavail",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                },
                "congestion": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "congestion",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                },
                "noanswer": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "noanswer",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                },
                "qwaitratio": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "qwaitratio",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                },
                "qwaittime": {
                    "action": None,
                    "actionarg1": None,
                    "actionarg2": None,
                    "actiontype": "none",
                    "application": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "category": "queue",
                    "categoryval": "35",
                    "custom": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "endcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "event": "qwaittime",
                    "extension": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "group": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "linked": True,
                    "meetme": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "none": {
                        "action": "none",
                        "actionarg1": None,
                        "actionarg2": None
                    },
                    "outcall": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "queue": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "schedule": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "sound": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "user": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemail": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    },
                    "voicemenu": {
                        "action": "",
                        "actionarg1": "",
                        "actionarg2": ""
                    }
                }
            },
            "queue": {
                "announce": "",
                "announce-frequency": "0",
                "announce-holdtime": "no",
                "announce-position": "yes",
                "announce-position-limit": "5",
                "announce-round-seconds": "0",
                "autofill": "1",
                "autopause": "1",
                "category": "queue",
                "commented": False,
                "context": None,
                "defaultrule": None,
                "eventmemberstatus": "1",
                "eventwhencalled": "1",
                "joinempty": "",
                "leavewhenempty": "",
                "maxlen": 0,
                "memberdelay": "0",
                "membermacro": None,
                "min-announce-frequency": "60",
                "monitor-format": None,
                "monitor-type": None,
                "musicclass": "default",
                "name": "n1022",
                "periodic-announce": "queue-periodic-announce",
                "periodic-announce-frequency": "0",
                "queue-callswaiting": "queue-callswaiting",
                "queue-holdtime": "queue-holdtime",
                "queue-minutes": "queue-minutes",
                "queue-reporthold": "queue-reporthold",
                "queue-seconds": "queue-seconds",
                "queue-thankyou": "queue-thankyou",
                "queue-thereare": "queue-thereare",
                "queue-youarenext": "queue-youarenext",
                "random-periodic-announce": "0",
                "reportholdtime": "0",
                "retry": "5",
                "ringinuse": "1",
                "servicelevel": "0",
                "setinterfacevar": "0",
                "setqueueentryvar": "1",
                "setqueuevar": "1",
                "strategy": "ringall",
                "timeout": "15",
                "timeoutpriority": "app",
                "timeoutrestart": "0",
                "weight": "0",
                "wrapuptime": "0"
            },
            "queuefeatures": {
                "announce_holdtime": "0",
                "announceoverride": "",
                "context": "default",
                "ctipresence": None,
                "data_quality": "0",
                "displayname": "dn1022",
                "hitting_callee": "0",
                "hitting_caller": "1",
                "id": 35,
                "identity": "n1022 (1022@default)",
                "name": "n1022",
                "nonctipresence": None,
                "number": "1022",
                "preprocess_subroutine": None,
                "retries": "0",
                "ring": "0",
                "timeout": "0",
                "transfer_call": "0",
                "transfer_user": "1",
                "url": "",
                "waitratio": 100,
                "waittime": 5,
                "write_caller": "0",
                "write_calling": "0"
            },
            "user": False,
            'schedule_id': 1
        }

        queue = Queue.from_obj_dict(obj_dict)

        self.assertEqual(35, queue.id)
        self.assertEqual('n1022', queue.name)
        self.assertEqual('dn1022', queue.display_name)
        self.assertEqual('1022', queue.number)
        self.assertEqual('default', queue.context)
        self.assertEqual(0, queue.maxlen)
        self.assertEqual(100, queue.waitratio)
        self.assertEqual(5, queue.waittime)

    def test_from_list_obj_dict(self):
        obj_dict = {
            "announce_holdtime": "0",
            "announceoverride": "",
            "category": "queue",
            "commented": False,
            "context": "default",
            "ctipresence": None,
            "data_quality": "0",
            "displayname": "dn1022",
            "hitting_callee": "0",
            "hitting_caller": "1",
            "id": "35",
            "identity": "dn1022 (1022@default)",
            "name": "n1022",
            "nb_qmember": "0",
            "nonctipresence": None,
            "number": "1022",
            "preprocess_subroutine": None,
            "retries": "0",
            "ring": "0",
            "timeout": "0",
            "transfer_call": "0",
            "transfer_user": "1",
            "url": "",
            "waitratio": 100,
            "waittime": 5,
            "write_caller": "0",
            "write_calling": "0",
        }

        queue = Queue.from_list_obj_dict(obj_dict)

        self.assertEqual(35, queue.id)
        self.assertEqual('n1022', queue.name)
        self.assertEqual('dn1022', queue.display_name)
        self.assertEqual('1022', queue.number)
        self.assertEqual('default', queue.context)
        self.assertEqual(100, queue.waitratio)
        self.assertEqual(5, queue.waittime)
