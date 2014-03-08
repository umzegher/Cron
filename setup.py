#!/usr/bin/python

from distutils.core import setup

setup(
    name='Megacron',
    version='0.1',
    description='Distributed Cron Replacement',
    author='John Tanner, Favian Contreras, Ben Zhegers, Ben Zeghers',
    author_email='megacronteam@gmail.com',
    packages=['API','edit','scheduler','status','worker'],
    url='https://pypi.python.org/pypi/Megacron',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
