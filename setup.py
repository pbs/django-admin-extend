#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-admin-extend',
    version='0.0.2.pbs.4',
    description=('Provides functionality for extending'
                 'ModelAdmin classes that have already'
                 'been registered by other apps'),
    author='Ioan Alexandru Cucu',
    author_email='alexandruioan.cucu@gmail.com',
    url='https://github.com/kux/django-admin-extend',
    install_requires=["Django>=1.7,<1.9", ],
    packages=find_packages(),
    include_package_data=True,
)
