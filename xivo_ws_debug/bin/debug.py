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

import argparse
import getpass
import readline
import sys
from xivo_ws_debug.formatter import JSONFormatter, PprintFormatter, \
    PythonFormatter
from xivo_ws.facade import XivoServer
from xivo_ws.exception import WebServiceRequestError


def main():
    parsed_args = _parse_args(sys.argv[1:])

    if parsed_args.username is None:
        parsed_args.user = raw_input('Username: ')
    if parsed_args.password is None:
        parsed_args.password = getpass.getpass('Password: ')

    if parsed_args.format == 'json':
        formatter = JSONFormatter()
    elif parsed_args.format == 'pprint':
        formatter = PprintFormatter()
    elif parsed_args.format == 'python':
        formatter = PythonFormatter()
    else:
        print >> sys.stderr, 'Unknown format %r' % parsed_args.format
        sys.exit(1)

    xivo_ws = XivoServer(parsed_args.hostname, parsed_args.username, parsed_args.password)
    loop(xivo_ws, formatter)


def _parse_args(args):
    parser = _new_argument_parser()
    return parser.parse_args(args)


def _new_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username',
                        help='authentication username')
    parser.add_argument('-p', '--password',
                        help='authentication password')
    parser.add_argument('--format', choices=['json', 'pprint', 'python'], default='json',
                        help='print format')
    parser.add_argument('hostname',
                        help='hostname of xivo server')
    return parser


def loop(xivo_ws, formatter):
    try:
        while True:
            try:
                command = raw_input('ws_debug> ')
                obj_name, sep, tail = command.partition(' ')
                if not obj_name:
                    continue

                try:
                    obj = getattr(xivo_ws, obj_name)
                except AttributeError:
                    print 'Unknown name %r' % obj_name
                    continue

                action, sep, tail = tail.rstrip().partition(' ')
                if action == 'list':
                    data = formatter.format(obj.raw_list())
                elif action == 'search':
                    search_pattern = tail
                    data = formatter.format(obj.raw_search(search_pattern))
                elif action == 'view':
                    object_id = tail
                    data = formatter.format(obj.raw_view(object_id))
                else:
                    data = 'Unknown action %r' % action
                print data
            except WebServiceRequestError as e:
                print e
            except KeyboardInterrupt:
                print
    except EOFError:
        print


if __name__ == '__main__':
    main()
