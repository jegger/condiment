#!/usr/bin/env python

import codecs
from setuptools import find_packages
from distutils.core import setup
from os.path import join, dirname, abspath


def read(rel_path):
    here = abspath(dirname(__file__))
    with codecs.open(join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='condiment',
    py_modules=['condiment'],
    scripts=['scripts/condiment'],
    version="0.6",
    description='Conditionally include code according to environment variables',
    long_description=read("README.md"),
    author='Mathieu Virbel',
    author_email='mat@kivy.org',
    keywords=['python', 'preprocessor', 'meta', 'condiment', 'conditional'],
    platforms='all',
    packages=find_packages(),
    python_requires=">=3.6.5",
    url='http://github.com/tito/condiment',
    license='zlib',
    zip_safe=False,
    install_requires = [],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: zlib/libpng License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators',
    ])
