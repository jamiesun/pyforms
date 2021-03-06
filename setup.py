#!/usr/bin/python
from setuptools import setup, find_packages
version = '0.1'

setup(name='pyforms',
      version=version,
      author='jamiesun',
      author_email='jamiesun.net@gmail.com',
      url='https://github.com/jamiesun/pyforms',
      license='Public domain',
      description='web app forms tools',
      long_description=open('README.md').read(),
      classifiers=[
       'Development Status :: 6 - Mature',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3.2',
       'Topic :: Software Development :: Libraries :: Python Modules',
       'Topic :: Internet :: WWW/HTTP',
       ],
      packages=find_packages(exclude=['tests']),
      keywords=['web', 'form','html','http'],
      zip_safe=True,
      include_package_data=True,
      )