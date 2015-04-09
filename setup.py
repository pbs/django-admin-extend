#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-admin-extend',
    version='0.0.2.pbs.2',
    description=('Provides functionality for extending'
                 'ModelAdmin classes that have already'
                 'been registered by other apps'),
    author='Ioan Alexandru Cucu',
    author_email='alexandruioan.cucu@gmail.com',
    url='https://github.com/kux/django-admin-extend',
    install_requires=('Django>=1.3,<1.5',),
    packages=find_packages(),
    include_package_data=True,
    setup_requires = ['s3sourceuploader', ],
)
