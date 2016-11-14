#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='triptranslator',
    version='0.1.0',
    description="Python library for translating boarding passes into human readable directions.",
    long_description=readme,
    author="Marek Szwałkiewicz",
    author_email='marek@szwalkiewicz.waw.pl',
    url='https://github.com/niktto/triptranslator',
    packages=[
        'triptranslator',
    ],
    package_dir={'triptranslator':
                 'triptranslator'},
    include_package_data=True,
    install_requires=[],
    license="MIT license",
    zip_safe=False,
    keywords='triptranslator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[]
)
