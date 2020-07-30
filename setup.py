#!/usr/bin/env python

# stdlib
import os
import pathlib
import sys
import warnings

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import

if not pathlib.Path("rsc_on_this_day.1").is_file():
	warnings.warn("manpage not found. Trying to build now.")
	exit_code = os.system("./make_manpage.sh")
	if exit_code:
		sys.exit(exit_code)

setup(
		description='Displays Royal Society of Chemistry "On This Day" facts.',
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		)

# TODO: include manpage in wheel and put in right place on filesystem
