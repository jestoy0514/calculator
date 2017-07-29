#!/usr/bin/env python3

from distutils.core import setup

config = {'name': 'Calculator',
    'version': '1.0',
    'description': 'A simple calculator.',
    'author': 'Jesus Vedasto Olazo',
    'author_email': 'jessie@jestoy.frihost.net',
    'url': 'https://github.com/jestoy0514/calculator',
    'packages': ['calculator'],
    'license': 'GNU General Public License Version 3'
    }

setup(**config)
