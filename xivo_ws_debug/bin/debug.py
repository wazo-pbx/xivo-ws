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
import readline
import sys
from xivo_ws.facade import XivoServer
from xivo_ws.exception import WebServiceRequestError
from xivo_ws_debug.editor import read_content_from_editor
from xivo_ws_debug.formatter import JSONFormatter, PprintFormatter, \
    PythonFormatter


def main():
    parsed_args = _parse_args(sys.argv[1:])

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
    add_raw_data = ''
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
                if action == 'add':
                    add_raw_data = read_content_from_editor(add_raw_data)
                    if not add_raw_data.rstrip():
                        print 'Aborting add due to empty data'
                        add_raw_data = ''
                        continue
                    data = eval(add_raw_data)
                    obj.raw_add(data)
                elif action == 'delete':
                    object_id = tail
                    obj.raw_delete(object_id)
                elif action == 'delete_all':
                    obj.raw_delete_all()
                elif action == 'list':
                    print formatter.format(obj.raw_list())
                elif action == 'search':
                    search_pattern = tail
                    print formatter.format(obj.raw_search(search_pattern))
                elif action == 'view':
                    object_id = tail
                    print formatter.format(obj.raw_view(object_id))
                else:
                    print 'Unknown action %r' % action
            except WebServiceRequestError as e:
                print e
            except KeyboardInterrupt:
                print
            except EOFError:
                raise
            except Exception as e:
                print 'Unexpected exception:', e
    except EOFError:
        print


if __name__ == '__main__':
    main()
