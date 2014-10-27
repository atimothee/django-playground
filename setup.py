# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django_playground
version = django_playground.__version__

setup(
    name='django_playground',
    version=version,
    author='',
    author_email='atimothee@gmail.com',
    packages=[
        'django_playground',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['django_playground/manage.py'],
)