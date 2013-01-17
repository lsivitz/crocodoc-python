import os
import sys
from crocodoc import version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='crocodoc',
      version=version.VERSION,
      description='Python wrapper for the Crocodoc API',
      author='Brandon Goldman',
      author_email='brandon.goldman@gmail.com',
      url='https://crocodoc.com/docs/api/',
      packages=['crocodoc'],
)