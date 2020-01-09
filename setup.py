#!/usr/bin/env python

# pyre-fixme[21]: Could not find `setuptools`.
from setuptools import find_packages, setup

setup(
    version='0.1',
    description='Source API',
    author='Kristoffer Dalby',
    author_email='kradalby@kradalby.no',
    packages=find_packages(),
    test_suite='tests',
)
