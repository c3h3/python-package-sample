#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup

from setuptools import setup, find_packages

setup(
    name='test',
    version='0.0.1dev',
    author='TEST',
    author_email='TEST@test.test',
    packages=find_packages(),
    install_requires=[],
)
