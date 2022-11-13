from setuptools import setup, find_packages

setup(name='falcon',
      version='0.0.2',
      description='A DSL for the creation of tests',
      author='Aaron Kuhlman',
      author_email='kuhlmaa@bgsu.edu',
      install_requires=['pytest', 'toolz', 'antlr4-python3-runtime'],
      license='Apache License 2.0')
