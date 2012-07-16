# -*- coding: UTF-8 -*-

from distutils.core import setup
from xivo_ws.version import version

setup(
    name='xivo-ws',
    version=version,
    description='Enable programmatic access to a XiVO server via the XiVO web services.',
    url='https://gitorious.org/xivo/xivo-ws',
    packages=['xivo_ws',
              'xivo_ws.client',
              'xivo_ws.objects',
              'xivo_ws.objects.common',
              'xivo_ws_debug',
              'xivo_ws_debug.bin',
              'xivo_ws_debug.client'],
    scripts=['bin/xivo-ws-debug'],
    license='GPLv3',
    long_description=open('README').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
