"""packaging"""
from setuptools import setup


def read_file(path):
    """Read a while file into a string"""
    with open(path) as infile:
        return infile.read()


setup(
    name='wavenet',
    version='0.1.1',
    packages=['wavenet'],
    install_requires=read_file('requirements.txt').split('\n'),
    descriptions='wavenet things',
    long_description=read_file('README.md'),
)
