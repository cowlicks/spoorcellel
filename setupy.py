#!/usr/bin/env python

from os.path import exists
from setuptools import setup
setup(name='spoorcellel',
      version='0.0.1',
      description='larger than memory parallel sparse matrices',
      maintainer='Blake Griffith',
      maintainer_email='blake.a.griffith@gmail.com',
      license='BSD',
      keywords='task-scheduling parallelism',
      packages=['spoorcellel'],
      requires=['dask', 'toolz', 'chest', 'numpy'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
