# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry',
 'poetry.config',
 'poetry.console',
 'poetry.console.commands',
 'poetry.console.commands.cache',
 'poetry.console.commands.debug',
 'poetry.console.commands.env',
 'poetry.console.commands.self',
 'poetry.console.commands.self.show',
 'poetry.console.commands.source',
 'poetry.console.events',
 'poetry.console.io',
 'poetry.console.io.inputs',
 'poetry.console.logging',
 'poetry.console.logging.formatters',
 'poetry.inspection',
 'poetry.installation',
 'poetry.installation.operations',
 'poetry.json',
 'poetry.layouts',
 'poetry.masonry',
 'poetry.masonry.builders',
 'poetry.mixology',
 'poetry.mixology.solutions',
 'poetry.mixology.solutions.providers',
 'poetry.mixology.solutions.solutions',
 'poetry.packages',
 'poetry.plugins',
 'poetry.publishing',
 'poetry.puzzle',
 'poetry.pyproject',
 'poetry.repositories',
 'poetry.repositories.link_sources',
 'poetry.toml',
 'poetry.utils',
 'poetry.vcs',
 'poetry.vcs.git',
 'poetry.version']

package_data = \
{'': ['*'], 'poetry.json': ['schemas/*']}

install_requires = \
['build>=0.10.0,<0.11.0',
 'cachecontrol[filecache]>=0.12.9,<0.13.0',
 'cleo>=2.0.0,<3.0.0',
 'crashtest>=0.4.1,<0.5.0',
 'dulwich>=0.21.2,<0.22.0',
 'filelock>=3.8.0,<4.0.0',
 'html5lib>=1.0,<2.0',
 'installer>=0.7.0,<0.8.0',
 'jsonschema>=4.10.0,<5.0.0',
 'keyring>=23.9.0,<24.0.0',
 'lockfile>=0.12.2,<0.13.0',
 'packaging>=20.4',
 'pexpect>=4.7.0,<5.0.0',
 'pkginfo>=1.9.4,<2.0.0',
 'platformdirs>=3.0.0,<4.0.0',
 'poetry-core==1.6.0',
 'poetry-plugin-export>=1.3.1,<2.0.0',
 'pyproject-hooks>=1.0.0,<2.0.0',
 'requests-toolbelt>=0.9.1,<2',
 'requests>=2.18,<3.0',
 'shellingham>=1.5,<2.0',
 'tomlkit>=0.11.4,<1.0.0',
 'trove-classifiers>=2022.5.19',
 'urllib3>=1.26.0,<2.0.0',
 'virtualenv>=20.22.0,<21.0.0']

extras_require = \
{':python_version < "3.10"': ['importlib-metadata>=4.4'],
 ':python_version < "3.11"': ['tomli>=2.0.1,<3.0.0'],
 ':python_version < "3.8"': ['backports.cached-property>=1.0.2,<2.0.0'],
 ':sys_platform == "darwin"': ['xattr>=0.10.0,<0.11.0']}

entry_points = \
{'console_scripts': ['poetry = poetry.console.application:main']}

setup_kwargs = {
    'name': 'poetry',
    'version': '1.5.0',
    'description': 'Python dependency management and packaging made easy.',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'Arun Babu Neelicattu',
    'maintainer_email': 'arun.neelicattu@gmail.com',
    'url': 'https://python-poetry.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
