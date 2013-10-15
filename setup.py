#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup
from xivo_ws.version import version

setup(
    name='xivo-ws',
    version=version,
    description='A library for the XiVO web services.',
    url='https://github.com/xivo-pbx/xivo-ws.git',
    packages=['xivo_ws',
              'xivo_ws.bin',
              'xivo_ws.client',
              'xivo_ws.debug',
              'xivo_ws.debug.client',
              'xivo_ws.objects',
              'xivo_ws.objects.common'],
    scripts=['bin/xivo-ws-debug'],
    license='GPLv3',
    long_description=open('README').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
