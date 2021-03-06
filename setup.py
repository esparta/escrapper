"""
Setup.py for eScrapper, modules to do scrapping on version control portals,
providing some kind of "API"
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys
import re


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    """ Read a python's file """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as current_file:
            buf.append(current_file.read())
    return sep.join(buf)

LONG_DESCRIPTION = read('README.rst')

SOURCE = read('escrapper/__init__.py')
PATTERN = re.compile(r'''__version__ = ['"](?P<version>[\d.]+)['"]''')
VERSION = PATTERN.search(SOURCE).group('version')


class PyTest(TestCommand):
    """ Mixin to integrate pytest with setup.py """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='escrapper',
    version=VERSION,
    url='http://github.com/esparta/escrapper',
    license='Apache Software License',
    author="Espartaco Palma",
    tests_require=['tox'],
    install_requires=['beautifulsoup4>=4.3.1',
                      'requests>=1.2.3'
                      ],
    cmdclass={'test': PyTest},
    author_email='esparta@gmail.com',
    description='Scrapping tool, can process WebSVN portal ',
    long_description=LONG_DESCRIPTION,
    packages=['escrapper'],
    include_package_data=True,
    platforms='any',
    test_suite='escrapper.test_app',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 1 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={'testing': ['pytest'], }
)
