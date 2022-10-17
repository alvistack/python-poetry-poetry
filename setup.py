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
 'poetry.repositories',
 'poetry.repositories.link_sources',
 'poetry.utils',
 'poetry.vcs',
 'poetry.vcs.git',
 'poetry.version']

package_data = \
{'': ['*'], 'poetry': ['_vendor/*'], 'poetry.json': ['schemas/*']}

install_requires = \
['cachecontrol[filecache]>=0.12.9,<0.13.0',
 'cachy>=0.3.0,<0.4.0',
 'cleo>=1.0.0a5,<2.0.0',
 'crashtest>=0.3.0,<0.4.0',
 'dulwich>=0.20.44,<0.21.0',
 'html5lib>=1.0,<2.0',
 'jsonschema>=4.10.0,<5.0.0',
 'keyring>=21.2.0',
 'packaging>=20.4',
 'pexpect>=4.7.0,<5.0.0',
 'pkginfo>=1.5,<2.0',
 'platformdirs>=2.5.2,<3.0.0',
 'poetry-core==1.1.0',
 'poetry-plugin-export>=1.0.6,<2.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.18,<3.0',
 'shellingham>=1.5,<2.0',
 'tomlkit>=0.11.1,<1.0.0,!=0.11.2,!=0.11.3',
 'urllib3>=1.26.0,<2.0.0',
 'virtualenv']

extras_require = \
{':python_version < "3.10"': ['importlib-metadata>=4.4,<5.0'],
 ':sys_platform == "darwin"': ['xattr>=0.9.7,<0.10.0']}

entry_points = \
{'console_scripts': ['poetry = poetry.console.application:main']}

setup_kwargs = {
    'name': 'poetry',
    'version': '1.2.0',
    'description': 'Python dependency management and packaging made easy.',
    'long_description': '# Poetry: Dependency Management for Python\n\n[![Tests Status](https://github.com/python-poetry/poetry/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/python-poetry/poetry/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)\n[![Stable Version](https://img.shields.io/pypi/v/poetry?label=stable)](https://pypi.org/project/poetry/)\n[![Pre-release Version](https://img.shields.io/github/v/release/python-poetry/poetry?label=pre-release&include_prereleases&sort=semver)](https://pypi.org/project/poetry/#history)\n[![Downloads](https://img.shields.io/pypi/dm/poetry)](https://pypistats.org/packages/poetry)\n[![Discord](https://img.shields.io/discord/487711540787675139?logo=discord)](https://discord.com/invite/awxPgve)\n\nPoetry helps you declare, manage and install dependencies of Python projects,\nensuring you have the right stack everywhere.\n\nIt requires Python 3.7+ to run.\n\n![Poetry Install](https://raw.githubusercontent.com/python-poetry/poetry/master/assets/install.gif)\n\n## Documentation\n\nThe [complete documentation](https://python-poetry.org/docs/) is available on the [official website](https://python-poetry.org).\n\n## Installation\n\nInstructions on how to install `poetry` can be found [here](https://python-poetry.org/docs/master/#installation).\nYou can also refer [here](https://python-poetry.org/docs/master/#enable-tab-completion-for-bash-fish-or-zsh) for\ninformation on how to enable tab completion in your environment.\n\n## Introduction\n\n`poetry` is a tool to handle dependency installation as well as building and packaging of Python packages.\nIt only needs one file to do all of that: the new, [standardized](https://www.python.org/dev/peps/pep-0518/) `pyproject.toml`.\n\nIn other words, poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and `Pipfile`.\n\n```toml\n[tool.poetry]\nname = "my-package"\nversion = "0.1.0"\ndescription = "The description of the package"\n\nlicense = "MIT"\n\nauthors = [\n    "Sébastien Eustace <sebastien@eustace.io>"\n]\n\nreadme = "README.md"\n\nrepository = "https://github.com/python-poetry/poetry"\nhomepage = "https://python-poetry.org"\n\nkeywords = ["packaging", "poetry"]\n\n[tool.poetry.dependencies]\npython = "^3.8"  # Compatible python versions must be declared here\naiohttp = "^3.8.1"\n# Dependencies with extras\nrequests = { version = "^2.28", extras = [ "security" ] }\n# Python specific dependencies with prereleases allowed\ntomli = { version = "^2.0.1", python = "<3.11", allow-prereleases = true }\n# Git dependencies\ncleo = { git = "https://github.com/python-poetry/cleo.git", branch = "master" }\n\n# Optional dependencies (extras)\npendulum = { version = "^2.1.2", optional = true }\n\n[tool.poetry.dev-dependencies]\npytest = "^7.1.2"\npytest-cov = "^3.0"\n\n[tool.poetry.scripts]\nmy-script = "my_package:main"\n```\n\nThere are some things we can notice here:\n\n* It will try to enforce [semantic versioning](<http://semver.org>) as the best practice in version naming.\n* You can specify the readme, included and excluded files: no more `MANIFEST.in`.\n`poetry` will also use VCS ignore files (like `.gitignore`) to populate the `exclude` section.\n* Keywords can be specified and will act as tags on the packaging site.\n* The dependencies sections support caret, tilde, wildcard, inequality and multiple requirements.\n* You must specify the python versions for which your package is compatible.\n\n`poetry` will also detect if you are inside a virtualenv and install the packages accordingly.\nSo, `poetry` can be installed globally and used everywhere.\n\n`poetry` also comes with a full fledged dependency resolution library.\n\n## Why?\n\nPackaging systems and dependency management in Python are rather convoluted and hard to understand for newcomers.\nEven for seasoned developers it might be cumbersome at times to create all files needed in a Python project: `setup.py`,\n`requirements.txt`, `setup.cfg`, `MANIFEST.in` and `Pipfile`.\n\nSo I wanted a tool that would limit everything to a single configuration file to do:\ndependency management, packaging and publishing.\n\nIt takes inspiration in tools that exist in other languages, like `composer` (PHP) or `cargo` (Rust).\n\nAnd, finally, I started `poetry` to bring another exhaustive dependency resolver to the Python community apart from\n[Conda\'s](https://conda.io).\n\n## Resources\n\n* [Official Website](https://python-poetry.org)\n* [Issue Tracker](https://github.com/python-poetry/poetry/issues)\n* [Discord](https://discord.com/invite/awxPgve)\n',
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
