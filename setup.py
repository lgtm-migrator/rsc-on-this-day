#!/usr/bin/env python
"""Setup script"""

from __pkginfo__ import (
	author, author_email, install_requires,
	license, long_description, classifiers,
	entry_points, modname, py_modules,
	short_desc, VERSION, web,
	)

from setuptools import setup

from build_manpages.build_manpages import build_manpages, get_build_py_cmd, get_install_cmd
from setuptools.command.build_py import build_py
from setuptools.command.install import install

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
