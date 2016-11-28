#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup
from setuptools import find_packages
from xivo_ws.version import version

setup(
    name='xivo-ws',
    version=version,
    description='A library for the XiVO web services.',
    url='https://github.com/wazo-pbx/xivo-ws.git',
    packages=find_packages(),
    scripts=['bin/xivo-ws-debug'],
    license='GPLv3',
    long_description=open('README.md').read(),
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
