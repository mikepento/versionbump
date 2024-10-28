import os
from setuptools import setup

# there's probably a better way to do this ??
from versionbump import (
    __title__,
    __desc__,
    __version__,
    __license__,
    __author__,
    __email__)


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    packages=['versionbump'],
    description=__desc__,
    long_description=long_description,
    long_description_type='text/markdown',
    entry_points={
        'console_scripts': [
            'versionbump = versionbump.cli:main'
        ]
    },
    python_requires='>=3.7',
    include_package_data=True
)
