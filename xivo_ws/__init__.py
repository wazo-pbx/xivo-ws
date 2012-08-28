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

from xivo_ws.destination import GroupDestination, QueueDestination
from xivo_ws.exception import WebServiceError, WebServiceRequestError
from xivo_ws.facade import XivoServer
from xivo_ws.objects.agent import Agent
from xivo_ws.objects.context import Context, ContextRange
from xivo_ws.objects.device import Device
from xivo_ws.objects.entity import Entity
from xivo_ws.objects.group import Group
from xivo_ws.objects.incall import Incall
from xivo_ws.objects.line import Line
from xivo_ws.objects.outcall import Outcall, OutcallExten
from xivo_ws.objects.queue import Queue
from xivo_ws.objects.siptrunk import SIPTrunk
from xivo_ws.objects.statconf import Statconf
from xivo_ws.objects.user import User, UserLine, UserVoicemail
from xivo_ws.objects.trunk_custom import TrunkCustom
