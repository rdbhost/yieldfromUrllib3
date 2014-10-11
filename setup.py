#!/usr/bin/env python

from distutils.core import setup

import os
import re

try:
    import setuptools
except ImportError:
    pass # No 'develop' command, oh well.

setup(name='yieldfrom.urllib3',

      version='0.1',

      description="Asyncio HTTP library with thread-safe connection pooling, file post, and more.",
      long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read(),
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='urllib httplib asyncio filepost http https ssl pooling',

      author='Andrey Petrov',
      author_email='andrey.petrov@shazow.net',
      maintainer='David Keeney',
      maintainer_email='dkeeney@rdbhost.com',

      url='http://urllib3.readthedocs.org/',
      license='MIT',

      packages=['yieldfrom.urllib3',
                'yieldfrom.urllib3.packages', 'yieldfrom.urllib3.packages.ssl_match_hostname',
                'yieldfrom.urllib3.util',
                ],
      package_dir = {'yieldfrom': 'yieldfrom'},
      install_requires=['yieldfrom.http.client', 'setuptools'],
      namespace_packages = ['yieldfrom'],

      test_suite='test',
      )
