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

import os
import subprocess
import tempfile

_DEFAULT_EDITOR = 'vi'


def read_content_from_editor(initial_content=None):
    editor_cmd = _get_editor_cmd()
    filename = _create_tmpfile(initial_content, '.py')
    try:
        _edit_file(editor_cmd, filename)
        content = _read_file(filename)
    finally:
        os.remove(filename)

    return content


def _get_editor_cmd():
    return os.environ.get('EDITOR', _DEFAULT_EDITOR)


def _create_tmpfile(content, suffix):
    fd, filename = tempfile.mkstemp(suffix)
    try:
        if content:
            os.write(fd, content)
    finally:
        os.close(fd)

    return filename


def _edit_file(editor_cmd, filename):
    subprocess.call([editor_cmd, filename])


def _read_file(filename):
    with open(filename) as fobj:
        return fobj.read()
