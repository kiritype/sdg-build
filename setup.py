# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(name='sdg',
      version='1.7.0',
      description='Build SDG data and metadata into output formats',
      url='https://github.com/open-sdg/sdg-build',
      author='Doug Ashton',
      author_email='douglas.j.ashton@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'check', 'reset']),
      zip_safe=False,
      package_data={'sdg': [
        os.path.join('outputs', 'sdmx_global_content_constraints.csv'),
      ]},
      include_package_data=True,
      python_requires='>=3.5',
      install_requires=['pyyaml', 'gitpython', 'numpy', 'pandas', 'yamlmd', 'jsonschema', 'requests', 'humanize', 'unicode-slugify', 'sdmx1>=2.6.1', 'frictionless', 'csvw', 'mammoth', 'pyquery', 'pyjstat', 'Jinja2', 'natsort'],
      dependency_links=[
        "git+ssh://git@github.com/dougmet/yamlmd.git@0.1.7",
    ])
