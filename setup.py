#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 -- Lars Heuer.
# All rights reserved.
#
# License: BSD License
#
"""\
Setup script.

:author:       Lars Heuer
:license:      BSD License
"""
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os
import io
import re


def read(*filenames, **kwargs):
    base_path = os.path.dirname(os.path.realpath(__file__))
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(os.path.join(base_path, filename), encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

version = re.search(r'''^__version__ = ["']([^'"]+)['"]''',
                    read('ftapp.py'), flags=re.MULTILINE).group(1)

setup(
    name='ftapp',
    version=version,
    url='https://github.com/heuer/ftapp/',
    description='Script zur Erstellung einer fischertechnik Anwendung',
    long_description=read('README.rst', 'CHANGES.rst'),
    license='BSD',
    author='Lars Heuer',
    author_email='heuer@semagia.com',
    platforms=['any'],
    install_requires=['click>=5.1'],
    packages=find_packages(exclude=['docs', 'tests', 'htmlcov']),
    py_modules=['ftapp'],
    include_package_data=True,
    keywords=['fischertechnik', 'ftduino'],
    entry_points={
        'console_scripts': [
            'ftapp = ftapp:cli',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
