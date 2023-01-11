# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['antsibull_changelog']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML',
 'docutils',
 'packaging',
 'rstcheck>=3.0.0,<7.0.0',
 'semantic_version']

entry_points = \
{'console_scripts': ['antsibull-changelog = antsibull_changelog.cli:main']}

setup_kwargs = {
    'name': 'antsibull-changelog',
    'version': '0.18.0',
    'description': 'Changelog tool for Ansible-base and Ansible collections',
    'author': 'Felix Fontein',
    'author_email': 'felix@fontein.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ansible-community/antsibull-changelog',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
