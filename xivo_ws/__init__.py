# -*- coding: utf-8 -*-

# Copyright (C) 2012-2016 Avencall
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
import os
from xivo_ws.calleridmode import PrependCallerIDMode, OverwriteCallerIDMode, AppendCallerIDMode
from xivo_ws.destination import GroupDestination, QueueDestination, UserDestination, VoicemailDestination
from xivo_ws.exception import WebServiceError, WebServiceRequestError
from xivo_ws.objects.agent import Agent
from xivo_ws.objects.cel import CEL
from xivo_ws.objects.confroom import ConfRoom
from xivo_ws.objects.context import Context, ContextRange
from xivo_ws.objects.cti_profile import CTIProfile
from xivo_ws.objects.customtrunk import CustomTrunk
from xivo_ws.objects.device import Device
from xivo_ws.objects.entity import Entity
from xivo_ws.objects.group import Group
from xivo_ws.objects.iaxtrunk import IAXTrunk
from xivo_ws.objects.incall import Incall
from xivo_ws.objects.line import Line
from xivo_ws.objects.outcall import Outcall, OutcallExten
from xivo_ws.objects.queue import Queue
from xivo_ws.objects.sccp_general_settings import SCCPGeneralSettings
from xivo_ws.objects.schedule import Schedule
from xivo_ws.objects.siptrunk import SIPTrunk
from xivo_ws.objects.statconf import Statconf
from xivo_ws.objects.user import User, UserLine, UserVoicemail
from xivo_ws.objects.voicemail import Voicemail
from xivo_ws.objects.queueskillrules import QueueSkillRules


if os.environ.get('XIVO_WS_DEBUG'):
    from xivo_ws.facade import DebugXivoServer as XivoServer

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
else:
    from xivo_ws.facade import XivoServer
