#!/usr/bin/env python
from setuptools import setup, find_packages

# Adding this import avoids an exception caused by nosetests
# http://stackoverflow.com/questions/9352656/python-assertionerror-when-running-nose-tests-with-coverage
from multiprocessing import util
util = util  # make pyflakes/etc happy


def requirements(filename='requirements.txt'):
    with open(filename, 'r') as f:
        return f.readlines()


setup(
    name='prove-it',
    version='0.0.1',
    author='Jess Stanton',
    author_email='jess.m.stanton@gmail.com',
    packages=find_packages(),
    description='This is a play repo to help teach testing and debugging',
    install_requires=requirements(),
    test_suite='nose.collector',
    url='https://github.com/tiny-mouse/prove-it',
)
