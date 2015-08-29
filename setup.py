# -*- coding: utf-8 -*-


import os
import re
import io
import sys
import shlex
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA


base_path = os.path.dirname(__file__)


# version
meta_file = os.path.join(base_path, 'czech_holidays.py')
meta_file_contents = io.open(meta_file, encoding='utf-8').read()
meta = dict(re.findall(r'__([^_]+)__ = \'([^\']*)\'', meta_file_contents))


# release a version, publish to GitHub and PyPI
if sys.argv[-1] == 'publish':
    command = lambda cmd: subprocess.check_call(shlex.split(cmd))
    command('git tag v' + meta['version'])
    command('git push --tags origin master:master')
    command('python setup.py sdist upload')
    sys.exit()


setup(
    name=meta['title'],
    version=meta['version'],
    description='Czech holidays on PyPI.',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    author=meta['author'],
    author_email='jan.javorek@gmail.com',
    url='https://github.com/honzajavorek/czech-holidays',
    license=open('LICENSE').read(),
    py_modules=['czech_holidays'],
    include_package_data=True,
    install_requires=['python-dateutil'],
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    )
)
