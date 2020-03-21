# -*- encoding: utf-8 -*-
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


# Werkzeug and Flask do it like this, requests just does `eval('__version.py__').
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'samesite_compat_check', '__version__.py')) as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)


# fmt: off
setup(
    name="samesite-compat-check",
    version=version,
    url="https://github.com/peergradeio/samesite-compat-check",
    license='Apache License 2.0',

    author="Malthe Jørgensen",
    author_email="malthe.jorgensen@gmail.com",

    description="A port of Chrome's browser compatibility check for SameSite=None cookies",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests',)),

    install_requires=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
