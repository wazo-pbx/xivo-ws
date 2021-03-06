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
import copy
from xivo_ws.objects.queue import Queue

_QUEUE_OBJ_DICT_TO_WS = {
    'queuefeatures': {
        'timeout': '0',
        'hitting_caller': True,
        'transfer_user': True,
        'name': 'foo',
        'displayname': 'Foo bar',
        'number': '555',
        'context': 'default',
        'waittime': None,
        'waitratio': None,
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
        'strategy': 'ringall',
        'maxlen': 0,
        'joinempty': None,
        'leavewhenempty': None,
        'autopause': True,
        'wrapuptime': 0,
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
    'agent': [],
    'user': [],
}

_QUEUE_OBJ_DICT_FROM_WS = {
    "agent": [
        {
            "call-limit": "0",
            "category": "queue",
            "channel": "Agent",
            "commented": False,
            "interface": "Agent/101",
            "paused": None,
            "penalty": "2",
            "queue_name": "n1022",
            "skills": "agent-50",
            "state_interface": "",
            "userid": 50,
            "usertype": "agent"
        },
        {
            "call-limit": "0",
            "category": "queue",
            "channel": "Agent",
            "commented": False,
            "interface": "Agent/102",
            "paused": None,
            "penalty": "6",
            "queue_name": "n1022",
            "skills": "agent-95",
            "state_interface": "",
            "userid": 95,
            "usertype": "agent"
        }
    ],
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
        "waitratio": 1,
        "waittime": 5,
        "write_caller": "0",
        "write_calling": "0"
    },
    "user": False,
}


class TestQueue(unittest.TestCase):
    def test_to_obj_dict_full(self):
        expected_obj_dict = copy.deepcopy(_QUEUE_OBJ_DICT_TO_WS)
        expected_obj_dict['queuefeatures']['waittime'] = 5
        expected_obj_dict['queuefeatures']['waitratio'] = 1
        expected_obj_dict['queuefeatures']['timeout'] = '10'
        expected_obj_dict['queue']['autopause'] = False
        expected_obj_dict['queue']['leavewhenempty'] = 'unavailable, pause'
        expected_obj_dict['queue']['joinempty'] = 'unavailable'
        expected_obj_dict['queue']['maxlen'] = 1
        expected_obj_dict['queue']['strategy'] = 'linear'
        expected_obj_dict['queue']['timeout'] = 30
        expected_obj_dict['queue']['wrapuptime'] = 15
        expected_obj_dict['schedule_id'] = 1
        expected_obj_dict['agent'] = [1, 2]
        queue = Queue(id=1,
                      name='foo',
                      display_name='Foo bar',
                      number='555',
                      context='default',
                      ring_strategy='linear',
                      ringing_time=10,
                      maxlen=1,
                      joinempty='unavailable',
                      leavewhenempty='unavailable, pause',
                      autopause=False,
                      reachability_timeout=30,
                      waittime=5,
                      waitratio=1,
                      agents=[1, 2],
                      schedule_id=1,
                      wrapuptime=15,)

        obj_dict = queue.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_to_obj_dict_minimum(self):
        expected_obj_dict = copy.deepcopy(_QUEUE_OBJ_DICT_TO_WS)
        queue = Queue(id=1,
                      name='foo',
                      display_name='Foo bar',
                      number='555',
                      context='default',)

        obj_dict = queue.to_obj_dict()

        self.assertEqual(expected_obj_dict, obj_dict)

    def test_from_obj_dict(self):
        obj_dict = copy.deepcopy(_QUEUE_OBJ_DICT_FROM_WS)

        queue = Queue.from_obj_dict(obj_dict)

        self.assertEqual(35, queue.id)
        self.assertEqual('n1022', queue.name)
        self.assertEqual('dn1022', queue.display_name)
        self.assertEqual('1022', queue.number)
        self.assertEqual('default', queue.context)
        self.assertEqual(0, queue.maxlen)
        self.assertEqual(0, queue.ringing_time)
        self.assertEqual(1, queue.waitratio)
        self.assertEqual(5, queue.waittime)
        self.assertEqual(None, queue.schedule_id)
        self.assertEqual([50, 95], queue.agents)

    def test_from_obj_dict_with_schedule_id(self):
        obj_dict = copy.deepcopy(_QUEUE_OBJ_DICT_FROM_WS)
        obj_dict['schedule_id'] = 1

        queue = Queue.from_obj_dict(obj_dict)

        self.assertEqual(35, queue.id)
        self.assertEqual('n1022', queue.name)
        self.assertEqual('dn1022', queue.display_name)
        self.assertEqual('1022', queue.number)
        self.assertEqual('default', queue.context)
        self.assertEqual(0, queue.ringing_time)
        self.assertEqual(0, queue.maxlen)
        self.assertEqual(1, queue.waitratio)
        self.assertEqual(5, queue.waittime)
        self.assertEqual(1, queue.schedule_id)
        self.assertEqual([50, 95], queue.agents)

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
            "timeout": "10",
            "transfer_call": "0",
            "transfer_user": "1",
            "url": "",
            "waitratio": 1,
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
        self.assertEqual(10, queue.ringing_time)
        self.assertEqual(1, queue.waitratio)
        self.assertEqual(5, queue.waittime)
