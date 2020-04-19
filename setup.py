#!/usr/bin/env python
"""Setup script"""

import pathlib
import sys

from setuptools import setup

from __pkginfo__ import (
	author, author_email, classifiers, entry_points, install_requires, license, long_description, modname, py_modules,
	short_desc, VERSION, web,
	)

if not pathlib.Path("rsc_on_this_day.1").is_file():
	sys.stderr.write("Error: manpage not found. Please build it with `./make_manpage.sh` and try again.\n")
	sys.stderr.flush()
	sys.exit(1)

setup(
		author=author,
		author_email=author_email,
		classifiers=classifiers,
		description=short_desc,
		entry_points=entry_points,
		install_requires=install_requires,
		license=license,
		long_description=long_description,
		name=modname,
		packages=None,
		py_modules=py_modules,
		url=web,
		version=VERSION,
		)

# TODO: include manpage in wheel and put in right place on filesystem
