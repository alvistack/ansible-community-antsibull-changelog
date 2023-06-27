# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='antsibull-changelog',
    version='0.21.0',
    description='Changelog tool for Ansible-base and Ansible collections',
    author_email='Felix Fontein <felix@fontein.de>, Toshio Kuratomi <a.badger@gmail.com>, Matt Clay <matt@mystile.com>',
    maintainer_email='Felix Fontein <felix@fontein.de>, Maxwell G <maxwell@gtmx.me>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Ansible',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Typing :: Typed',
    ],
    install_requires=[
        'docutils',
        'packaging',
        'pyyaml',
        'rstcheck<7.0.0,>=3.0.0',
        'semantic-version',
    ],
    extras_require={
        'codeqa': [
            'flake8>=3.8.0',
            'pylint',
            'reuse',
        ],
        'coverage': [
            'coverage[toml]',
        ],
        'dev': [
            'antsibull-changelog[codeqa]',
            'antsibull-changelog[coverage]',
            'antsibull-changelog[formatters]',
            'antsibull-changelog[test]',
            'antsibull-changelog[typing]',
            'nox',
        ],
        'formatters': [
            'black',
            'isort',
        ],
        'test': [
            'pytest',
            'pytest-cov',
            'pytest-error-for-skips',
        ],
        'typing': [
            'mypy',
            'pyre-check>=0.9.17',
            'types-docutils',
            'types-pyyaml',
            'types-toml',
        ],
    },
    entry_points={
        'console_scripts': [
            'antsibull-changelog = antsibull_changelog.cli:main',
        ],
    },
    packages=[
        'antsibull_changelog',
    ],
    package_dir={'': 'src'},
)
