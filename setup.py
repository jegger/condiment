#!/usr/bin/env python

from distutils.core import setup
from condiment import __version__
from os.path import join, dirname

setup(
    name='condiment',
    py_modules=['condiment'],
    scripts=['scripts/condiment'],
    version=__version__,
    description='Conditionally include code according to environment',
    author='Mathieu Virbel',
    author_email='mat@kivy.org',
    license=open(join(dirname(__file__), 'LICENSE')).read(),
    keywords=['python', 'preprocessor', 'meta', 'condiment', 'conditional'],
    platforms='all',
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
