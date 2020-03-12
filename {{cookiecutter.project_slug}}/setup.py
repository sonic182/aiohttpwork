"""Setup module."""

import re
from setuptools import setup
from setuptools import find_packages


RGX = re.compile('([\w-]+==[\d.]+)')


def read_file(filename):
    """Read file correctly."""
    with open(filename) as _file:
        return _file.read().strip()


def requirements(filename):
    """Parse requirements from file."""
    return re.findall(RGX, read_file(filename)) or []


setup(
    name='{{cookiecutter.project_slug}}',
    version='0.0.1',
    description='{{cookiecutter.project_description}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    license='{{cookiecutter.license}}',
    setup_requires=['pytest-runner'],
    test_requires=['pytest'],
    install_requires=requirements('./requirements.txt'),
    packages=find_packages(),
    extras_require={
        'dev': requirements('./dev-requirements.txt'),
        'test': [
            'pytest',
            'coverage'
        ]
    }
)
